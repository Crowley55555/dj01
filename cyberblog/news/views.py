from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.text import slugify
from datetime import datetime
from .models import News, Comment
from .forms import NewsForm, CommentForm

# Create your views here.
def home (request):
    return render(request, 'ai_blog/home.html')

class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'
    paginate_by = 10

    def get_queryset(self):
        return News.objects.filter(is_published=True).order_by('-created_at')

class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return News.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = self.object.comments.filter(is_published=True).order_by('created_at')
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = self.object
            comment.save()
            messages.success(request, 'Комментарий успешно добавлен!')
            return redirect('news:news_detail', slug=self.object.slug)
        else:
            context = self.get_context_data()
            context['comment_form'] = form
            return self.render_to_response(context)

class NewsCreateView(CreateView):
    model = News
    form_class = NewsForm
    template_name = 'news/news_form.html'
    success_url = reverse_lazy('news:news_list')

    def form_valid(self, form):
        news = form.save(commit=False)
        news.author_name = form.cleaned_data['author_name']
        news.is_published = True
        news.moderation_status = 'approved'
        
        # Генерируем уникальный slug
        base_slug = slugify(news.title)
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        news.slug = f"{base_slug}-{timestamp}"
        
        news.save()
        messages.success(self.request, 'Новость успешно опубликована!')
        return redirect('news:news_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создать новость'
        context['button_text'] = 'Опубликовать'
        return context
