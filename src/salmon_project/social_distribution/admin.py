from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Post)
admin.site.register(PostLike)
admin.site.register(Comment)
admin.site.register(CommentLike)
admin.site.register(FollowRequest)
admin.site.register(FeedBlock)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('username', 'display_name', 'is_approved', 'host')
    list_filter = ('is_approved', 'host')
    search_fields = ('username', 'display_name')
    ordering = ('username',)
    readonly_fields = ('id',)

    fieldsets = (
        (None, {
            'fields': ('user', 'id', 'username', 'display_name', 'is_approved')
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