
from django.urls import path 
from .views import registerdata
from .views import register

from app import views
urlpatterns = [
    path('register/' ,views.register),
    path('registerdata/' ,views.registerdata ,name='register')
    
]