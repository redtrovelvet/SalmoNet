from django.urls import path
from . import views

urlpatterns = [
    # User-Facing Views
    path("", views.index, name="index"),
    path("authors/<uuid:author_id>/", views.profile, name="profile"),
    path("authors/<uuid:author_id>/edit/", views.edit_profile, name="edit_profile"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("authors/<uuid:author_id>/posts/<uuid:post_id>/edit/", views.edit_post, name="edit_post"),       
    path("authors/<uuid:author_id>/posts/<uuid:post_id>/delete/", views.delete_post_local, name="delete_post_local"),


    # Extra User-Facing Views (from following/friend branch)
    path("authors/", views.all_authors, name="all_authors"),
    path("authors/<uuid:author_id>/follow/", views.send_follow_request, name="send_follow_request"),
    path("authors/<uuid:author_id>/unfollow/", views.unfollow_author, name="unfollow_author"),
    path("follow_requests/", views.view_follow_requests, name="view_follow_requests"),
    path("follow_requests/<int:request_id>/approve/", views.approve_follow_request, name="approve_follow_request"),
    path("follow_requests/<int:request_id>/deny/", views.deny_follow_request, name="deny_follow_request"),
    path("profile/followers/", views.view_followers, name="view_followers"),
    path("profile/following/", views.view_following, name="view_following"),
    path("profile/friends/", views.view_friends, name="view_friends"),

    # API Endpoints
    path("api/authors/", views.get_authors, name="get_authors"),
    path("api/authors/<uuid:author_id>/", views.get_author, name="get_author"),
    path("api/authors/<uuid:author_id>/update/", views.update_author, name="update_author"),
    path("api/authors/create/", views.create_author, name="create_author"),
    path("api/authors/<uuid:author_id>/posts/<uuid:post_id>/", views.get_post, name="get_post"),
    path("api/posts/<uuid:post_fqid>/", views.get_post_by_fqid, name="get_post_by_fqid"),
    path("api/authors/<uuid:author_id>/posts/", views.get_author_posts, name="get_author_posts"),
    path("api/authors/<uuid:author_id>/posts/create/", views.create_post, name="create_post"),
    path("api/authors/<uuid:author_id>/posts/<uuid:post_id>/image/", views.get_post_image, name="get_post_image"),
    path("api/authors/<uuid:author_id>/posts/<uuid:post_id>/update/", views.update_post, name="update_post"),
    path("api/authors/<uuid:author_id>/posts/<uuid:post_id>/delete/", views.delete_post, name="delete_post"),
]
