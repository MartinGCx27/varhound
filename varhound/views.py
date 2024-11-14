from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView
from django import forms
from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
class HomeView(View):
   def get(self, request, *args, **kwargs):
       context={
           
       }
       return render(request, 'home.html',context)
class AboutView(LoginRequiredMixin, TemplateView):
    
    template_name = 'about.html'
    login_url = '/login/'
   

   

# Formulario personalizado para login
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class CustomLoginView(FormView):
    template_name = 'login.html'  # El archivo HTML del formulario de inicio de sesión
    form_class = LoginForm
    success_url = reverse_lazy('home')  # Redirige al usuario autenticado a 'dashboard'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            messages.error(self.request, 'Nombre de usuario o contraseña incorrectos')
            return self.form_invalid(form)