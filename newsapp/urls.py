from django.urls import path, include
from .views import index, article_detail, create_news_article, update_news_article, NewsArticleViewSet, CategoryViewSet, CommentViewSet, delete_comment, NewsletterViewSet, subscribe_newsletter, confirm_subscription, unsubscribe_newsletter
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register (r'articles', NewsArticleViewSet)
router.register (r'categories', CategoryViewSet)
router.register (r'comments', CommentViewSet)
router.register (r'newsletters', NewsletterViewSet)


urlpatterns = [
    path('', index, name='index'),
    path('article/<int:article_id>/', article_detail, name='article_detail'),
    path('article/create/', create_news_article, name='create_news_article'),
    path('article/<int:article_id>/update/', update_news_article, name='update_news_article'),
    path('comment/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
    path('subscribe/', subscribe_newsletter, name='subscribe_newsletter'),
    path('newsletter/confirm/', confirm_subscription, name='confirm_subscription'),
    path('newsletter/unsubscribe/', unsubscribe_newsletter, name='unsubscribe_newsletter'),
    path('api/', include(router.urls)),
]