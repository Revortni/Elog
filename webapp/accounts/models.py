from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator

# Create your models here.
class UserProfileManager(models.Manager):
	def get_queryset(self):
		return super(UserProfileManager,self).get_queryset().filter()
		
class PatientProfile(models.Model):
	user = models.OneToOneField(User,on_delete = models.CASCADE)
	
	def __str__(self):
		return self.user.username	
def create_profile(sender, **kwargs):
	if kwargs['created']:
		Patient_profile =PatientProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender = User)

