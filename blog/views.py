from django.shortcuts import render, get_object_or_404
from .models import Article


def blog(request):
    articles = Article.objects.order_by('-blogDate')[:5]
    return render(request, 'blog/all_blogs.html', {'articles': articles})


def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'blog/detail.html', {'article': article})