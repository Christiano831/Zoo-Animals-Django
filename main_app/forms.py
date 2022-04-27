from django.forms import ModelForm
from .models import Animal, Medication

class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'species', 'gender', 'age', 'needs_meds']

class MedicationForm(ModelForm):
  class Meta:
    model = Medication
    fields = ['date', 'med']
