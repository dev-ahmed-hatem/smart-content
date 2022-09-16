from django.urls import path
from .views import *

app_name = "home"
urlpatterns = [
    path("", home, name="home"),
    path("blog/", blog, name="blog"),
    path("article-<int:article_id>/", article, name="article"),
]
