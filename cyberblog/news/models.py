from django.db import models
from django.utils import timezone

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, verbose_name='URL-имя')
    content = models.TextField(verbose_name='Содержание')
    image = models.ImageField(upload_to='news/', verbose_name='Изображение', blank=True)
    source = models.CharField(max_length=100, verbose_name='Источник')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
