
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, AboutView
from django.urls import path
from .views import HomeView
from .views import AboutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('home', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
]
