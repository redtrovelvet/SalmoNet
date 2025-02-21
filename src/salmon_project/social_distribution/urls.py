from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/authors/", views.get_authors, name="get_authors"),
    path("api/authors/<uuid:author_id>/", views.get_author, name="get_author"),
    path("api/authors/<uuid:author_id>/update/", views.update_author, name="update_author"),
    path("api/authors/create/", views.create_author, name="create_author"),
    path("api/authors/<uuid:author_id>/inbox/", views.inbox, name="inbox"),
    path("api/authors/<uuid:author_id>/posts/<uuid:post_id>/comments/", views.get_comments, name="get_author_comments"),
    path("api/posts/<uuid:post_id>/comments/", views.get_comments, name="get_comments"),
    path("api/authors/<uuid:author_id>/commented/", views.commented, name="commented"),
    path("api/authors/<uuid:author_id>/commented/<uuid:comment_id>/", views.get_comment, name="get_author_comment"),
    path("api/commented/<uuid:comment_id>/", views.get_comment, name="get_comment"),
    path("api/authors/<uuid:author_id>/posts/<uuid:post_id>/likes/", views.get_post_likes, name="get_post_likes"),
    path("api/posts/<uuid:post_id>/likes/", views.get_post_likes, name="get_likes"),
    path("api/authors/<uuid:author_id>/posts/<uuid:post_id>/comments/<uuid:comment_id>/likes/", views.get_comment_likes, name="get_comment_likes"),
    path("api/authors/<uuid:author_id>/liked/", views.get_author_liked, name="get_author_liked"),
    path("api/authors/<uuid:author_id>/liked/<uuid:like_id>}/", views.get_like, name="get_author_like"),
    path("api/liked/<uuid:like_id>/", views.get_like, name="get_like"),
    path("authors/<uuid:author_id>/", views.profile, name="profile"),
    path("authors/<uuid:author_id>/edit/", views.edit_profile, name="edit_profile"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login")
]