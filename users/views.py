from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render

from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def handler404(request):
    return render(request, 'errors/404.html', status=404)

def handler500(request):
    return render(request, 'errors/500.html', status=500)