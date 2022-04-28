from django.db import models
from django.urls import reverse

# Create your models here.
class Zookeeper(models.Model):
	name = models.CharField(max_length=50)
	position = models.CharField(max_length=50)
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('zookeeper_info', kwargs={'zookeeper_id': self.id})
	
class Animal(models.Model):
	name = models.CharField(max_length=100)
	species = models.CharField(max_length=100)
	gender = models.CharField(max_length=250)
	age = models.IntegerField()
	needs_meds = models.BooleanField(null=False)
	zookeepers = models.ManyToManyField(Zookeeper)
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('info', kwargs={'animal_id': self.id})

class Medication(models.Model):
	date = models.DateField('Administration date')
	med = models.CharField(max_length=250)
	animal = models.ForeignKey(Animal, on_delete=models.CASCADE)

	class Meta:
		ordering = ['-date']
	def __str__(self):
		return self.animal, self.med, self.date