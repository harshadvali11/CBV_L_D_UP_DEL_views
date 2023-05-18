from django.shortcuts import render
from app.models import *
# Create your views here.
from django.views.generic import TemplateView,ListView

class Home(TemplateView):
    template_name='app/home.html'

class SchoolList(ListView):
    model = School
    context_object_name='schools'