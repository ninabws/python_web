from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request, "hello/index.html")

def maryane(request):
	return HttpResponse("Hello, Maryane")

def nina(resquest):
	return HttpResponse("Hello, Nina")


def greet(request, name):
	return render(request, "hello/index.html",{
                "name": name.capitalize()
    })


