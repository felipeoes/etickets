from rest_framework.response import Response
from rest_framework.views import APIView

from etickets.models import Ticket, User
from etickets.utils import error_decorator
from datetime import datetime

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
