from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User,Curstomer,Driver,Job
from django import forms
from django.forms import ModelForm

class JobForm(ModelForm):
	class Meta:
		model =Job
		fields =('product','assign_driver','load_size','origin','destination','budget','description')


		labels = {

		'product':'',
		'assign_driver':'',
		#'owner':'select the owner of the product',
		'load_size':'',
		'origin':'',
		'destination':'',
		'budget':'',
		'description':''

		}


		widgets= {
			'product' :forms.TextInput(attrs={'class':'form-control','placeholder':'enter product name '}),
			'assign_driver':forms.TextInput(attrs={'class':'form-control','placeholder':'assign driver imediatelly'}),
			#'owner':forms.Select(attrs={'class':'form-select','placeholder':''}),
			'load_size':forms.TextInput(attrs={'class':'form-control','placeholder':'the capacity of the load in kgs'}),
			'origin':forms.TextInput(attrs={'class':'form-control','placeholder':'good are delivered  from '}),
			'destination':forms.TextInput(attrs={'class':'form-control','placeholder':'good are to be transported to '}),
			'budget':forms.TextInput(attrs={'class':'form-control','placeholder':'estimate budget for transportation in ksh'}),
			'description':forms.Textarea(attrs={'class':'form-control','placeholder':'give the description including the place to delievr to and from '})
		}




class CurstomerForm(UserCreationForm):
	first_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	phone = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
	#image =forms.ImageField(widget=forms.ImageInput())


	class Meta(UserCreationForm.Meta):
		model =User

	def __init__(self,*args,**kwargs):
		super(UserCreationForm,self).__init__(*args,**kwargs)

		self.fields['username'].widget.attrs['class']='form-control'
		self.fields['username'].widget.attrs['autocomplete']='off'
		self.fields['password1'].widget.attrs['class']='form-control'
		self.fields['password2'].widget.attrs['class']='form-control'

	#user a single transaction to save to database
	@transaction.atomic
	def save(self):
		#save to user table role of driver

		user =super().save(commit=False)
		user.is_curstomer=True
		user.first_name = self.cleaned_data.get('first_name')
		user.last_name = self.cleaned_data.get('last_name')
		user.is_curstomer=True
		user.save()

		#save to curstomer table 
		client = Curstomer.objects.create(user=user)
		client.phone = self.cleaned_data.get('phone')
		client.email = self.cleaned_data.get('email')
		client.save()
		return user



		
		





class DriverForm(UserCreationForm):
	first_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	phone = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	driving_licence = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	truck_plates = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	truck_capacity = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta(UserCreationForm.Meta):
		model =User



	def __init__(self,*args,**kwargs):
		super(UserCreationForm,self).__init__(*args,**kwargs)

		self.fields['username'].widget.attrs['class']='form-control'
		self.fields['username'].widget.attrs['autocomplete']='off'
		self.fields['password1'].widget.attrs['class']='form-control'
		self.fields['password2'].widget.attrs['class']='form-control'


	@transaction.atomic
	def save(self):
 
		#save to user table role of driver

		user =super().save(commit=False)
		user.is_driver=True
		user.first_name = self.cleaned_data.get('first_name')
		user.last_name = self.cleaned_data.get('last_name')
		user.save()

		# validate and save to driver table

		driver = Driver.objects.create(user=user)
		driver.phone = self.cleaned_data.get('phone')
		driver.email = self.cleaned_data.get('email')
		driver.driving_licence = self.cleaned_data.get('driving_licence')
		driver.truck_capacity =self.cleaned_data.get('truck_capacity')
		driver.truck_plates =self.cleaned_data.get('truck_plates')
		driver.save() 
		return driver
