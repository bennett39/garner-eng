from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Project, Client

# Create your views here.
def index(request):
    context = {
        'projects': Project.objects.all()
    }
    return render(request, "sitereport/index.html", context)

def client(request, client_id):
    try:
        client = Client.objects.get(pk=client_id)
    except Client.DoesNotExist:
        raise Http404("Client does not exist.")

    context = {
        'client' : client
    }

    return render(request, "sitereport/client.html", context) 

def project(request, project_id):
    return HttpResponse("Project index")
