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