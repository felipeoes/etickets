import random

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from etickets.models import Ticket, User
from etickets.utils import error_decorator
from datetime import datetime
from neomodel import db
from node2vec import Node2Vec
import networkx as nx
from sklearn.ensemble import RandomForestClassifier
from gensim.models import Word2Vec
import pickle
from django.conf import settings
import os
import numpy as np
import random
import traceback

from create_fake_data import create_fake_data, create_fake_data_2

random.seed(1)

# retrieve all ticket nodes
class TicketsList(APIView):
    @error_decorator
    def get(self, request):
        tickets = [user.to_dict() for user in Ticket.nodes.all()]
        return Response(tickets)

class UserTickets(APIView):
    @error_decorator
    def get(self, request):
        user_email = request.GET.get('email', '')
        user = User.nodes.get_or_none(email=user_email)
        if user is None:
            raise Exception('User not found')
        
        tickets = [ticket.to_dict() for ticket in user.tickets.all()]
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
                  ('event', request.GET.get('event', '')),
                  ('type', request.GET.get('type', '')),
                  ]
        
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

class TicketExchange(APIView):
    @error_decorator
    def post(self, request):
        own_user_email = request.data.get('own_user_email', '')
        wished_ticket_user_email = request.data.get('wished_ticket_user_email', '')

        own_ticket_id = request.data.get('own_ticket_id', '')
        wished_ticket_id = request.data.get('wished_ticket_id', '')

        own_ticket = Ticket.nodes.get(uid=own_ticket_id)
        own_ticket_user = User.nodes.get(email=own_user_email)
        
        if not own_ticket or not own_ticket_user:
            raise Exception('Own ticket or user not found')
        
        wished_ticket = Ticket.nodes.get(uid=wished_ticket_id)
        wished_ticket_user = User.nodes.get(email=wished_ticket_user_email)
        
        if not wished_ticket or not wished_ticket_user:
            raise Exception('Wished ticket or user not found')
        
        # exchange tickets
        # if not own_ticket_user.tickets.is_connected(own_ticket):
        #     raise Exception('Own ticket not found')
        
        # if not wished_ticket_user.tickets.is_connected(wished_ticket):
        #     raise Exception('Wished ticket not found')
        own_ticket_user.tickets.disconnect(own_ticket)
        wished_ticket_user.tickets.disconnect(wished_ticket)
        
        own_ticket_user.tickets.connect(wished_ticket)
        wished_ticket_user.tickets.connect(own_ticket)
        
        own_ticket_user.save()
        wished_ticket_user.save()
        
        response_data = {'message': 'Tickets exchanged successfully'}
        return Response(response_data, status=status.HTTP_201_CREATED)
     
        

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

class TicketPredictionEXCHANGE_OFFER(APIView):
    @error_decorator
    def get(self, request):        
        ticket_uid = request.GET.get('ticket_uid', '')

        # load the model embedding
        file_path = os.path.join(settings.BASE_DIR, 'embedding_model.model')
        model = Word2Vec.load(file_path)

        # load the random forest model
        file_path = os.path.join(settings.BASE_DIR, "ml_model.pkl")
        with open(file_path, 'rb') as file:
            rf_classifier = pickle.load(file)        

        query = """
        MATCH (t1:Ticket),(t2:Ticket)
        WHERE NOT EXISTS((t1)-[:EXCHANGE_OFFER]-(t2)) and t1.name < t2.name and t1.uid = "{}"
        RETURN t1,t2
        """.format(ticket_uid)

        # Execute the query
        results_without_EXCHANGE_OFFER_top10, _ = db.cypher_query(query)

        if len(results_without_EXCHANGE_OFFER_top10)==0:
            error_message = 'Query return null'
            response_data = {'error': error_message}
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)        

        negative_edges_new = np.array([np.concatenate([model.wv[dict(result[0])['uid']],model.wv[dict(result[1])['uid']]]) for idx, result in enumerate(results_without_EXCHANGE_OFFER_top10)])

        # rf_classifier
        predictions_proba = rf_classifier.predict_proba(negative_edges_new)
        # Return the sorted nodes in terms of probability to have a EXCHANGE_OFFER

        top10_tickets = np.array([dict(result[1]) for result in results_without_EXCHANGE_OFFER_top10])[np.lexsort(predictions_proba.T[::-1])][:10]
        return Response(top10_tickets)

