from django.shortcuts import get_object_or_404, render
from . import models

# Create your views here.
def home(request):
    ''' this is function of the blog home. '''
    context = {
        "contents": models.HomeContent.objects.all().order_by('-published'),
    }
    return render(request, 'blog/base.html', context)

def details(request, slug):
    ''' this is function of the blog details articles. '''
    context = {
        "article": get_object_or_404(models.Article, slug=slug),
        "topics": models.Topics.objects.all()
    }
    return render(request, "blog/details.html", context)

def blog(request):
    ''' this is function of the site (blog)'''
    context = {
        "articles": models.Article.objects.filter(status="P").order_by('-published'),
        "topics": models.Topics.objects.all()
    }
    return render(request, "blog/blog.html", context)

def topics(request):
    ''' this is function of the article topics. '''
    context = {
        "topics": models.Topics.objects.all()
    }
    return render(request, 'blog/topics.html', context)

def topic(request, slug):
    ''' this is function of the topics. '''
    context = {
        "topic": get_object_or_404(models.Topics, slug=slug),
        "topics": models.Topics.objects.all()
    }
    return render(request, "blog/topic.html", context)
