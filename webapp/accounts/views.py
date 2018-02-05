from django.shortcuts import render,redirect
from .forms import RegistrationForm,EditProfileForm
from home.forms import LogForm
from django.contrib.auth.forms import UserChangeForm
from home.models import Post
from django.contrib.auth.models import User

# Create your views here.

def home(request):
	return render(request,'accounts/home.html')

def login_redirect(request):
	return redirect('/accounts/')

def register(request):
	if request.method =='POST':
		form = RegistrationForm(request.POST) 
		if form.is_valid():
			form.save()
			return redirect('/accounts/')
	else:
		form = RegistrationForm()
		args ={'form': form}
		return render(request,'accounts/reg_form.html',args)


def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
        posts = Post.objects.all().order_by('-created').filter(user_id=user.id)
        args = {'form':LogForm,'user':user,'posts':posts}
        if request.method=='POST':
        	form = LogForm(request.POST)
        	if form.is_valid():
        		post = form.save(commit = False)
        		post.user = user
        		post.save()
        		medicines = form.cleaned_data['medicines']
        		log = form.cleaned_data['log']
        		form =LogForm()
        	return redirect('accounts:patientlist')
        return render(request,'accounts/profile.html',args)
    else:
        user = request.user
        args ={'user': user}
        return render(request, 'accounts/profile.html', args)

def patientlist(request):
	user=User.objects.all().filter(is_staff=False)
	args = {'user':user}
	return render(request,'accounts/patientlist.html',args)

	
def edit_profile(request):
	if request.method=='POST':
		form = EditProfileForm(request.POST, instance = request.user)

		if form.is_valid():
			form.save()
			return redirect('/accounts/profile/')
	else:
		form = EditProfileForm(instance=request.user)
		args = {'form':form}
		return render(request,'accounts:edit.html',args )

