from django.shortcuts import render
from . import models

# Create your views here.
def home(request):
    ''' this is function of the blog home. '''
    context = {
        "articles": models.Article.objects.all()
    }
    return render(request, 'blog/base.html', context)
