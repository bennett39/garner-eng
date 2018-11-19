from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Project, Client, Site, Report, Contractor

# Create your views here.
def index(request):
    """
    Lists Projects alongside their respective Clients
    """
    context = {
        'projects': Project.objects.order_by('status', '-phase')
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
            'projects': client.projects.order_by('status'),
            'people': client.people.order_by('role')
    }

    return render(request, "sitereport/client.html", context) 


def clients(request):
    """
    Displays all clients.
    """
    context = {
            'clients': Client.objects.order_by('name')
    }

    return render(request, "sitereport/clients.html", context)


def contractor(request, contractor_id):
    """
    Display contractor that matches the passed in contractor_id
    """
    try:
        contractor = Contractor.objects.get(pk=contractor_id)
    except ContractorNotFound:
        raise Http404("Contractor not found.")

    context = {
            'contractor': contractor,
            'projects':
            contractor.contractor_projects.order_by('status'),
            'people': contractor.people.order_by('role')
    }

    return render(request, "sitereport/contractor.html", context)


def contractors(request):
    """
    Display a list of all contractors
    """
    context = {
            'contractors': Contractor.objects.order_by('name')
    }

    return render(request, "sitereport/contractors.html", context)


def project(request, project_id):
    """
    Displays Project information based on a passed-in project_id
    """
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404("Project does not exist.")

    context = {
            'project': project,
            'client': project.client,
            'sites': project.sites.order_by('-date_start')
    }

    return render(request, "sitereport/project.html", context) 


def projects(request):
    """
    List all projects alphabetically.
    """
    context = {
        'projects': Project.objects.order_by('name')
    }

    return render(request, "sitereport/projects.html", context)


def report(request, report_id):
    """
    Lookup a report via the report_id and display it
    """
    try:
        report = Report.objects.get(pk=report_id)
    except Report.DoesNotExist:
        raise Http404("Report does not exist.")

    context = {
            'report': report,
    }

    return render(request, "sitereport/report.html", context)


def site(request, site_id):
    try:
        site = Site.objects.get(pk=site_id)
    except Site.DoesNotExist:
        raise Http404("Site does not exist.")

    context = {
            'site': site,
            'reports': site.site_reports.order_by('date')
    }

    return render(request, "sitereport/site.html", context)

