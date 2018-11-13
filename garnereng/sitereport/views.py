from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Project, Client, Site

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
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404("Project does not exist.")

    context = {
        'project': project,
        'client': project.client,
        'sites': project.sites.all()
    }

    return render(request, "sitereport/project.html", context) 
