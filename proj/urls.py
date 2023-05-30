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

    # TICKETS
    path('tickets/list/', TicketsList.as_view()),
    path('tickets/', TicketDetail.as_view()),
    path('tickets-locations/', TicketsLocations.as_view()),
    path('tickets-search/', TicketsSearch.as_view()),


]

create_fake_data()
