from django.contrib import admin
from accounts.models import PatientProfile
# Register your models here.


class PatientProfileList(admin.ModelAdmin):
	list_display = ('user',)

	def First_Name(self, obj):
		return obj.first_name

	def get_queryset(self,request):
		queryset = super(DoctorProfileList,self).get_queryset(request)
		queryset = queryset.order_by('user')
		return queryset



admin.site.register(PatientProfile,PatientProfileList)