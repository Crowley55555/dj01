"""
URL configuration for ai_blog application.

Defines the routing for data and test pages.
"""
from django.urls import path
from . import views

app_name = 'ai_blog'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('prompt/', views.prompt_page, name='prompt'),
    path('test/', views.test, name='test'),
    path('data/', views.data_page, name='data'),
]