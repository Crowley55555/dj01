from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import News
from .forms import NewsForm

def news_list(request):
    news = News.objects.filter(is_published=True)
    return render(request, 'news/news_list.html', {'news': news})

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'news/news_detail.html', {'news': news})

@login_required
def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            messages.success(request, 'Новость успешно создана!')
            return redirect('news:news_detail', pk=news.pk)
    else:
        form = NewsForm()
    return render(request, 'news/news_form.html', {'form': form, 'title': 'Создать новость'})

@login_required
def edit_news(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.user != news.author:
        messages.error(request, 'У вас нет прав для редактирования этой новости!')
        return redirect('news:news_detail', pk=pk)
    
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            messages.success(request, 'Новость успешно обновлена!')
            return redirect('news:news_detail', pk=news.pk)
    else:
        form = NewsForm(instance=news)
    return render(request, 'news/news_form.html', {'form': form, 'title': 'Редактировать новость'})

@login_required
def delete_news(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.user != news.author:
        messages.error(request, 'У вас нет прав для удаления этой новости!')
        return redirect('news:news_detail', pk=pk)
    
    if request.method == 'POST':
        news.delete()
        messages.success(request, 'Новость успешно удалена!')
        return redirect('news:news_list')
    return render(request, 'news/news_confirm_delete.html', {'news': news}) 