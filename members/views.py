from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.http import HttpResponseRedirect 
from .models import User,Curstomer,Driver,Job
from .forms import CurstomerForm,DriverForm,JobForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

#delete the jobs 


def delete_jobs(request,job_id):
	job =Job.objects.get(pk=job_id)
	job.delete()
	return redirect('list-jobs')

#update the jobs 
def update_jobs(request,job_id):
	job =Job.objects.get(pk=job_id)
	form=JobForm(request.POST or None,instance=job)
	if form.is_valid():
		form.save()
		return redirect('list-jobs')
	return render(request,'members/update_job.html',{'form':form})



#list of jobs display

def list_jobs(request):
	jobs =Job.objects.all()
	context={
		'jobs':jobs
	}
	return render(request,'members/list_jobs.html',context)



#rendering form to add a job
def add_job(request):
	submitted=False
	if request.method == "POST":
		form=JobForm(request.POST)
		if form.is_valid():
			form.save()
			submitted=True
			return redirect('list-jobs')
			messages.success(request, 'task added succesfull .')
	else:
		form =JobForm
		if submitted in request.GET:
			submitted=True

	
	return render(request,'members/add_job.html',{'form':form,'submitted':submitted})




#logout form for all users
def logout_user(request):
	logout(request)
	return redirect('login')



#login users of the page
def login_user(request):
	if request.method =="POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('home')

		else:
			return redirect('login')



	else:
		return render(request,'members/login.html',{})


def home(request):
	return render(request,'members/home.html')


#
#createView display a form for creating  an object  if there is no object return non
class Curstomer_register(CreateView):
	model=User
	form_class =CurstomerForm
	template_name = 'members/curstomer_register.html'



class Driver_register(CreateView):
	model=User
	form_class =DriverForm
	template_name = 'members/driver_register.html'
	redirect ="home"





