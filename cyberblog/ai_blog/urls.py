"""
URL configuration for ai_blog application.

Defines the routing for data and test pages.
"""
from django.urls import path
from . import views

app_name = 'ai_blog'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('article/<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('article/create/', views.ArticleCreateView.as_view(), name='article_create'),
    path('data/', views.data_page, name='data'),
    path('prompt/', views.prompt_page, name='prompt'),
    path('test/', views.test, name='test'),
]