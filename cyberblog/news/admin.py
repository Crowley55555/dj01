from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_name', 'source', 'created_at', 'is_published', 'moderation_status')
    list_filter = ('is_published', 'moderation_status', 'created_at')
    search_fields = ('title', 'content', 'author_name', 'source')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'slug', 'content', 'image', 'source', 'author_name')
        }),
        ('Статус', {
            'fields': ('is_published', 'moderation_status', 'moderation_comment')
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    actions = ['make_published', 'make_unpublished']

    def make_published(self, request, queryset):
        queryset.update(is_published=True, moderation_status='approved')
    make_published.short_description = "Опубликовать выбранные новости"

    def make_unpublished(self, request, queryset):
        queryset.update(is_published=False)
    make_unpublished.short_description = "Снять с публикации выбранные новости"
