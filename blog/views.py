from django.shortcuts import render, get_object_or_404
from .models import Article,Tag
from django.db.models import Q

# Create your views here.

def home(request):
    featured = Article.articlemanager.filter(featured = True)[0:3]
    # print('============', featured)
    context = {
        'articles': featured
    }
    return render(request, 'index.html', context)


def article(request, article):
    # print('==', request,'==',article)
    articl_e = get_object_or_404(Article, slug=article, status = "published")

    context = {
        'article': articl_e
    }
    return render(request, 'article.html', context)

def articles(request):
    query = request.GET.get('query')
    # print('=============', query)

    if query == None:
        query = ''

    articles = Article.articlemanager.filter(
        Q(headline__icontains = query) |
        Q(sub_headline__icontains = query) |
        Q(body__icontains = query) 
    )
    # print('===========',articles)

    tags = Tag.objects.all()

    context = {
        'articles': articles,
        'tags': tags
    }
    
    return render(request, 'articles.html', context)