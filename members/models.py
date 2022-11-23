from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	is_curstomer = models.BooleanField(default=False)
	is_driver = models.BooleanField(default=False)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	#image =models.ImageField(default='',blank =True,upload_to ='images')



class Curstomer(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE ,primary_key=True)
	phone = models.CharField(max_length=20)
	email =models.EmailField('curstomer email')

	def __str__(self):
		return self.user.first_name + ' '+ self.user.last_name	


class Driver(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	phone = models.CharField(max_length=20)
	email =models.EmailField('curstomer email')
	driving_licence = models.CharField(max_length=10)
	truck_capacity = models.CharField(max_length=10)
	truck_plates =models.CharField(max_length=10)


	def __str__(self):
		return self.email


class Job(models.Model):
	owner=models.ForeignKey(User,on_delete=models.CASCADE)
	assign_driver = models.IntegerField(default=0)
	product = models.CharField(max_length=50)
	product_category = models.CharField(max_length=30,default=product)
	load_size =models.CharField(max_length=30)
	origin =models.CharField('origin destination',max_length=30)
	destination =models.CharField('final destination',max_length=30)
	budget = models.CharField('estinate budget',max_length=10)
	description = models.TextField()
	


	def __self__(self):
		return self.product





