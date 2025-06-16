from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.core.cache import cache
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib import messages
import json
from .models import Article, Category
from .forms import ArticleForm
from news.models import News, NewsReaction
from django.db.models import Count, Q
from django.contrib.auth.decorators import login_required
from datetime import timedelta

class HomeView(TemplateView):
    template_name = 'ai_blog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_news'] = News.objects.filter(is_published=True).order_by('-created_at')[:5]
        return context

class ArticleListView(ListView):
    model = Article
    template_name = 'ai_blog/article_list.html'
    context_object_name = 'articles'
    paginate_by = 10

    def get_queryset(self):
        queryset = Article.objects.filter(is_published=True).select_related('category')
        category_slug = self.request.GET.get('category')
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        return queryset.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'ai_blog/article_detail.html'
    context_object_name = 'article'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Article.objects.filter(is_published=True).select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'ai_blog/article_form.html'
    success_url = reverse_lazy('ai_blog:home')

    def form_valid(self, form):
        messages.success(self.request, 'Статья успешно создана!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

def data_page(request):
    return render(request, 'ai_blog/data.html')

def about(request):
    return render(request, 'ai_blog/about.html')

def contact(request):
    return render(request, 'ai_blog/contact.html')

def prompt_page(request):
    return render(request, 'ai_blog/prompt.html')

def test(request):
    return render(request, 'ai_blog/test.html')