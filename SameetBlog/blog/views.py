from django.shortcuts import get_object_or_404, render
from . import models

# Create your views here.
def home(request):
    ''' this is function of the blog home. '''
    context = {
        "articles": models.Article.objects.all()
    }
    return render(request, 'blog/base.html', context)

def details(request, slug):
    ''' this is function of the blog details articles. '''
    context = {
        "article": get_object_or_404(models.Article, slug=slug)
    }
    return render(request, "blog/details.html", context)
