from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class News(models.Model):
    STATUS_CHOICES = (
        ('pending', 'На модерации'),
        ('approved', 'Одобрено'),
        ('rejected', 'Отклонено'),
    )

    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL-имя')
    content = models.TextField(verbose_name='Содержание')
    image = models.ImageField(upload_to='news/', verbose_name='Изображение', blank=True)
    source = models.CharField(max_length=100, verbose_name='Источник')
    author_name = models.CharField(max_length=100, default='Аноним', verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    moderation_status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name='Статус модерации'
    )
    moderation_comment = models.TextField(blank=True, null=True, verbose_name='Комментарий модератора')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
