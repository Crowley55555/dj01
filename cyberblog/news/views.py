from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.text import slugify
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from .models import News, Comment, NewsReaction
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
        
        # Получаем реакцию пользователя, если она есть
        if self.request.user.is_authenticated:
            try:
                user_reaction = self.object.reactions.get(ip_address=self.request.META.get('REMOTE_ADDR'))
                context['user_reaction'] = user_reaction.reaction
            except NewsReaction.DoesNotExist:
                context['user_reaction'] = None
        else:
            context['user_reaction'] = None
            
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

class NewsCreateView(LoginRequiredMixin, CreateView):
    model = News
    form_class = NewsForm
    template_name = 'news/news_form.html'
    success_url = reverse_lazy('news:news_list')
    login_url = reverse_lazy('login')  # URL для перенаправления неавторизованных пользователей

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

@csrf_exempt
@require_POST
def news_reaction(request, slug):
    news = get_object_or_404(News, slug=slug, is_published=True)
    reaction_type = request.POST.get('reaction')
    ip_address = request.META.get('REMOTE_ADDR')

    if reaction_type not in ['like', 'dislike']:
        return JsonResponse({'error': 'Неверный тип реакции'}, status=400)

    try:
        # Пытаемся получить существующую реакцию
        user_reaction = news.reactions.get(ip_address=ip_address)
        
        if user_reaction.reaction == reaction_type:
            # Если реакция такая же, удаляем её
            user_reaction.delete()
            if reaction_type == 'like':
                news.likes_count = max(0, news.likes_count - 1)
            else:
                news.dislikes_count = max(0, news.dislikes_count - 1)
        else:
            # Если реакция другая, меняем её
            old_reaction = user_reaction.reaction
            user_reaction.reaction = reaction_type
            user_reaction.save()
            
            if old_reaction == 'like':
                news.likes_count = max(0, news.likes_count - 1)
                news.dislikes_count += 1
            else:
                news.dislikes_count = max(0, news.dislikes_count - 1)
                news.likes_count += 1
    except NewsReaction.DoesNotExist:
        # Создаем новую реакцию
        NewsReaction.objects.create(
            news=news,
            ip_address=ip_address,
            reaction=reaction_type
        )
        if reaction_type == 'like':
            news.likes_count += 1
        else:
            news.dislikes_count += 1

    news.save()
    
    return JsonResponse({
        'likes': news.likes_count,
        'dislikes': news.dislikes_count,
        'user_reaction': reaction_type
    })
