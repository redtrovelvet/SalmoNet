from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/authors/", views.get_authors, name="get_authors"),
    path("api/authors/<uuid:author_id>/", views.get_author, name="get_author"),
    path("api/authors/<uuid:author_id>/update/", views.update_author, name="update_author"),
    path("api/authors/<uuid:author_id>/create/", views.create_author, name="create_author"),
    path("authors/<uuid:author_id>/", views.profile, name="profile"),
    path("authors/<uuid:author_id>/edit/", views.edit_profile, name="edit_profile"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("authors/<uuid:author_id>/follow/", views.follow_author, name="follow_author"), 
    path("authors/<uuid:author_id>/unfollow/", views.unfollow_author, name="unfollow_author"),  
    path("authors/", views.all_authors, name="all_authors"),
]