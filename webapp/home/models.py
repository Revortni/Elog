from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	medicines = models.CharField(max_length = 500)
	created = models.DateTimeField(auto_now_add = True)
	log = models.CharField(max_length = 500)