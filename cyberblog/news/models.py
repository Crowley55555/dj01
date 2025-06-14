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
    likes_count = models.PositiveIntegerField(default=0, verbose_name='Количество лайков')
    dislikes_count = models.PositiveIntegerField(default=0, verbose_name='Количество дизлайков')

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

class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments', verbose_name='Новость')
    author_name = models.CharField(max_length=100, verbose_name='Имя автора')
    content = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['created_at']

    def __str__(self):
        return f'Комментарий от {self.author_name} к новости {self.news.title}'

class NewsReaction(models.Model):
    REACTION_CHOICES = (
        ('like', 'Лайк'),
        ('dislike', 'Дизлайк'),
    )

    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='reactions', verbose_name='Новость')
    ip_address = models.GenericIPAddressField(verbose_name='IP адрес')
    reaction = models.CharField(max_length=7, choices=REACTION_CHOICES, verbose_name='Реакция')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата реакции')

    class Meta:
        verbose_name = 'Реакция на новость'
        verbose_name_plural = 'Реакции на новости'
        unique_together = ['news', 'ip_address']  # Один IP может поставить только одну реакцию на новость

    def __str__(self):
        return f'{self.get_reaction_display()} от {self.ip_address} к новости {self.news.title}'
