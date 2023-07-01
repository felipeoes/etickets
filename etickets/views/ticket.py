import random

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from etickets.models import Ticket, User
from etickets.utils import error_decorator
from datetime import datetime
from neomodel import db

# retrieve all ticket nodes
class TicketsList(APIView):
    @error_decorator
    def get(self, request):
        tickets = [user.to_dict() for user in Ticket.nodes.all()]
        return Response(tickets)

# get all available tickets' locations
class TicketsLocations(APIView):
    @error_decorator
    def get(self, request):
        locations = []
        # get unique locations only

        for ticket in Ticket.nodes.all():
            if ticket.location not in locations:
                locations.append(ticket.location)

        return Response(locations)


# Tickets search by name or event
class TicketsSearch(APIView):
    @error_decorator
    def get(self, request, *args, **kwargs):
        fields = [('name', request.GET.get('name', '')),
                  ('event', request.GET.get('event', ''))]
        
        # Filter tickets by name or event and order by datetime
        tickets = Ticket.nodes.filter(**{field + '__icontains': value for field, value in fields if value}).order_by('-datetime')
        tickets = [ticket.to_dict() for ticket in tickets]
        
        return Response(tickets)
     


# class for Ticket CRUD operations
class TicketDetail(APIView):
    @error_decorator
    def get(self, request):
        uid = request.GET.get('uid', '')
        ticket = Ticket.nodes.get(uid=uid)
        return Response(ticket.to_dict())

    @error_decorator
    def post(self, request):
        
        # parse datetime string to datetime object
        try:
            request.data['datetime'] = datetime.strptime(request.data['datetime'], '%Y-%m-%dT%H:%M:%S.%fZ')
        except Exception as e:
            print(e)
            pass
        
        # get user
        user_email = request.data['user_email']
        user = User.nodes.get(email=user_email)
        
        ticket = Ticket(**request.data)
        ticket.save()
        
        # add relationship between user and ticket
        user.tickets.connect(ticket)
        user.save()
         
        return Response(ticket.to_dict())

    @error_decorator
    def put(self, request):
        uid = request.GET.get('uid', '')
        ticket = Ticket.nodes.get(uid=uid)
        ticket.__dict__.update(request.data)
        ticket.save()
        return Response(ticket.to_dict())

    @error_decorator
    def delete(self, request):
        uid = request.GET.get('uid', '')
        ticket = Ticket.nodes.get(uid=uid)
        ticket.delete()
        return Response(ticket.to_dict())

class TicketExchangeOffer(APIView):
    @error_decorator
    def post(self, request):
        # own_product_id = 799
        # wished_product_id = 801
        
        own_ticket_id = request.data.get('own_ticket_id')
        wished_ticket_id = request.data.get('wished_ticket_id')

        # query = f'''
        #     MATCH (o:Ticket), (w:Ticket)
        #     WHERE ID(o)={own_ticket_id} AND ID(w) = {wished_ticket_id}
        #     CREATE (o)-[:EXCHANGE_OFFER]->(w)
        # '''
        query = f'''
            MATCH (o:Ticket), (w:Ticket)
            WHERE o.uid="{own_ticket_id}" AND w.uid = "{wished_ticket_id}"
            CREATE (o)-[:EXCHANGE_OFFER]->(w)
        '''
        try:
            db.cypher_query(query)
            response_data = {'message': 'Relationship created successfully'}
            return Response(response_data, status=status.HTTP_201_CREATED)
        except Exception as e:
            error_message = str(e)
            response_data = {'error': error_message}
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

# Class that returns the node IDs of all nodes in a cycle (if any)
class TicketCycle(APIView):
    @error_decorator
    def get(self, request):
        # uid = request.GET.get('uid', '')
        id = request.GET.get('id', '')
        # own_ticket = request.data['own_ticket']
        # wished_ticket = request.data['wished_ticket']

        # create arc between own_ticket and wished_ticket

        # check if there are circles after the arc creation
        # query = f'''
        #     MATCH n=(t:Ticket)-[*1..10]->(t)
        #     WHERE ID(t) = {id}
        #     RETURN n
        # '''

        query = f'''
            MATCH n=(t:Ticket)-[*1..10]->(t)
            WHERE t.uid = "{id}"
            RETURN n
        '''
        
        # Execute the query
        results, _ = db.cypher_query(query)

        nodes_for_cycle = {}
        # lookup for cicles
        for idx,cycle in enumerate(results):
            # For each cycle, return the nodes if each cycle
            list_node_c = []
            for node_c in cycle[0]:
                list_node_c.append(node_c.id)
            nodes_for_cycle[idx]=list_node_c
        
        return Response(nodes_for_cycle)
    

# create fake cycle data
class TicketFakeCycle(APIView):
    @error_decorator
    def post(self, request):
        ticket_uid = request.data['ticket_uid']
        cycle_length = request.data['cycle_length']
        
        # create a cycle of at least `cycle_length` that `ticket_uid` is involved in 
        
        # get ticket node with uid = ticket_uid
        target_ticket = Ticket.nodes.get(uid=ticket_uid)
        
        # get random tickets (until `cycle_length`) that are not the target ticket
        tickets = [ticket for ticket in Ticket.nodes.exclude(uid=ticket_uid).all()]
        random_tickets = random.sample(tickets, cycle_length-1)
        
        # create a cycle of relationships
        for idx, ticket in enumerate(random_tickets):
            if idx == 0:
                target_ticket.interests.connect(ticket)
            else:
                random_tickets[idx-1].interests.connect(ticket)
                
        # connect last ticket to target ticket
        random_tickets[-1].interests.connect(target_ticket)
         
        return Response({'message': 'Cycle created successfully'})

# create fake cycle data in which only one ticket is needed to complete the cycle. Return that ticket
class OneLeftTicketFakeCycle(APIView):
    @error_decorator
    def post(self, request):
        cycle_length = request.data['cycle_length']
        seed = request.data.get('seed', 0)
        ticket_type = request.data.get('ticket_type', None)
        
        # set random seed
        random.seed(seed)
         
        # get random tickets (until `cycle_length`)
        tickets = [ticket for ticket in Ticket.nodes.all()]
        
        # filter by ticket type, if provided
        if ticket_type:
            tickets = [ticket for ticket in tickets if ticket.type == ticket_type]
        
        random_tickets = random.sample(tickets, cycle_length)
        
        # create a cycle of relationships
        for idx, ticket in enumerate(random_tickets):
            if idx == 0:
                pass
            else:
                random_tickets[idx-1].interests.connect(ticket)
                
        # connect last ticket to first ticket
        random_tickets[-1].interests.connect(random_tickets[0])
        
        # return the ticket hat is left to complete the cycle and the ticket it should be connected to
        return Response({
            'ticket_uid': random_tickets[0].uid,
            'ticket_name': random_tickets[0].name,
            'target_ticket_uid': random_tickets[-1].uid,
            'target_ticket_name': random_tickets[-1].name,
        })
    
         
        
             
         