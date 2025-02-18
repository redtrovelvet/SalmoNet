from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Author, Post
from .serializers import AuthorSerializer
from django.conf import settings
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "social_distribution/index.html")

def profile(request, author_id):
    '''
    renders the profile page for an author
    '''
    author = get_object_or_404(Author, id=author_id)
    posts = Post.objects.filter(author=author, visibility="PUBLIC").order_by("-created_at")
    return render(request, "social_distribution/profile.html", {"author": author, "posts": posts})

@api_view(["GET"])
def get_authors(request):
    '''
    returns all authors in local node
    '''
    local_authors = Author.objects.filter(host=settings.BASE_URL)
    serializer = AuthorSerializer(local_authors, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_author(request, author_id):
    '''
    returns specific author profiile
    '''
    author = get_object_or_404(Author, id=author_id)
    serializer = AuthorSerializer(author)
    return Response(serializer.data)

@api_view(["POST"])
def update_author(request, author_id):
    '''
    updates an author's profile
    ''' 
    author = get_object_or_404(Author, id=author_id)
    serializer = AuthorSerializer(author, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=400, data=serializer.errors)
