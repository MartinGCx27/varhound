
from django.contrib import admin
from django.urls import path
from .views import HomeView
from .views import AboutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('home', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about')
]
