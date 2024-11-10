from django.views.generic import View
from django.shortcuts import render
class HomeView(View):
   def get(self, request, *args, **kwargs):
       context={
           
       }
       return render(request, 'home.html',context)
class AboutView(View):
   def get(self, request, *args, **kwargs):
       context = {}
       return render(request, 'about.html', context)
   
  