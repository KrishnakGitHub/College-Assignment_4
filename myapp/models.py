from django.db import models

# Create your models here.
class Department(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Student(models.Model):
	name = models.CharField(max_length=100)
	Department = models.ForeignKey(Department,on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']

class Lecturer(models.Model):
	name = models.CharField(max_length=100)
	Department = models.ManyToManyField(Department)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']
