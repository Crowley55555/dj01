"""
URL configuration for ai_blog application.

Defines the routing for data and test pages.
"""
from django.urls import path
from .views import (
    HomeView, ArticleDetailView, ArticleCreateView,
    data_page, prompt_page
)

app_name = 'ai_blog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<slug:slug>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article/create/', ArticleCreateView.as_view(), name='article_create'),
    path('data/', data_page, name='data'),
    path('prompt/', prompt_page, name='prompt'),
]