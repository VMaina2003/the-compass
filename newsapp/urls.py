from django.urls import path
from .views import index, article_detail

urlpatterns = [
    path('', index, name='index'),
    path('article/<int:article_id>/', article_detail, name='article_detail'),
]