from django import forms
import datetime
from .models import Post
class LogForm(forms.ModelForm):
	medicines = forms.CharField(label='Medicines',widget=forms.TextInput(
																			attrs={
																					'class':'form-control',
																					'placeholder':'Medicines'}
																					))
	log = forms.CharField(label='Log',widget=forms.TextInput(
																attrs={
																'class':'form-control',
																'placeholder':'Type the checkup log here...'
																}))


	class Meta:
		model = Post
		fields =('medicines','log',)