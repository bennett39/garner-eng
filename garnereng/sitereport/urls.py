from django.urls import path

from . import views

# URL paths:
urlpatterns = [
    path('', views.index, name='index'), 
    path('client/<int:client_id>', views.client, name='client'),
    path('clients/', views.clients, name='clients'),
    path('project/<int:project_id>', views.project, name='project'),
    path('projects/', views.projects, name='projects'),
    path('site/<int:site_id>', views.site, name='site'),
]
