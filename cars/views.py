from django.shortcuts import render

# Create your views here.

from django.views.generic import *
from .models import Car
from .forms import CarForm

class CarListView(ListView):
    template_name="cars.html"
    queryset=Car.objects.all()

class CarDetailView(DetailView):
    template_name="car.html"
    queryset=Car.objects.all()

class CarCreateView(CreateView):
    template_name="add_car.html"
    queryset=Car.objects.all()
    form_class=CarForm

class CarUpdateView(UpdateView):
    template_name="update_car.html"
    queryset=Car.objects.all()
    fields=["title","make","model","price"]