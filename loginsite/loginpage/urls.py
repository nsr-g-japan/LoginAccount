from django.urls import  path
from .views import *

urlpatterns=[
    path('homepage',homepage, name='homepage'),

    path('landingpage', landingpage),
    path('home', home, name='signin'),

]