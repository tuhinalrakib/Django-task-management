from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # work with database connection
    # Transform data
    # data pass 
    # HTTP response / json response
    return HttpResponse("Welcome to our website")

def contact(request):
    return HttpResponse("This is contact page")

def show_task(request):
    return HttpResponse("<h1>This is Task page<h1/>")

def show_specific_task(request, id):
    print("id", id)
    print("ID Type", type(id))
    return HttpResponse(f"<h1>This is specific task Page {id}<h1/>")