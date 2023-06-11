from rest_framework.response import Response
from rest_framework.views import APIView

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
        query = f'''
        MATCH n=(t:Ticket)-[*1..6]->(t)
        WHERE ID(t) = {id}
        RETURN n
        '''

        # Execute the query
        results, meta = db.cypher_query(query)

        nodes_for_cycle = {}
        # lookup for cicles
        for idx,cycle in enumerate(results):
            # For each cycle, return the nodes if each cycle
            list_node_c = []
            for node_c in cycle[0]:
                list_node_c.append(node_c.id)
            nodes_for_cycle[idx]=list_node_c
        
        return Response(nodes_for_cycle)