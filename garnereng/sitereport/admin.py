from django.contrib import admin

from .models import (UsState, Client, Person, Project, Site, Contractor,
Status, Phase, DamType, SpillwayType, TestType, Report)

# Register your models here.
admin.site.register(UsState)
admin.site.register(Client)
admin.site.register(Person)
admin.site.register(Project)
admin.site.register(Site)
admin.site.register(Contractor)
admin.site.register(Phase)
admin.site.register(Status)
admin.site.register(DamType)
admin.site.register(SpillwayType)
admin.site.register(TestType)
admin.site.register(Report)