class ModelTrain(APIView):
    @error_decorator
    def post(self, request):
        # Generate the node embeddings and train the model
        query = """
        MATCH (t1:Ticket)
        RETURN t1
        """

        # Execute the query
        results_ticket, _ = db.cypher_query(query)

        query = """
        MATCH (t1:User)
        RETURN t1
        """

        # Execute the query
        results_user, _ = db.cypher_query(query)

        query = """
        MATCH n=(u1:User)-[]-(t1:Ticket)
        RETURN n
        """

        # Execute the query
        results_user_ticket, _ = db.cypher_query(query)

        query = """
        MATCH n=(t1:Ticket)-[]-(t2:Ticket)
        WHERE t1.name < t2.name
        RETURN n
        """

        # Execute the query
        results_ticket_ticket, _ = db.cypher_query(query)

        query = """
        MATCH n=(t1:Ticket)-[:EXCHANGE_OFFER]-(t2:Ticket)
        WHERE t1.name < t2.name
        RETURN n
        """

        # Execute the query
        results_ticket_ticket_EXCHANGE_OFFER, _ = db.cypher_query(query)

        query = """
        MATCH (t1:Ticket),(t2:Ticket)
        WHERE NOT EXISTS((t1)-[:EXCHANGE_OFFER]->(t2)) and t1.name < t2.name
        RETURN t1,t2
        """

        # Execute the query
        results_without_EXCHANGE_OFFER, _ = db.cypher_query(query)
        g_nx = nx.Graph()
        g_nx.add_nodes_from([(result[0]['uid'],{a:b for a,b in dict(result[0]).items() if a!='uid'}) for idx, result in enumerate(results_ticket)])
        g_nx.add_nodes_from([(result[0]['uid'],{a:b for a,b in dict(result[0]).items() if a not in ['uid','name','cpf','phone','email']}) for idx, result in enumerate(results_user)])
        g_nx.add_edges_from([(dict(result[0].start_node)['uid'],dict(result[0].end_node)['uid']) for idx, result in enumerate(results_user_ticket)])
        g_nx.add_edges_from([(dict(result[0].start_node)['uid'],dict(result[0].end_node)['uid'],result[0].relationships[0]._properties) for idx, result in enumerate(results_ticket_ticket)])

        node2vec = Node2Vec(g_nx, dimensions=64, walk_length=30, num_walks=10, workers=10)
        model = node2vec.fit(window=10, min_count=1, batch_words=4) 
        # Save model for later use
        
        file_path = os.path.join(settings.BASE_DIR, 'embedding_model.model')
        model.save(file_path)

        # Criar combinacoes de pares de nos e se há ou não uma relação de EXCHANGE_OFFER
        positive_edges = np.array([[np.concatenate([model.wv[dict(result[0].start_node)['uid']],model.wv[dict(result[0].end_node)['uid']]]),'1'] for idx, result in enumerate(results_ticket_ticket_EXCHANGE_OFFER)])
        negative_edges = [[np.concatenate([model.wv[dict(result[0])['uid']],model.wv[dict(result[1])['uid']]]),'0'] for idx, result in enumerate(results_without_EXCHANGE_OFFER)]
        # # downsampling - criar um conjunto balanceado de EXCHANGE_OFFER sim e nao

        negative_edges = random.sample(negative_edges,len(positive_edges))

        dataset = np.random.permutation(np.concatenate([positive_edges,negative_edges]))
        y = dataset[:,1]
        X = np.squeeze(dataset[:,:1])
        X = np.array([x for x in X])
        # Create a Random Forest classifier
        rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

        # Train the classifier using the training data
        rf_classifier.fit(X, y)

        # Make predictions on the test data
        # y_pred = rf_classifier.predict(X_test)
        # y_pred_proba = rf_classifier.predict_proba(X_test)

        # Save the model under the cwd
        file_path = os.path.join(settings.BASE_DIR, "ml_model.pkl")
        with open(file_path, 'wb') as file:
            pickle.dump(rf_classifier, file)

        response_data = {'message': 'Machine Learning trained and saved successfully'}
        return Response(response_data, status=status.HTTP_201_CREATED)


