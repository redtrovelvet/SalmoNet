from rest_framework import serializers
from django.conf import settings
from .models import Author, Post

class AuthorSerializer(serializers.Serializer):
    type = serializers.CharField(default="author")
    id = serializers.SerializerMethodField()
    username = serializers.CharField(max_length=100)
    display_name = serializers.CharField(max_length=100, allow_null=True, required=False)
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
    
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'text', 'image', 'video', 'content_type', 'visibility', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate(self, attrs):
        if 'text' not in attrs and 'image' not in attrs and 'video' not in attrs:
            raise serializers.ValidationError("A post must contain text, image, or video.")
        return attrs
