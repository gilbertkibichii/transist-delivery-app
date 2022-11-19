from django.contrib import admin
from .models import User,Driver,Curstomer,Job
from django.contrib.admin.models import LogEntry


#admin.site.register(User)
#admin.site.register(Driver)
#admin.site.register(Curstomer)


LogEntry.objects.all().delete()

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
	list_display=('owner','product','load_size')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display =('first_name','last_name')

''
@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
	list_display = ('user','phone','truck_capacity',)
	
@admin.register(Curstomer)
class CurstomerAdmin(admin.ModelAdmin):
	list_display = ('user','phone','email')