class Top10TicketsForMe(APIView):
    @error_decorator
    def get(self, request): 
        try:
            email = request.GET.get('email', '')
            # load the model embedding
            file_path = os.path.join(settings.BASE_DIR, 'embedding_model.model')
            model = Word2Vec.load(file_path)

            # load the random forest model
            file_path = os.path.join(settings.BASE_DIR, "ml_model.pkl")
            with open(file_path, 'rb') as file:
                rf_classifier = pickle.load(file)        

            query = """
            MATCH (u1:User)-[:HAS_TICKET]-(t1:Ticket),(u2:User)-[:HAS_TICKET]-(t2:Ticket)
            WHERE NOT EXISTS((t1)-[:EXCHANGE_OFFER]-(t2)) and t1.name < t2.name and u1.name < u2.name and u1.email ="{}"
            RETURN t1,t2
            """.format(email)

            # Execute the query
            results_without_EXCHANGE_OFFER_top10, _ = db.cypher_query(query)

            if len(results_without_EXCHANGE_OFFER_top10)==0:
                error_message = 'Query return null'
                response_data = {'error': error_message}
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

            negative_edges_new = np.array([np.concatenate([model.wv[dict(result[0])['uid']],model.wv[dict(result[1])['uid']]]) for idx, result in enumerate(results_without_EXCHANGE_OFFER_top10)])            

            predictions_proba = rf_classifier.predict_proba(negative_edges_new)
            # Return the sorted nodes in terms of probability to have a EXCHANGE_OFFER

            top10_tickets = np.array([dict(result[1]) for result in results_without_EXCHANGE_OFFER_top10])[np.lexsort(predictions_proba.T[::-1])][:10]
            my_tickets = np.array([dict(result[0]) for result in results_without_EXCHANGE_OFFER_top10])[np.lexsort(predictions_proba.T[::-1])][:10]
            my_tickets_uid = [ticket['uid'] for ticket in my_tickets]
            for idx,ticket in enumerate(top10_tickets):
                ticket['my_ticket_id']=my_tickets_uid[idx]
            
            top10_tickets = {'ticket':top10_tickets}
            return Response(top10_tickets)
        except Exception as e:
            error_message = str(e)
            response_data = {'error': error_message}
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class CreateFakeData(APIView):
    @error_decorator
    def post(self, request):
        create_fake_data()
        # create_fake_data_2()
        try:
            response_data = {'message': 'Relationship created successfully'}
            return Response(response_data, status=status.HTTP_201_CREATED)
        except Exception as e:
            error_message = str(e)
            response_data = {'error': error_message}
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
    

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
        random_users  = random.sample(User.nodes.all(), cycle_length)
        
        # create a cycle of relationships
        for idx, ticket in enumerate(random_tickets):
            if idx == 0:
                pass
            else:
                # add user to ticket
                random_users[idx-1].tickets.connect(ticket)
                
                # add interest relationship
                random_tickets[idx-1].interests.connect(ticket)
                
        # connect last ticket to first ticket
        random_users[-1].tickets.connect(random_tickets[0])
        random_tickets[-1].interests.connect(random_tickets[0])
        
        
        # return the ticket hat is left to complete the cycle and the ticket it should be connected to, as well as its respective users
        return Response({
            'ticket_uid': random_tickets[0].uid,
            'ticket_name': random_tickets[0].name,
            'ticker_user_email': random_users[0].email,
            'target_ticket_uid': random_tickets[-1].uid,
            'target_ticket_name': random_tickets[-1].name,
            'target_ticket_user_email': random_users[-1].email,
        })
    