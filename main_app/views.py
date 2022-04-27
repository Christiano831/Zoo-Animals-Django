import re
from django.shortcuts import render, redirect
from .forms import MedicationForm
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
  medication_form = MedicationForm()
  return render(request, 'animals/info.html', {
    'animal': animal, 
    'medication_form': medication_form
  })

def add_medication(request, animal_id):
  form = MedicationForm(request.POST)
  if form.is_valid():
    new_medication = form.save(commit=False)
    new_medication.animal_id = animal_id
    new_medication.save()
  return redirect('info', animal_id=animal_id)

class AnimalUpdate(UpdateView):
  model = Animal
  fields = ['name', 'species', 'gender', 'age']

class AnimalDelete(DeleteView):
  model = Animal
  success_url = '/animals/'