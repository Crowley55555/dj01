"""
URL configuration for news application.
"""
from django.urls import path
from .views import NewsListView, NewsDetailView, NewsCreateView

app_name = 'news'

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('create/', NewsCreateView.as_view(), name='news_create'),
    path('<slug:slug>/', NewsDetailView.as_view(), name='news_detail'),
]
