#references:
#https://www.pythontutorial.net/django-tutorial/django-registration/

from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Author, Post
from .serializers import AuthorSerializer
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        author = get_object_or_404(Author, username=request.user.username)
        followed_authors = author.following.all()

        posts = Post.objects.filter(author__in=followed_authors, visibility__in=["PUBLIC", "FRIENDS", "UNLISTED"]).exclude(visibility="DELETED").order_by("-created_at")

        public_posts = Post.objects.filter(visibility="PUBLIC").exclude(visibility="DELETED").order_by("-created_at")
        posts = (posts | public_posts).distinct().order_by("-created_at")
    else:
        posts = Post.objects.filter(visibility="PUBLIC").exclude(visibility="DELETED").order_by("-created_at")

    return render(request, "social_distribution/index.html", {"posts": posts})

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

def register(request):
    '''
    To handle registration of new users and will create an Auther profile
    '''
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Author.objects.create(username=user.username)
            login(request, user)
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, "social_distribution/register.html", {"form": form})

def login_view(request):
    '''
    To handle user login
    '''
    if request.method == "POST":
        form = AuthenticationForm(data=request.data)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")
    else:
        form = AuthenticationForm()
    return render(request, "social_distribution/login.html", {"form": form})

def logout_view(request):
    '''
    Logs the author out and returns to homepage (index.html)
    '''
    logout(request)
    return redirect("index")

@api_view(["GET"])
def get_authors(request):
    '''
    API: returns all authors in local node
    '''
    local_authors = Author.objects.filter(host=settings.BASE_URL)
    serializer = AuthorSerializer(local_authors, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_author(request, author_id):
    '''
    API: returns specific author profiile
    '''
    author = get_object_or_404(Author, id=author_id)
    serializer = AuthorSerializer(author)
    return Response(serializer.data)


@api_view(["POST"])
def create_author(request, author_id):
    '''
    API: creates a new author 
    '''
    serializer = AuthorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(status=400, data=serializer.errors)

@api_view(["POST"])
def update_author(request, author_id):
    '''
    API: updates an author's profile
    ''' 
    author = get_object_or_404(Author, id=author_id)
    serializer = AuthorSerializer(author, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=400, data=serializer.errors)



