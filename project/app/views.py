from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .models import Student


# Create your views here.
def register(request):
    return render(request,'register.html')


def registerdata(request):
    print (request.method)
    print (request.POST)
    var1 = request.POST.get('name')
    var2 = request.POST.get('email')
    var3 = request.POST.get('contact')
    Student.objects.create(Name=var1,Email=var2,Contact=var3)
    print("Data save successfully")