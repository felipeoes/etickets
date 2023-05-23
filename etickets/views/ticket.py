from rest_framework.response import Response
from rest_framework.views import APIView

from etickets.models import Ticket
from etickets.utils import error_decorator


# retrieve all ticket nodes
class TicketsList(APIView):
    @error_decorator
    def get(self, request):
        tickets = [user.to_dict() for user in Ticket.nodes.all()]
        return Response(tickets)

# Tickets search by name, event or location


class TicketsSearch(APIView):
    @error_decorator
    def get(self, request, name, event, location):
        tickets = [user.to_dict() for user in Ticket.nodes.all()]

        fields_map = {
            'name': name,
            'event': event,
            'location': location,
        }

        for ticket in tickets:
            for field, value in fields_map.items():
                if value and value.lower() not in ticket[field].lower():
                    tickets.remove(ticket)
                    break

        return Response(tickets)


# class for Ticket CRUD operations
class TicketDetail(APIView):
    @error_decorator
    def get(self, request, uid):
        ticket = Ticket.nodes.get(uid=uid)
        return Response(ticket.to_dict())

    @error_decorator
    def post(self, request):
        ticket = Ticket(**request.data)
        ticket.save()
        return Response(ticket.to_dict())

    @error_decorator
    def put(self, request, uid):
        ticket = Ticket.nodes.get(uid=uid)
        ticket.__dict__.update(request.data)
        ticket.save()
        return Response(ticket.to_dict())

    @error_decorator
    def delete(self, request, uid):
        ticket = Ticket.nodes.get(uid=uid)
        ticket.delete()
        return Response(ticket.to_dict())
