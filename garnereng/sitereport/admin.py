from django.contrib import admin

from .models import UsState, Client, Person, Project, Site

# Register your models here.
admin.site.register(UsState)
admin.site.register(Client)
admin.site.register(Person)
admin.site.register(Project)
admin.site.register(Site)
