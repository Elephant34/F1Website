from django.contrib import admin
from django.urls import path

from .views import emailView, successView

urlpatterns = [
    path('contact-us/', emailView, name='contact-us'),
    path('success/', successView, name='success'),
]