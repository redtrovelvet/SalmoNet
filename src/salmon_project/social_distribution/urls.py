from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/authors/", views.get_authors, name="get_authors"),
    path("api/authors/<uuid:author_id>/", views.get_author, name="get_author"),
    path("api/authors/<uuid:author_id>/update/", views.update_author, name="update_author"),
    path("api/authors/create/", views.create_author, name="create_author"),

    # Inbox API
    path("api/authors/<uuid:author_id>/inbox/", views.inbox, name="inbox"),

    # Comments API
    path("api/authors/<uuid:author_id>/posts/<uuid:post_id>/comments/", views.get_comments, name="get_author_comments"),
    path("api/posts/<uuid:post_id>/comments/", views.get_comments, name="get_comments"),
    path("api/authors/<uuid:author_id>/post/<uuid:post_id>/comments/<uuid:comment_id>/", views.get_comment, name="get_remote_comment"), # discrepency on whether it should be comment or comments in the specifcation, {REMOTE_COMMENT_FQID}

    # Commented API
    path("api/authors/<uuid:author_id>/commented/", views.commented, name="get_commented"), # single url for {AUTHOR_SERIAL} and {AUTHOR_FQID}
    path("api/authors/<uuid:author_id>/commented/<uuid:comment_id>/", views.get_comment, name="get_author_comment"),
    path("api/commented/<uuid:comment_id>/", views.get_comment, name="get_comment"),

    # Likes API
    path("api/authors/<uuid:author_id>/posts/<uuid:post_id>/likes/", views.get_post_likes, name="get_post_likes"),
    path("api/posts/<uuid:post_id>/likes/", views.get_post_likes, name="get_likes"),
    path("api/authors/<uuid:author_id>/posts/<uuid:post_id>/comments/<uuid:comment_id>/likes/", views.get_comment_likes, name="get_comment_likes"),

    # Liked API
    path("api/authors/<uuid:author_id>/liked/", views.get_author_liked, name="get_author_liked"), # single url for {AUTHOR_SERIAL} and {AUTHOR_FQID}
    path("api/authors/<uuid:author_id>/liked/<uuid:like_id>}/", views.get_like, name="get_author_like"),
    path("api/liked/<uuid:like_id>/", views.get_like, name="get_like"),

    path("authors/<uuid:author_id>/", views.profile, name="profile"),
    path("authors/<uuid:author_id>/edit/", views.edit_profile, name="edit_profile"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login")
]