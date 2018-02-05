from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
import datetime


class RegistrationForm(UserCreationForm):
	gender = forms.ChoiceField(choices=(('M','Male'),('F','Female')))
	age = forms.IntegerField(required= True,max_value=100,min_value = 1)
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields =(
			'username',
			'first_name',
			'last_name',
			'gender',
			'age',
			'email',
			'password1',
			'password2',
			)


	def save(self, commit=True):
		user= super(RegistrationForm, self).save(commit=False)
		user.username = self.cleaned_data['username']
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.gender = self.cleaned_data['gender']
		user.age = self.cleaned_data['age']
		user.email = self.cleaned_data['email']

		if commit:
			user.save()

		return user

class EditProfileForm(UserChangeForm):

	class Meta:
		model = User
		fields = ('email','first_name','last_name','password')

