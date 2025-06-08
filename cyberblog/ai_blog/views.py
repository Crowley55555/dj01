from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.core.cache import cache
from .models import Article, Category

class HomeView(ListView):
    model = Article
    template_name = 'ai_blog/home.html'
    context_object_name = 'articles'
    paginate_by = 5

    def get_queryset(self):
        return Article.objects.filter(is_published=True).select_related('category').order_by('-created_at')

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

def data_page(request):
    return render(request, 'ai_blog/data.html')

def prompt_page(request):
    return render(request, 'ai_blog/prompt.html')

def test_page(request):
    return render(request, 'ai_blog/test.html')