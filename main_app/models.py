from django.db import models
from django.urls import reverse

# Create your models here.
class Animal(models.Model):
	name = models.CharField(max_length=100)
	species = models.CharField(max_length=100)
	gender = models.CharField(max_length=250)
	age = models.IntegerField()

def __str__(self):
        return self.name

def get_absolute_url(self):
	return reverse('info', kwargs={'animal_id': self.id})

