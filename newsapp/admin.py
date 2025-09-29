from django.contrib import admin
from .models import Category, NewsArticle, Comment, newsletter

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)    
    
@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', 'category', 'published_at')
    search_fields = ('title', 'writer__name', 'category__name')
    list_filter = ('category', 'published_at')
    ordering = ('-published_at',)
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'author_name', 'content', 'created_at')
    search_fields = ('content', 'author_name__username', 'article__title')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    
@admin.register(newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    search_fields = ('email',)
    list_filter = ('subscribed_at',)
    ordering = ('-subscribed_at',)
    
    
# Register your models here.
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(NewsArticle, NewsArticleAdmin)
# admin.site.register(Comment, CommentAdmin)
