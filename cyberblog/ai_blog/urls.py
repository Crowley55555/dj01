"""
URL configuration for ai_blog application.

Defines the routing for data and test pages.
"""
from django.urls import path
from . import views

app_name = 'ai_blog'

urlpatterns = [
    path('', views.home_page, name='home'),  # Добавляем домашнюю страницу
    path('data/', views.data_page, name='data'),
    path('test/', views.test_page, name='test'),
]