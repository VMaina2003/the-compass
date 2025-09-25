from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import NewsArticle, Writer, Category, Comment

def index(request):
    articles = NewsArticle.objects.all().order_by('-published_at')[:5]
    context = {'articles': articles}    
    
    return render(request, 'newsapp/index.html', context)

def article_detail(request, article_id):
    article = NewsArticle.objects.get(id=article_id)
    comments = article.comments.all().order_by('-created_at')
    context = {'article': article, 'comments': comments}
    
    return render(request, 'newsapp/article_detail.html', context)  