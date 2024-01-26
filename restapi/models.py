from django.db import models

# Create your models here.
class roles(models.Model):
	rolename=models.CharField(max_length=50,unique=True)


	def __str__(self):
		return self.rolename



class polling(models.Model):
	name= models.CharField(max_length=15)
	role = models.CharField(max_length=50)
	date = models.DateField(auto_now_add=True)


	def __str__(self):
		return self.name		