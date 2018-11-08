from django.shortcuts import render
from .models import GitCours
from .models import LinuxCours
from .models import PyCours
from .models import JsCours
from .models import JqCours
from .models import MyCours

from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def courses(request):
    template = "courses.html"
    return render(request,template)

@login_required(login_url='/')
def githome(request):
	Content = GitCours.objects.all()


	context = {'Content':Content,}
	template = 'git_course.html'
	return render(request,template,context)
@login_required(login_url='/')
def linuxhome(request):
	Content = LinuxCours.objects.all()
	context = {'Content':Content,}
	template = 'li_course.html'
	return render(request,template,context)

@login_required(login_url='/')
def pyhome(request):
	Content = PyCours.objects.all()
	context = {'Content':Content,}
	template = 'py_course.html'
	return render(request,template,context)


@login_required(login_url='/')
def jshome(request):
	Content = JsCours.objects.all()
	context = {'Content':Content,}
	template = 'js_course.html'
	return render(request,template,context)

@login_required(login_url='/')
def jqueryhome(request):
	Content = JqCours.objects.all()
	context = {'Content':Content,}
	template = 'Jq_course.html'
	return render(request,template,context)

@login_required(login_url='/')
def mysqlhome(request):
	Content = MyCours.objects.all()
	context = {'Content':Content,}
	template = 'my_course.html'
	return render(request,template,context)
