from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Project, Client, Site

# Create your views here.
def index(request):
    """
    Lists Projects alongside their respective Clients
    """
    context = {
            'projects': Project.objects.all()
    }
    return render(request, "sitereport/index.html", context)

def client(request, client_id):
    """
    Displays Client and Project information based on a passed-in 
    client_id
    """
    try:
        # Lookup Client via primary key (pk). More information:
        # https://docs.djangoproject.com/en/dev/ref/models/instances/#the-pk-property
        client = Client.objects.get(pk=client_id)
    except Client.DoesNotExist:
        # Basic error checking that client successfully retrieved
        raise Http404("Client does not exist.")

    context = {
            'client' : client,
            'projects': client.projects.all()
    }

    return render(request, "sitereport/client.html", context) 

def project(request, project_id):
    """
    Displays Project information based on a passed-in project_id
    """
    try:
        # Lookup Project via primary key (pk). More information:
        # https://docs.djangoproject.com/en/dev/ref/models/instances/#the-pk-property
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        # Error checking for project successfully retrieved
        raise Http404("Project does not exist.")

    context = {
            'project': project,
            'client': project.client,
            'sites': project.sites.all()
    }

    return render(request, "sitereport/project.html", context) 

def site(request, site_id):
    try:
        # Lookup Site via primary key (pk). More information:
        # https://docs.djangoproject.com/en/dev/ref/models/instances/#the-pk-property
        site = Site.objects.get(pk=site_id)
    except Site.DoesNotExist:
        #  Error checking if site exists
        raise Http404("Site does not exist.")

    context = {
            'site': site
    }

    return render(request, "sitereport/site.html", context)

