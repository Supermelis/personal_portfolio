from django.shortcuts import render
from .models import Article


def blog(request):
    articles = Article.objects.order_by('-blogDate')
    return render(request, 'blog/all_blogs.html', {'articles': articles})