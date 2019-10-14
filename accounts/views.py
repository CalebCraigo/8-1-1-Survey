from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.contrib.auth import logout
from django.urls import reverse_lazy

class LoginView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('surveys:index')
    template_name = 'login.html'
# Create your views here.
