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
    path("authors/<uuid:author_id>/unfollow/", views.unfollow_author, name="unfollow_author"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("authors/", views.all_authors, name="all_authors"),
    path("authors/<uuid:author_id>/follow/", views.send_follow_request, name="send_follow_request"),
    path("follow_request/<int:request_id>/approve/", views.approve_follow_request, name="approve_follow_request"),  
    path("follow_request/<int:request_id>/deny/", views.deny_follow_request, name="deny_follow_request"),  
    path("follow_requests/", views.view_follow_requests, name="view_follow_requests"), 
    path("follow_requests/<int:request_id>/approve/", views.approve_follow_request, name="approve_follow_request"),
    path("follow_requests/<int:request_id>/deny/", views.deny_follow_request, name="deny_follow_request"),
]

