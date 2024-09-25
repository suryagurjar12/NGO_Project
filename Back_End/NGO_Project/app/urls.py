from django.urls import path
from .views import *

urlpatterns = [
    path('',Registration,name='registration'),
    path('Admin',Admin,name='Admin')
]
