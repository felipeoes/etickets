from django.contrib import admin
from django.urls import path
from etickets.views.user import *
from etickets.views.ticket import *
from create_fake_data import create_fake_data

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # USERS
    path('users/list/', UsersList.as_view()),
    path('users/<str:email>/', UserDetail.as_view()),
    path('users-interests/', UserInterest.as_view()),
    path('user-tickets/', UserTickets.as_view()),

    # TICKETS
    path('tickets/list/', TicketsList.as_view()),
    path('tickets/', TicketDetail.as_view()),
    path('tickets-locations/', TicketsLocations.as_view()),
    path('tickets-search/', TicketsSearch.as_view()),
    path('tickets-cycles/', TicketCycle.as_view()),
    path('tickets-exchange/', TicketExchange.as_view()),
    path('tickets-exchange-offer/', TicketExchangeOffer.as_view()),
    path('tickets-train/', ModelTrain.as_view()),
    path('tickets-prediction/', TicketPredictionEXCHANGE_OFFER.as_view()),
    path('dashboard/for-me/', Top10TicketsForMe.as_view()),
    path('tickets-sintetic-data/', CreateFakeData.as_view()),


    path('tickets-fake-cycle/', TicketFakeCycle.as_view()),
    path('seed/build/', OneLeftTicketFakeCycle.as_view()),
]

# create_fake_data()
