from django.db import models

# Create your models here.
class UsState(models.Model):
    state = models.CharField(max_length=254)
    symbol = models.CharField(max_length=2)

    def __str__(self):
        return self.state

class Client(models.Model):
    name = models.CharField('company/client name', max_length=254)
    address = models.CharField(max_length=254, null=True, blank=True)
    city = models.CharField(max_length=64, null=True, blank=True)
    state = models.ForeignKey(UsState, on_delete=models.CASCADE,
            null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name

class Person(models.Model):
    first = models.CharField(max_length=128)
    last = models.CharField(max_length=128)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone = models.CharField(max_length=16, null=True, blank=True)
    company = models.ManyToManyField(Client)

    def __str__(self):
        return f"{self.first} {self.last}"

class Project(models.Model):
    name = models.CharField('project name', max_length=254)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=127, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
            default=None)
    street = models.CharField(max_length=254)
    city = models.CharField(max_length=64)
    state = models.ForeignKey(UsState, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=10)
    date_start = models.DateField('date started', default=None,
            null=True, blank=True)
    date_end = models.DateField('date ended', default=None, null=True,
            blank=True)

    def __str__(self):
        return f"{self.name}"
