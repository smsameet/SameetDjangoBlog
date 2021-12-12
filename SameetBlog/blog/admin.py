from django.contrib import admin
from . import models

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'published', 'status'
    )
    list_filter = (
        'status', 'published'
    )
    prepopulated_fields = {
        'slug': ('title',)
    }
    search_fields = [
        'title', 'body'
    ]
    ordering = [
        '-published'
    ]
admin.site.register(models.Article, ArticleAdmin)

class HomeContentConfig(admin.ModelAdmin):
    list_display = (
        'title',
    )
    list_filter = (
        'title',
    )
    search_fields = [
        'title', 'body'
    ]
    ordering = [
        'title'
    ]
admin.site.register(models.HomeContent, HomeContentConfig)

class TopicsConfig(admin.ModelAdmin):
    list_display = (
        'title', 'slug', 'position'
    )
    list_filter = (
        'title',
    )
    search_fields = [
        'title', 'position', 'slug'
    ]
admin.site.register(models.Topics, TopicsConfig)
