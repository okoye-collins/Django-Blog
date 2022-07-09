from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def article(request):
    return render(request, 'article.html')

def articles(request):
    return render(request, 'articles.html')