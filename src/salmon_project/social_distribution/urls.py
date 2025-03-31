from django.urls import path, re_path
from . import views

urlpatterns = [
    # User-Facing Views
    path("", views.index, name="index"),
    path("authors/<uuid:author_id>/", views.profile, name="profile"),
    path("authors/<uuid:author_id>/edit/", views.edit_profile, name="edit_profile"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("authors/<uuid:author_id>/posts/<uuid:post_id>/", views.view_post, name="view_post"),
    path("authors/<uuid:author_id>/posts/<uuid:post_id>/edit/", views.edit_post, name="edit_post"),       
    path("authors/<uuid:author_id>/posts/<uuid:post_id>/delete/", views.delete_post_local, name="delete_post_local"),
    path("admin_controls/", views.admin_controls, name="admin_controls"),
    path("api/set_node_info/", views.set_node_info, name="set_node_info"),
    path("api/connect/", views.connect_node, name="connect_node"),
    path("api/add_remote_node/", views.add_remote_node, name="add_remote_node"),
    path("api/remove_connection/", views.remove_connection, name="remove_connection"),
    path("api/connect_external/", views.connect_external, name="connect_external"),

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
    path('pending_approval/', views.pending_approval, name='pending_approval'),
    
    # Authors API
    path("api/authors/", views.get_authors, name="get_authors"),
    path("api/authors", views.get_authors, name="get_authors"),

    # Single Author API
    path("api/authors/<uuid:author_id>/", views.author_details, name="author_details"),

    # Posts API
    path("api/authors/<uuid:author_id>/posts/<uuid:post_id>/", views.posts_detail, name="posts_detail"),
    path("api/authors/<uuid:author_id>/posts/", views.author_posts, name="author_posts"),
    path("api/authors/<uuid:author_id>/posts/create/", views.create_post, name="create_post"),
    path("api/authors/<uuid:author_id>/posts/<uuid:post_id>/image/", views.get_post_image, name="get_post_image"),
    re_path(r'^api/posts/(?P<post_fqid>https?.+)/image/$',views.get_postimage_by_fqid,name="get_postimage_by_fqid"),


    # Inbox API 
    re_path(r"^api/authors/(?P<author_id>[^/]+)/inbox/?$", views.inbox, name="inbox"),
  


    # Comments API
    path("api/authors/<str:author_id>/posts/<str:post_id>/comments/", views.get_comments, name="get_author_comments"),
    re_path(r'^api/posts/(?P<post_id>https?.+)/comments/$', views.get_comments, name="get_comments"),
    re_path(r'^api/authors/(?P<author_id>[0-9a-f-]+)/post/(?P<post_id>[0-9a-f-]+)/comment/(?P<comment_id>https?.+)/$',views.get_comment, name="get_remote_comment"),

    # Commented API
    path("api/authors/<str:author_id>/commented/", views.commented, name="commented"),
    re_path(r'^api/authors/(?P<author_id>https?.+)/commented/$', views.commented, name="commented_fqid"),
    path("api/authors/<str:author_id>/commented/<str:comment_id>/", views.get_comment, name="get_author_comment"),
    re_path(r'^api/commented/(?P<comment_id>https?.+)/$', views.get_comment, name="get_comment"),

    # Likes API
    path("api/authors/<str:author_id>/posts/<str:post_id>/likes/", views.get_post_likes, name="get_post_likes"),
    re_path(r'^api/posts/(?P<post_id>https?.+)/likes/$', views.get_post_likes, name="get_post_likes_fqid"),
    re_path(r'^api/authors/(?P<author_id>[0-9a-f-]+)/posts/(?P<post_id>[0-9a-f-]+)/comments/(?P<comment_id>https?.+)/likes/$', views.get_comment_likes, name="get_comment_likes"),

    # Liked API
    path("api/authors/<str:author_id>/liked/", views.get_author_liked, name="get_author_liked"),
    path("api/authors/<str:author_id>/liked/<str:like_id>/", views.get_like, name="get_author_like"),
    re_path(r'^api/authors/(?P<author_id>https?.+)/liked/$', views.get_author_liked, name="get_author_liked_fqid"),
    re_path(r'^api/liked/(?P<like_id>https?.+)/$', views.get_like, name="get_like"),

    # Extra APIs to like posts and comments (not in the spec)
    path("api/authors/<uuid:author_id>/posts/<uuid:post_id>/liked/", views.like_post, name="like_post"),
    path("api/authors/<uuid:author_id>/comments/<uuid:comment_id>/liked/", views.like_comment, name="like_comment"),

   
    path("api/authors/<uuid:author_id>/followers/", views.get_followers_api, name="get_followers_api"),
    re_path(r'^api/authors/(?P<author_id>[0-9a-f-]+)/followers/(?P<foreign_author_encoded>https?.+)/$', views.modify_follower_api, name="modify_follower_api"),
    path("api/authors/<uuid:author_id>/followrequest/", views.api_send_follow_request, name="api_send_follow_request"),
    path('search_authors/', views.search_authors, name='search_authors'),
    #---DO NOT CHANGE POSTITION OF THIS OR ELSE IT MESSES UP THE CODE PLEASE MAKE SURE THIS PATH IS ALWAYS THE LAST PATH---#
    re_path(r'^api/posts/(?P<post_fqid>https?.+)/$', views.get_post_by_fqid, name="get_post_by_fqid"),
    #<BEGIN GENERATED model='gpt-4' date=2025-03-23 prompt: when i use fqid, the url path doesnt work becuase im using str:author_fqid, but when i use path:author_fqid it overrides the path of other urls, what do id?>
    re_path(r'^api/authors/(?P<author_fqid>https?.+)/$', views.fqid_author_details, name="fqid_author_details"),
    #<END GENERATED></END>.
]
