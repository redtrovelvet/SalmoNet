from django.shortcuts import render, get_object_or_404, redirect
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

def edit_profile(request, author_id):
    '''
    To allow authors to edit their profile information like display name, github, and profile image
    '''
    author = get_object_or_404(Author, id=author_id)
    if request.method == "POST":
        author.display_name = request.POST.get("display_name", author.display_name)
        author.github = request.POST.get("github", author.github)

        if "profile_image" in request.FILES:
            author.profile_image = request.FILES["profile_image"]
        
        author.save()
        return redirect("profile", author_id=author.id)
    return render(request, "social_distribution/edit_profile.html", {"author": author})

def logout(request):
    '''
    Logs the author out and returns to homepage (index.html)
    '''
    logout(request)
    return redirect("index")

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
