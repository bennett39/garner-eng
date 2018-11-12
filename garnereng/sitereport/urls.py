from django.urls import path

from . import views

# URL paths:
urlpatterns = [
    path('', views.index, name='index'),
    path('client/', views.client, name='client'),
    path('project/', views.project, name='project'),
]
