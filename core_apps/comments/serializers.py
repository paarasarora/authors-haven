from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Comment

User = get_user_model()


class CommentSerializer(serializers.ModelSerializer):
    user_first_name = serializers.CharField(source = 'user.first_name', read_only=True)
    parent_comment = serializers.CharField(source = 'parent_comment.content',read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "user", "article", "content","parent_comment","user_first_name"]


class CommentListSerializer(serializers.ModelSerializer):
    article = serializers.ReadOnlyField(source="article.title",read_only=True)
    user_first_name = serializers.CharField(source = 'user.first_name', read_only=True)
    parent_comment = serializers.CharField(source = 'parent_comment.content',read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "user", "parent_comment","article", "content","user_first_name"]
