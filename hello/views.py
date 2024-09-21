#views.py --> which templates should be selected/which information should be given to the templates
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
     return render(request, "hello\index.html")

def jan(request):
     return HttpResponse("Hello, Jan!")

def greet_html(request, name):
     return render(request, "hello\greet.html",{"name":name.capitalize()})