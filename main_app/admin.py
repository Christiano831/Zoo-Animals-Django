from django.contrib import admin

# Register your models here.
from .models import Animal, Medication

admin.site.register(Animal)
admin.site.register(Medication)