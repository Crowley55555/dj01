from django.contrib import admin
from .models import Article, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at', 'is_published')
    list_filter = ('category', 'is_published', 'created_at')
    search_fields = ('title', 'content', 'author')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    list_editable = ('is_published',)
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'slug', 'author', 'category', 'image')
        }),
        ('Содержание', {
            'fields': ('summary', 'content')
        }),
        ('Статус', {
            'fields': ('is_published',)
        }),
    )
