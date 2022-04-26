import re
from django.shortcuts import render

from .models import Animal

# Create your views here.

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