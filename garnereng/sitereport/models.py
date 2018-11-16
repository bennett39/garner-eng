from django.db import models
import time
from datetime import date

# Create your models here.
class UsState(models.Model):
    """
    Create a table for US States so that Clients, Contractors, and 
    Projects are searchable by state.
    """
    state = models.CharField(max_length=64)
    symbol = models.CharField(max_length=2)

    def __str__(self):
        return self.state


class Person(models.Model):
    """
    Create a table of individual Persons that can be affiliated with
    Projects, Clients, and Contractors.
    """
    first = models.CharField(max_length=128)
    last = models.CharField(max_length=128)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone = models.CharField(max_length=16, null=True, blank=True)

    def __str__(self):
        return f"{self.first} {self.last}"


class Client(models.Model):
    """
    Create a table of Clients (companies) that are associated with 
    Projects
    """
    name = models.CharField('company/client name', max_length=254)
    address = models.CharField(max_length=254, null=True, blank=True)
    city = models.CharField(max_length=64, null=True, blank=True)
    state = models.ForeignKey(UsState, on_delete=models.CASCADE,
            null=True, blank=True, related_name='state_clients')
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    decider = models.ForeignKey(Person, on_delete=models.CASCADE, 
            null=True, blank=True, related_name='decision_maker')
    lead = models.ForeignKey(Person, on_delete=models.CASCADE,
            null=True, blank=True, related_name='project_lead')
    referral = models.CharField('referral source', max_length=254, 
            null=True, blank=True)

    def __str__(self):
        return self.name


class Contractor(models.Model):
    """
    Create a table of Contractors that are associated with Projects.
    """
    name = models.CharField('company/client name', max_length=254)
    address = models.CharField(max_length=254, null=True, blank=True)
    city = models.CharField(max_length=64, null=True, blank=True)
    state = models.ForeignKey(UsState, on_delete=models.CASCADE,
            null=True, blank=True, related_name='state_contractors')
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    contact = models.ForeignKey(Person, on_delete=models.CASCADE,
            null=True, blank=True, related_name='contact')

    def __str__(self):
        return self.name


class Phase(models.Model):
    """
    Create a table of Project Phases (e.g. "Design", "Proposal", or
    "Construction"). Projects searchable/sortable by Phase.
    """
    label = models.CharField(max_length=64)

    def __str__(self):
        return self.label


class Status(models.Model):
    """
    Create a table of current Project Statuses (e.g. "Active",
    "Standby", or "Complete"). Projects searchable/sortable by Status.
    """
    label = models.CharField(max_length=64)

    def __str__(self):
        return self.label


class DamType(models.Model):
    """
    Create a table of Project DamTypes (e.g. "Earth/Embankment",
    "Gravity", "Arch"). Searchable/sortable by DamType.
    
    If Project.is_dam == False, then DamType should be None.
    """
    label = models.CharField(max_length=64)

    def __str__(self):
        return self.label


class SpillwayType(models.Model):
    """
    Create a table of SpillwayTypes (e.g. "Riser", "Overflow",
    "Labrynth"). Searchable/sortable by SpillwayType.

    If Project.is_dam == False, then SpillwayType should be None.
    """
    label = models.CharField(max_length=64)

    def __str__(self):
        return self.label


class TestType(models.Model):
    """
    Crate a table of TestTypes performed on a field visit to a Site
    (e.g. "Structural Steel", "Concrete", "Proofroll"). Reports
    searchable/sortable by TestType.
    """
    label = models.CharField(max_length=64)

    def __str__(self):
        return self.label


class Project(models.Model):
    """
    Create a table of Projects. Projects is the core model of this app.

    Related models:
        - Client
        - Contractor
        - Phase
        - Status
        - DamType
        - SpillwayType
        - Site (via 'sites' related_name)
    
    TODO: Add logic to the is_dam boolean field that sets remaining
    fields to None/Null when is_dam==False. 
    
    For now, leave fields empty when is_dam==False
    """

    name = models.CharField('project name', max_length=254)
    client = models.ForeignKey(Client, on_delete=models.CASCADE,
            related_name='projects')
    number = models.CharField('job number', max_length=16, unique=True,
            blank=True, null=True)
    started = models.DateField(null=True, blank=True)
    budget = models.FloatField(null=True, blank=True)
    billed = models.FloatField(null=True, blank=True)
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE,
            blank=True, null=True, related_name='contractor')
    construction_cost = models.FloatField(null=True, blank=True)
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE, 
            blank=True, null=True, related_name='phase')
    status = models.ForeignKey(Status, on_delete=models.CASCADE,
            blank=True, null=True, related_name='status')
    is_dam = models.BooleanField('is it a dam?', null=True)
    dam_type = models.ForeignKey(DamType, on_delete=models.CASCADE, 
            blank=True, null=True, related_name='dam_type')
    height = models.FloatField(null=True, blank=True)
    width = models.FloatField(null=True, blank=True)
    watershed = models.FloatField(null=True, blank=True)
    spillway_type = models.ForeignKey(SpillwayType, 
            on_delete=models.CASCADE, blank=True, null=True, 
            related_name='spillway_type')
    details = models.TextField(null=True, blank=True)
    flood_volume = models.FloatField(null=True, blank=True)
    total_volume = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name


class Site(models.Model):
    """
    Create a table of construction Sites affiliated with a given
    Project.
    """
    name = models.CharField(max_length=127, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
            default=None, related_name='sites')
    street = models.CharField(max_length=254)
    city = models.CharField(max_length=64)
    state = models.ForeignKey(UsState, on_delete=models.CASCADE,
            related_name='state_sites')
    zip_code = models.CharField(max_length=10)
    date_start = models.DateField('date started', default=None,
            null=True, blank=True)
    date_end = models.DateField('date ended', default=None, null=True,
            blank=True)

    def __str__(self):
        return f"{self.name}"


class Report(models.Model):
    """
    Create a table of daily field Reports affiliated with a given Site 
    (Sites are further affiliated with a given Project).
    """
    date = models.DateField(null=True, default=None)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, 
            related_name='site_reports')
    mileage = models.FloatField(null=True, blank=True)
    travel_time = models.FloatField(null=True, blank=True)
    site_time = models.FloatField(null=True, blank=True)
    temperature = models.IntegerField(null=True, blank=True)
    weather = models.CharField(max_length=64)
    conditions = models.CharField('site conditions', max_length=128)
    description = models.TextField('work description', null=True, 
            blank=True)
    tests = models.ManyToManyField(TestType, blank=True)
    photos = models.TextField('Drive/Dropbox link to photos', null=True,
            blank=True)

    def __str__(self):
        return self.date.strftime("%Y-%m-%d")

