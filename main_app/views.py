import re
from django.shortcuts import render

from .models import Animal

from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

class AnimalCreate(CreateView):
  model = Animal
  fields = '__all__'
  success_url = '/animals/'

def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def animals_index(request):
  animals = Animal.objects.all()
  return render(request, 'animals/index.html', { 'animals': animals })

def info(request, animal_id):
  animal = Animal.objects.get(id=animal_id)
  return render(request, 'animals/info.html', {'animal': animal})

class AnimalUpdate(UpdateView):
  model = Animal
  fields = ['name', 'species', 'gender', 'age']

class AnimalDelete(DeleteView):
  model = Animal
  success_url = '/animals/'