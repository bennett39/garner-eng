from django.shortcuts import render
from django.http import HttpResponse

from .models import Project

# Create your views here.
def index(request):
    context = {
        'projects': Project.objects.all()
    }
    return render(request, "sitereport/index.html", context)

def client(request):
    return HttpResponse("Client index")

def project(request):
    return HttpResponse("Project index")
