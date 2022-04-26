import re
from django.shortcuts import render

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def animals_index(request):
  return render(request, 'animals/index.html', { 'animals': animals })

class Animal:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, species, gender, age):
    self.name = name
    self.species = species
    self.gender = gender
    self.age = age

animals = [
  Animal('Kevin', 'rhino', 'male', 8),
  Animal('Jasmine', 'zebra', 'female', 10),
  Animal('Levi', 'monkey', 'male', 23)
]