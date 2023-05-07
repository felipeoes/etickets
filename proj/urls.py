from django.contrib import admin
from django.urls import path

from etickets.views.user import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/list/', UserList.as_view()),
    path('users/<str:email>/', UserDetail.as_view()),

]
