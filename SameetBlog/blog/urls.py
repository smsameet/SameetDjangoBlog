from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name="home"),
    path('blog/', views.blog, name="blog"),
    path('blog/article/<slug:slug>', views.details, name="details"),
    path('topics/', views.topics, name="topics"),
    path('topics/<slug:slug>', views.topic, name="topic")
]
