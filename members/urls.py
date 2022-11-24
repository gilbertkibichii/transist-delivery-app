from django.urls import path
from . import views	 

urlpatterns = [
	path('curstomer_register/',views.Curstomer_register.as_view(), name='Curstomer_register'),
	path('driver_register/',views.Driver_register.as_view(), name='Driver_register'),
	path('list_jobs/',views.list_jobs, name='list-jobs'),
	path('update_jobs/<job_id>/',views.update_jobs, name='update-job'),
	path('delete_jobs/<job_id>/',views.delete_jobs, name='delete-job'),
	path('add_job/',views.add_job, name='add_job'),
	path('home/',views.home, name ='home'),
	path('login/',views.login_user,name='login'),
	path('logout/',views.logout_user, name='logout'),
	path('job_info/<job_id>/',views.job_info,name='job_info'),
	path('user/<user_id>/',views.user,name='user'),
	path('take_job/<job_id>/',views.take_job,name='take_job')
]