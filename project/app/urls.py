
from django.urls import path
from .views import *


urlpatterns = [
    path("registration/" ,register),
    path("registrationdata/" ,registrationdata ,name='register'),
    
]