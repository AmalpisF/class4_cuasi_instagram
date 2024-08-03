from django.shortcuts import render
from django.views.generic import ListView
from publicaciones.models import tabla1

# Create your views here.

class HomePageView(ListView):

    model = tabla1
    template_name = "home.html"