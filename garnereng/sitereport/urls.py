from django.urls import path

from . import views

# URL paths:
urlpatterns = [
    path('', views.index, name='index'), 
    path('client/<int:client_id>', views.client, name='client'),
    path('clients/', views.clients, name='clients'),
    path('contractor/<int:contractor_id>', views.contractor,
        name='contractor'),
    path('contractors', views.contractors, name='contractors'),
    path('project/<int:project_id>', views.project, name='project'),
    path('projects/', views.projects, name='projects'),
    path('report/<int:report_id>', views.report, name='report'),
    path('site/<int:site_id>', views.site, name='site'),
]
