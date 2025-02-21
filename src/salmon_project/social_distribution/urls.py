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
    path("authors/<uuid:author_id>/posts/<uuid:post_id>/delete/", views.delete_post, name="delete_post"),

    
    # API Endpoints
    path("api/authors/", views.get_authors, name="get_authors"),
    path("api/authors/<uuid:author_id>/", views.get_author, name="get_author"),
    path("api/authors/<uuid:author_id>/update/", views.update_author, name="update_author"),
    path("api/authors/create/", views.create_author, name="create_author"),
    path('api/authors/<uuid:author_id>/posts/<uuid:post_id>/', views.get_post, name='get_post'),
    #path('api/authors/<uuid:author_id>/posts/<uuid:post_id>/delete/', views.delete_post, name='delete_post'),
    #path('api/authors/<uuid:author_id>/posts/<uuid:post_id>/edit/', views.edit_post, name='edit_post'),
    path('api/posts/<uuid:post_fqid>/', views.get_post_by_fqid, name='get_post_by_fqid'),
    path('api/authors/<uuid:author_id>/posts/', views.get_author_posts, name='get_author_posts'),
    path('api/authors/<uuid:author_id>/posts/create/', views.create_post, name='create_post'),
    path('api/authors/<uuid:author_id>/posts/<uuid:post_id>/image/', views.get_post_image, name='get_post_image'),
]