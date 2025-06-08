"""
URL configuration for ai_blog application.

Defines the routing for data and test pages.
"""
from django.urls import path
from .views import (
    HomeView, data_page, prompt_page, test_page,
    ArticleListView, ArticleDetailView
)

app_name = 'ai_blog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('articles/<slug:slug>/', ArticleDetailView.as_view(), name='article_detail'),
    path('data/', data_page, name='data'),
    path('prompt/', prompt_page, name='prompt'),
    path('test/', test_page, name='test'),
]