from django.shortcuts import render

# Create your views here.
def home(request):
    ''' this is function of the blog home. '''
    context = {}
    return render(request, 'blog/base.html', context)
