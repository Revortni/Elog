from django.urls import path
from django.conf.urls import url
from home.views import HomeView

urlpatterns = [
    path('',HomeView.as_view(),name ='home')
]