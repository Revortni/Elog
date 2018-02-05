from django.views.generic import TemplateView
from django.shortcuts import render
from home.forms import LogForm
from django.contrib.auth.models import User
from home.models import Post


class HomeView(TemplateView):
	template_name = 'accounts/profile.html' #homepage for homeapp

	def get(self, request):
		form = LogForm()
		user = User.objects.all().filter(is_staff=False )
		posts= Post.object.all().order_by('-created')

		return render(request,self.template_name,{'form': form,'users':user,'posts':posts})

	def post(request):
		if request.method=='POST':
			form = LogForm(request.POST, instance = request.user)

			if form.is_valid():
				post = form.save(commit = False)
				post.user = request.user
				post.save()
				medicine = form.cleaned_data['medicine']
				log = form.cleaned_data['log']

				form =LogForm()
				return HttpResponseRedirect("")

			args = {'form':form}
			return render(request,self.template_name,args )