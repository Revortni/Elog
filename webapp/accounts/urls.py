from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout
from django.views.generic import ListView, DetailView
from .models import PatientProfile as Patient
from django.contrib.auth.models import User

urlpatterns = [
    path('',views.home,name ='home'),
    path('login/',login,{'template_name':'accounts/login.html'},name='login'),
    path('logout/',logout,{'template_name':'accounts/logout.html'},name='logout'),
    path('register/',views.register,name='register'),
   	url(r'^profile/$',views.view_profile,name='view_profile'),
   	url(r'^profile/edit/$',views.edit_profile,name='edit_profile'),
	  url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
   	url(r'^patientlist/$',views.patientlist,name ='patientlist'),
   	]