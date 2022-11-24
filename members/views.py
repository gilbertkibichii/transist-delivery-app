from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.http import HttpResponseRedirect 
from .models import User,Curstomer,Driver,Job
from .forms import CurstomerForm,DriverForm,JobForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.mail import send_mail

def take_job(request,job_id):
	job =Job.objects.get(pk=job_id)

	if request.user.is_driver:
		job.assign_driver=request.user.id
		send_mail(
			"bid for the job",
			"I am exited to be applying for the Transport position ",
			"{{request.user.email}}",
			['{{job.owner.email}}'],
			fail_silently=False
			)
		if job.assign_driver==request.user.id:
			messages.success(request,"you've been assigned the task proceed to the destination")

	return render(request,'members/take_job.html',{})



def user(request,user_id):
	user =User.objects.get(pk=user_id)
	return render(request,'members/user.html',{'user':user})




def job_info(request,job_id):
	job=Job.objects.get(pk=job_id)
	if request.user.is_driver or request.user.is_superuser:
		return render(request,'members/job_info.html',{'job':job})

	else:
		messages.success(request,"only drivers are allowed to access this page ")
		return redirect('list-jobs')




#delete the jobs 
def delete_jobs(request,job_id):
	if request.user.is_curstomer or request.user.is_superuser:
		job =Job.objects.get(pk=job_id)
		if request.user ==job.owner:
			job.delete()
			return redirect('list-jobs')
		else:
			messages.success(request,'you\'re not allowed to delete this job !!!')
			return redirect('list-jobs')

	else:
		messages.success(request,"access denied driver are not allowed to delete jobs")
		return redirect('list-jobs')

#update the jobs 
def update_jobs(request,job_id):
	job =Job.objects.get(pk=job_id)
	if request.user ==job.owner or request.user.is_superuser:
		form=JobForm(request.POST or None,instance=job)
		if form.is_valid():
			form.save()
			return redirect('list-jobs')

		#else:
			#return render(request,'members/update_job.html',{'form':form})

	else:
		messages.success(request,"you`re not allowed to update this event")
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
	if request.user.is_curstomer or request.user.is_superuser:
		if request.method == "POST":
			form=JobForm(request.POST)
			if form.is_valid():
				job_info =form.save(commit=False)
				job_info.owner =request.user
				#job_info.assign_driver=request.user.id
				job_info.save()
				submitted=True
				messages.success(request, 'task added succesfull .')
				return redirect('list-jobs')
				
		else:
			form =JobForm
			if submitted in request.GET:
				submitted=True

	else:
		messages.success(request,"sorry permission denied,  you're not allowed to access this page ")
		return redirect('list-jobs')

	
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
			messages.success(request,"invalid login details please try again")
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





