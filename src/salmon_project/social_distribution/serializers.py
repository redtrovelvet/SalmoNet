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
    host = serializers.URLField()
    display_name = serializers.CharField(max_length=100, allow_null=True, required=False, default="Display Name")
    github = serializers.URLField(allow_null=True, required=False)
    profile_image = serializers.URLField(allow_null=True, required=False)
    username = serializers.CharField(max_length=100)

    def get_id(self, obj):
        """
        returns full API URL for the author
        """
        return f"{obj.fqid}"
    
    def create(self, validated_data):
        """
        create and return a new "Author" instance, given the validated data
        """
        return Author.objects.create(
            username = validated_data["username"],
            display_name = validated_data.get("display_name"),
            github = validated_data.get("github"),
            profile_image = validated_data.get("profile_image"),
            host = validated_data["host"]
        ) 
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Author` instance, given the validated data
        """
        instance.display_name = validated_data.get("display_name", instance.display_name)
        instance.github = validated_data.get("github", instance.github)
        instance.profile_image = validated_data.get("profile_image", instance.profile_image)
        instance.save()
        return instance
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        base_host = instance.host.rstrip('/')
        representation["id"] = instance.fqid
        representation["host"] = f"{instance.host}/api/"
        representation["page"] = f"{base_host}/authors/{instance.id}"
        representation.pop("username", None)
        return {snake_to_camel(key): value for key, value in representation.items()}

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

        # Get the host
        host = settings.BASE_URL

        # Add the fields to the representation in the correct format
        representation["author"] = AuthorSerializer(instance.author).data
        representation["id"] = instance.fqid
        representation["object"] = f"{instance.object.fqid}"
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

        # Get the host
        host = settings.BASE_URL

        representation["author"] = AuthorSerializer(instance.author).data
        representation["id"] = instance.fqid
        representation["post"] = f"{instance.post.fqid}"
        representation["page"] = f"{host}/authors/{instance.post.author.id}/posts/{instance.post.id}"
        likes = CommentLike.objects.filter(object=instance.id)
        serialized_likes = CommentLikeSerializer(likes, many=True).data
        likes_data = {
            "type": "likes",
            "page": f"{host}/authors/{instance.author.id}/comments/{instance.id}",
            "id": f"{instance.fqid}/likes",
            "page_number": 1, # TODO: make this number variable
            "size": min(len(serialized_likes), 50),
            "count": len(serialized_likes),
            "src": serialized_likes
        }

        representation["likes"] = LikesListSerializer(likes_data).data
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

        # Get the host
        host = settings.BASE_URL

        # Add the fields to the representation in the correct format
        representation["author"] = AuthorSerializer(instance.author).data
        representation["id"] = instance.fqid
        representation["object"] = f"{instance.object.fqid}"
        return {snake_to_camel(key): value for key, value in representation.items()}
    
    def to_internal_value(self, data):
        data = {camel_to_snake(key): value for key, value in data.items()}
        return super().to_internal_value(data)
    
class PostSerializer(serializers.ModelSerializer):
    # TODO: might need to add more attributes like page and description to the post
    type = serializers.CharField(default="post")
    comments = CommentsListSerializer(read_only=True)
    likes = LikesListSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ["type", "id", "author", "content", "content_type", "visibility", "created_at", "updated_at", "comments", "likes"]
        read_only_fields = ["type", "id", "author", "created_at", "updated_at", "comments", "likes"]

    def validate(self, attrs):
        has_file = self.context.get("has_file", False)
        if not has_file and (not attrs.get("content")):
            raise serializers.ValidationError("A post must contain text or an uploaded file.")
        return attrs
    
    def create(self, validated_data):
        validated_data.pop("type", None)
        validated_data.pop("comments", None)
        validated_data.pop("likes", None)
        return super().create(validated_data)
    
    def get_id(self, obj):
        """
        returns full API URL for the author
        """
        return f"{obj.fqid}"
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        ct = instance.content_type
        if ct == "text/plain":
            title = "plain text post"
            description = "plain text post"
        elif ct == "text/markdown":
            title = "markdown post"
            description = "markdown post"
        elif ct in ["image/png;base64", "image/jpeg;base64", "application/base64"]:
            title = "base64 post"
            description = "base64 post"
        else:
            title = ""
            description = ""
        
        representation = {
            "type": "post",
            "title": title,
            "id": instance.fqid,
            "page": f"{instance.author.host.rstrip('/')}/authors/{instance.author.id}/posts/{instance.id}",
            "description": description,
            "contentType": instance.content_type,
            "content": instance.content,
            "author": AuthorSerializer(instance.author).data,
        }

        # Get the host
        host = settings.BASE_URL

        comments = Comment.objects.filter(post=instance.id)
        serialized_comments = CommentSerializer(comments, many=True).data
        comments_data = {
            "type": "comments",
            "page": f"{host}/authors/{instance.author.id}/posts/{instance.id}",
            "id": f"{instance.fqid}/comments",
            "page_number": 1, # TODO: make this number variable
            "size": min(len(serialized_comments), 5),
            "count": len(serialized_comments),
            "src": serialized_comments
        }
        representation["comments"] = CommentsListSerializer(comments_data).data
        likes = PostLike.objects.filter(object=instance.id)
        serialized_likes = PostLikeSerializer(likes, many=True).data
        likes_data = {
            "type": "likes",
            "page": f"{host}/authors/{instance.author.id}/posts/{instance.id}",
            "id": f"{instance.fqid}/likes",
            "page_number": 1, # TODO: make this number variable
            "size": min(len(serialized_likes), 50),
            "count": len(serialized_likes),
            "src": serialized_likes
        }
        representation["likes"] = LikesListSerializer(likes_data).data

        representation["published"] = instance.created_at.isoformat()
        representation["visibility"] = instance.visibility

        return {snake_to_camel(key): value for key, value in representation.items()}