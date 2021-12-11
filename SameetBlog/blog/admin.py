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
    prepopulated_fields = {
        'slug': ('title',)
    }
    search_fields = [
        'title', 'body'
    ]
    ordering = [
        'title'
    ]
admin.site.register(models.HomeContent, HomeContentConfig)
