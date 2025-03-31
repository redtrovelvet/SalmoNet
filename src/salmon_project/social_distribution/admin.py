from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(PostLike)
admin.site.register(Comment)
admin.site.register(CommentLike)
admin.site.register(FollowRequest)
admin.site.register(FeedBlock)
admin.site.register(RemoteNode)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('username', 'display_name', 'is_approved', 'host')
    list_filter = ('is_approved', 'host')
    search_fields = ('username', 'display_name')
    ordering = ('username',)
    readonly_fields = ('id', 'fqid')

    fieldsets = (
        (None, {
            'fields': ('user', 'id', 'username', 'display_name', 'is_approved', 'fqid')  # added fqid here
        }),
        ('Profile Information', {
            'fields': ('github', 'profile_image', 'page')
        }),
        ('Network Information', {
            'fields': ('host', 'following')
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('user',)
        return self.readonly_fields

    def approve_authors(self, request, queryset):
        queryset.update(is_approved=True)
    approve_authors.short_description = "Approve selected authors"

    def unapprove_authors(self, request, queryset):
        queryset.update(is_approved=False)
    unapprove_authors.short_description = "Unapprove selected authors"
    
admin.site.register(Author, AuthorAdmin)

# show non editable fields in post
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'created_at', 'updated_at')
    list_filter = ('author',)
    search_fields = ('content',)
    ordering = ('-created_at',)
    readonly_fields = ('id', 'fqid', 'created_at', 'updated_at')

    fieldsets = (
        (None, {
            'fields': ('author', 'id', 'fqid')
        }),
        ('Post Content', {
            'fields': ('content',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('author',)
        return self.readonly_fields
admin.site.register(Post, PostAdmin)