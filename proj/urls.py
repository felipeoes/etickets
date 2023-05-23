from django.contrib import admin
from django.urls import path

from etickets.views.user import *
from etickets.views.ticket import *
from create_fake_data import create_fake_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/list/', UsersList.as_view()),
    path('users/<str:email>/', UserDetail.as_view()),

    # TICKETS
    path('tickets/list/', TicketsList.as_view()),
    path('tickets/<str:uid>/', TicketDetail.as_view()),
    path('search/tickets/<str:name>/<str:event>/<str:location>/',
         TicketsSearch.as_view()),

]

create_fake_data()
