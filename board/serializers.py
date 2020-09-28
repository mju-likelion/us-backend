# 반환값을 JSON으로 주기 위해 Serialize(직렬화)를 하는 파일

from rest_framework import serializers
from .models import Post

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'author',
            'board_type',
            'title',
            'content',
            'image',
            'like',
            'created_at',
            'update_at',
            'published_at', 
        )
        model = Post

class AddPostSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        board = Post.objects.create(
            author=validated_data["author"],
            board_type=validated_data["board_type"],
            title=validated_data["title"],
            content=validated_data["content"],
            image=validated_data["image"],
        )
        board.save()
        return board

    class Meta:
        model = Post
        fields = ["pk", "author","board_type", "title", "content", "image"]    