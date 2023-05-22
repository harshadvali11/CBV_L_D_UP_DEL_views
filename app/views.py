from django.shortcuts import render
from app.models import *
# Create your views here.
from django.views.generic import DeleteView,UpdateView,TemplateView,ListView,DetailView,CreateView
from django.urls import reverse_lazy
class Home(TemplateView):
    template_name='app/home.html'

class SchoolList(ListView):
    model = School
    context_object_name='schools'

class SchoolDetail(DetailView):
    model=School
    context_object_name='sclobject'

class SchoolCreate(CreateView):
    model=School
    fields='__all__'

class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'

class Schooldelete(DeleteView):
    model=School
    context_object_name='schoolobject'
    success_url=reverse_lazy('SchoolList')










