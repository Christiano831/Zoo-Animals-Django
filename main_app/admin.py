from django.contrib import admin

# Register your models here.
from .models import Animal, Medication, Zookeeper

admin.site.register(Animal)
admin.site.register(Medication)
admin.site.register(Zookeeper)