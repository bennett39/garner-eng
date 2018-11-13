from django.urls import path

from . import views

# URL paths:
urlpatterns = [
    path('', views.index, name='index'),
    path('client/<int:client_id>', views.client, name='client'),
    path('project/<int:project_id>', views.project, name='project'),
    path('site/<int:site_id>', views.site, name='site'),
]
