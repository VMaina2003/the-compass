from rest_framework import serializers
from .models import NewsArticle, Category, Comment ,newsletter 


class NewsArticleSerializer(serializers.ModelSerializer):
    writer = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = NewsArticle
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        
class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = newsletter
        fields = '__all__'