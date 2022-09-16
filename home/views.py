from django.shortcuts import render
from .models import *


def home(request):
    return render(request, "home/home.html")


def blog(request):
    articles = Article.objects.all()
    return render(request, "home/blog.html", context={"articles": articles})


def article(request, article_id):
    current_article = Article.objects.get(id=article_id)
    current_article.visited()
    print(current_article.views)
    paragraphs = Paragraph.objects.filter(article=current_article).order_by("order")
    recent_articles = Article.objects.all()[:2]
    context = {
        "article_title": current_article.article_title,
        "paragraphs": paragraphs,
        "recent_articles": recent_articles
    }
    return render(request, "home/article.html", context=context)
