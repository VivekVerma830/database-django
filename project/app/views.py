from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def register(request):
    return render(request,'registration.html')


def registrationdata(request):
    # return HttpResponse(request,'registrationdata')  #server to views data 
    print (request.method)
    print (request.POST)