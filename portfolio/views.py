from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from django.urls import reverse
from django.views import generic

from .models import Gallery, ResumeItem, CodingProject, Media

def index(request):
    context = {}
    return render(request, 'portfolio/index.html', context)

def resume(request):
    item_list = ResumeItem.objects.order_by('start_date').reverse()
    context = {
        'item_list': item_list,
    }
    return render(request, 'portfolio/resume.html', context)

def projects(request):
    project_list = CodingProject.objects.all()
    context = {
        'project_list': project_list,
    }
    return render(request, 'portfolio/projects.html', context)

def gallery(request, slug):
    # Load gallery that will be displayed
    gallery = get_object_or_404(Gallery, slug=slug)
    # Load other galleries as well for navigation display
    gallery_list = Gallery.objects.all()
    context = {
        'gallery': gallery,
        'gallery_list': gallery_list,
    }
    return render(request, 'portfolio/gallery.html', context)