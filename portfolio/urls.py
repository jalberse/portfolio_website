from django.urls import path

from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('code/resume', views.resume, name = 'resume'),
    path('code/projects', views.projects, name= 'projects'),
    path('art-<slug:slug>', views.gallery, name = 'gallery'),
]