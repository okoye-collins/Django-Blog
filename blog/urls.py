from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('article', views.article, name='article'),
    path('articles', views.articles, name='articles')
]