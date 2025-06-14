from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
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

class HomeView(ListView):
    model = Article
    template_name = 'ai_blog/home.html'
    context_object_name = 'articles'
    paginate_by = 10

    def get_queryset(self):
        return Article.objects.filter(is_published=True).select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
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

def prompt_page(request):
    return render(request, 'ai_blog/prompt.html')

@csrf_exempt
@require_http_methods(["POST"])
def analytics(request):
    try:
        page = request.POST.get('page', '')
        time = request.POST.get('time', '')
        
        # Здесь можно добавить логику сохранения аналитики
        # Например, в базу данных или файл логов
        print(f"Analytics: Page={page}, Time={time}")
        
        return HttpResponse(status=200)
    except Exception as e:
        print(f"Analytics error: {str(e)}")
        return HttpResponse(status=500)