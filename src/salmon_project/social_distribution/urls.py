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
    path("authors/<uuid:author_id>/posts/<uuid:post_id>/view/", views.view_post, name="view_post"),
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
    path("admin/approval/", views.admin_approval, name="admin_approval"),
    path("admin/approve/<uuid:author_id>/", views.approve_author, name="approve_author"),
    path("admin/reject/<uuid:author_id>/", views.reject_author, name="reject_author"),
    
    # Authors API
    path("api/authors/", views.get_authors, name="get_authors"),

    # Single Author API
    path("api/authors/<uuid:author_id>/", views.author_details, name="author_details"),

    # Posts API
    path("api/authors/<uuid:author_id>/posts/<uuid:post_id>/", views.get_post, name="get_post"),
    path("api/posts/<uuid:post_fqid>/", views.get_post_by_fqid, name="get_post_by_fqid"),
    path("api/authors/<uuid:author_id>/posts/", views.get_author_posts, name="get_author_posts"),
    path("api/authors/<uuid:author_id>/posts/create/", views.create_post, name="create_post"),
    path("api/authors/<uuid:author_id>/posts/<uuid:post_id>/image/", views.get_post_image, name="get_post_image"),
    path("api/authors/<uuid:author_id>/posts/<uuid:post_id>/update/", views.update_post, name="update_post"),
    path("api/authors/<uuid:author_id>/posts/<uuid:post_id>/delete/", views.delete_post, name="delete_post"),

    # Inbox API (used for follow requests in our API)
    path("api/authors/<uuid:author_id>/inbox/", views.inbox, name="inbox"),

    # Comments API
    path("api/authors/<uuid:author_id>/posts/<uuid:post_id>/comments/", views.get_comments, name="get_author_comments"),
    path("api/posts/<uuid:post_id>/comments/", views.get_comments, name="get_comments"),
    path("api/authors/<uuid:author_id>/post/<uuid:post_id>/comments/<uuid:comment_id>/", views.get_comment, name="get_remote_comment"),

    # Commented API
    path("api/authors/<uuid:author_id>/commented/", views.commented, name="commented"),
    path("api/authors/<uuid:author_id>/commented/<uuid:comment_id>/", views.get_comment, name="get_author_comment"),
    path("api/commented/<uuid:comment_id>/", views.get_comment, name="get_comment"),

    # Likes API
    path("api/authors/<uuid:author_id>/posts/<uuid:post_id>/likes/", views.get_post_likes, name="get_post_likes"),
    path("api/posts/<uuid:post_id>/likes/", views.get_post_likes, name="get_likes"),
    path("api/authors/<uuid:author_id>/posts/<uuid:post_id>/comments/<uuid:comment_id>/likes/", views.get_comment_likes, name="get_comment_likes"),

    # Liked API
    path("api/authors/<uuid:author_id>/liked/", views.get_author_liked, name="get_author_liked"),
    path("api/authors/<uuid:author_id>/liked/<uuid:like_id>/", views.get_like, name="get_author_like"),
    path("api/liked/<uuid:like_id>/", views.get_like, name="get_like"),

    # Extra APIs to like posts and comments (not in the spec)
    path("api/authors/<uuid:author_id>/posts/<uuid:post_id>/liked/", views.like_post, name="like_post"),
    path("api/authors/<uuid:author_id>/comments/<uuid:comment_id>/liked/", views.like_comment, name="like_comment"),

   
    path("api/authors/<uuid:author_id>/followers/", views.modify_follower_api, name="get_followers_api"),
    path("api/authors/<uuid:author_id>/followers/<str:foreign_author_encoded>/", views.modify_follower_api, name="modify_follower_api"),
    
    path("api/authors/<uuid:author_id>/followrequest/", views.api_send_follow_request, name="api_send_follow_request"),
]
