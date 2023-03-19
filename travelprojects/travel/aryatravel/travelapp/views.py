from django.shortcuts import render
from .models import Destination
from .models import Persons
# Create your views here.

def demo(request):
    obj=Destination.objects.all()
    j=Persons.objects.all()
    return render(request,"index.html",{'result':obj,'context':j})

##def demo1(request):
    #j=Persons.objects.all()
    #return render(request,"index.html",{'context':j})