from django.db import models
import uuid
from django.conf import settings

class Author(models.Model):
    """
    An author who can create posts and comments and follow other authors
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100, unique=True)
    following = models.ManyToManyField('self', symmetrical=False)
    display_name = models.CharField(max_length=100, unique=True, default="Display Name")
    github = models.URLField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='images/', null=True, blank=True)
    page = models.URLField(null=True, blank=True)
    host = models.URLField(default=settings.BASE_URL)

    def __str__(self):
        return self.username
    
class Post(models.Model):
    """
    A post by an author with text and/or an image
    """
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Visibility options for a post
    VISIBILITY_CHOICES = [
        ('PUBLIC', 'Public'),
        ('UNLISTED', 'Unlisted'),
        ('FRIENDS', 'Friends'),
        ('DELETED', 'Deleted'),
    ]
    visibility = models.CharField(choices=VISIBILITY_CHOICES, default='PUBLIC', max_length=100)

class PostLike(models.Model):
    """
    A like on a post by an author
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # Ensure that a user can only like a post once
    # https://docs.djangoproject.com/en/5.1/ref/models/options/#unique-together
    class Meta:
        unique_together = ['post', 'author']

class Comment(models.Model):
    """
    A comment on a post by an author
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class CommentLike(models.Model):
    """
    A like on a comment by an author
    """
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # Ensure that a user can only like a comment once
    # https://docs.djangoproject.com/en/5.1/ref/models/options/#unique-together
    class Meta:
        unique_together = ['comment', 'author']