from django.db import models

# Create your models here.
class UsState(models.Model):
    state = models.CharField(max_length=64)
    symbol = models.CharField(max_length=2)

    def __str__(self):
        return self.state


class Person(models.Model):
    first = models.CharField(max_length=128)
    last = models.CharField(max_length=128)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone = models.CharField(max_length=16, null=True, blank=True)

    def __str__(self):
        return f"{self.first} {self.last}"


class Client(models.Model):
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
    label = models.CharField(max_length=64)

    def __str__(self):
        return self.label


class Status(models.Model):
    label = models.CharField(max_length=64)

    def __str__(self):
        return self.label


class DamType(models.Model):
    label = models.CharField(max_length=64)

    def __str__(self):
        return self.label


class SpillwayType(models.Model):
    label = models.CharField(max_length=64)

    def __str__(self):
        return self.label


class Project(models.Model):
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
