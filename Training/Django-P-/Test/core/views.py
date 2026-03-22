from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_world(request):
    return HttpResponse("Hello, Kaka!")

def helloWorld(request):
    return render(request, "core/hello.html")