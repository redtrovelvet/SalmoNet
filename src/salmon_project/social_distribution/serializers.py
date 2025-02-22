from rest_framework import serializers
from django.conf import settings
from .models import Author, Post, Comment, CommentLike, PostLike
import uuid
import re

# The following function and the use of it in the below serializers from Microsoft Copilot, "how do I change snake case to camel case to representation and convert it back for create", 2025-02-21
def snake_to_camel(snake_str):
        components = snake_str.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])

# The following function and the use of it in the below serializers from Microsoft Copilot, "how do I change snake case to camel case to representation and convert it back for create", 2025-02-21
def camel_to_snake(camel_str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()

class AuthorSerializer(serializers.Serializer):
    type = serializers.CharField(default="author")
    id = serializers.SerializerMethodField()
    username = serializers.CharField(max_length=100)
    display_name = serializers.CharField(max_length=100, allow_null=True, required=False, default="Display Name")
    github = serializers.URLField(allow_null=True, required=False)
    profile_image = serializers.URLField(allow_null=True, required=False)
    host = serializers.URLField()

    def get_id(self, obj):
        '''
        returns full API URL for the author
        '''
        return f"{obj.host}/api/authors/{obj.id}"
    
    def create(self, validated_data):
        '''
        create and return a new 'Author' instance, given the validated data
        '''
        return Author.objects.create(
            username = validated_data["username"],
            display_name = validated_data.get("display_name"),
            github = validated_data.get("github"),
            profile_image = validated_data.get("profile_image"),
            host = validated_data["host"]
        ) 
    
    def update(self, instance, validated_data):
        '''
        Update and return an existing `Author` instance, given the validated data
        '''
        instance.display_name = validated_data.get("display_name", instance.display_name)
        instance.github = validated_data.get("github", instance.github)
        instance.profile_image = validated_data.get("profile_image", instance.profile_image)
        instance.save()
        return instance

class CommentLikeSerializer(serializers.Serializer):
    type = serializers.CharField(default="like")
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    published = serializers.DateTimeField(required=False)
    id = serializers.UUIDField(required=False)
    object = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all())

    def create(self, validated_data):
        return CommentLike.objects.create(
            author = validated_data["author"],
            object = validated_data["object"]
        )
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author'] = AuthorSerializer(instance.author).data
        return {snake_to_camel(key): value for key, value in representation.items()}
    
    def to_internal_value(self, data):
        data = {camel_to_snake(key): value for key, value in data.items()}
        return super().to_internal_value(data)
    
class LikesListSerializer(serializers.Serializer):
    type = serializers.CharField(default="likes")
    page = serializers.CharField(max_length=256)
    id = serializers.CharField(max_length=256)
    page_number = serializers.IntegerField()
    size = serializers.IntegerField()
    count = serializers.IntegerField()
    src = serializers.ListField()

class CommentSerializer(serializers.Serializer):
    type = serializers.CharField(default="comment")
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    comment = serializers.CharField()
    content_type = serializers.CharField()
    published = serializers.DateTimeField(required=False)
    id = serializers.UUIDField(required=False)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    likes = LikesListSerializer(many=True, read_only=True)

    def create(self, validated_data):
        return Comment.objects.create(
            author = validated_data["author"],
            comment = validated_data["comment"],
            content_type = validated_data.get("content_type"),
            post = validated_data["post"]
        )
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author'] = AuthorSerializer(instance.author).data
        likes = CommentLike.objects.filter(object=instance.id)
        serialized_likes = CommentLikeSerializer(likes, many=True).data
        likes_data = {
            "type": "likes",
            "page": instance.post.id,
            "id": str(instance.id) + "/likes",
            "page_number": 1, # TODO: make this number variable
            "size": min(len(serialized_likes), 50),
            "count": len(serialized_likes),
            "src": serialized_likes
        }

        representation['likes'] = LikesListSerializer(likes_data).data
        return {snake_to_camel(key): value for key, value in representation.items()}

    def to_internal_value(self, data):
        data = {camel_to_snake(key): value for key, value in data.items()}
        return super().to_internal_value(data)
    
class CommentsListSerializer(serializers.Serializer):
    type = serializers.CharField(default="comments")
    page = serializers.CharField(max_length=256)
    id = serializers.CharField(max_length=256)
    page_number = serializers.IntegerField()
    size = serializers.IntegerField()
    count = serializers.IntegerField()
    src = serializers.ListField()
    
class PostLikeSerializer(serializers.Serializer):
    type = serializers.CharField(default="like")
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    published = serializers.DateTimeField(required=False)
    id = serializers.UUIDField(required=False)
    object = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    
    def create(self, validated_data):
        return PostLike.objects.create(
            author = validated_data["author"],
            object = validated_data["object"]
        )
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author'] = AuthorSerializer(instance.author).data
        return {snake_to_camel(key): value for key, value in representation.items()}
    
    def to_internal_value(self, data):
        data = {camel_to_snake(key): value for key, value in data.items()}
        return super().to_internal_value(data)
    
class PostSerializer(serializers.ModelSerializer):
    # TODO: might need to add more attributes like page and description to the post
    type = serializers.CharField(default="post")
    comments = CommentsListSerializer(many=True, read_only=True)
    likes = LikesListSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['type', 'id', 'author', 'text', 'image', 'video', 'content_type', 'visibility', 'created_at', 'updated_at', 'comments', 'likes']
        read_only_fields = ['type', 'id', 'author', 'created_at', 'updated_at', 'comments', 'likes']

    def validate(self, attrs):
        if 'text' not in attrs and 'image' not in attrs and 'video' not in attrs:
            raise serializers.ValidationError("A post must contain text, image, or video.")
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('type', None)
        validated_data.pop('comments', None)
        validated_data.pop('likes', None)
        return super().create(validated_data)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["type"] = "post"
        representation['author'] = AuthorSerializer(instance.author).data
        comments = Comment.objects.filter(post=instance.id)
        serialized_comments = CommentSerializer(comments, many=True).data
        comments_data = {
            "type": "comments",
            "page": instance.id,
            "id": str(instance.id) + "/comments",
            "page_number": 1, # TODO: make this number variable
            "size": min(len(serialized_comments), 50),
            "count": len(serialized_comments),
            "src": serialized_comments
        }
        representation['comments'] = CommentsListSerializer(comments_data).data
        likes = PostLike.objects.filter(object=instance.id)
        serialized_likes = PostLikeSerializer(likes, many=True).data
        likes_data = {
            "type": "likes",
            "page": instance.id,
            "id": str(instance.id) + "/likes",
            "page_number": 1, # TODO: make this number variable
            "size": min(len(serialized_likes), 50),
            "count": len(serialized_likes),
            "src": serialized_likes
        }
        representation['likes'] = LikesListSerializer(likes_data).data
        return {snake_to_camel(key): value for key, value in representation.items()}