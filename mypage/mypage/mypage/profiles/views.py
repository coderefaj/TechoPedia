from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import course_name

# Create your views here.
def home(request):
	p = course_name.objects.all()
	context = {'p':p,}
	template = 'index.html'
	return render(request,template,context)
def about(request):
	context = {}
	template = 'about.html'
	return render(request , template , context)

@login_required
def userProfile(request):
	user = request.user

	context = {'user':user}
	template = 'profile.html'
	return render(request,template,context)
