from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    slug = models.SlugField(unique=True, verbose_name='URL-имя')
    description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, verbose_name='URL-имя')
    summary = models.TextField(verbose_name='Краткое описание')
    content = models.TextField(verbose_name='Содержание')
    image = models.ImageField(upload_to='articles/', verbose_name='Изображение')
    author = models.CharField(max_length=100, verbose_name='Автор')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles', verbose_name='Категория')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
