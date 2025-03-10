from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Post)
admin.site.register(PostLike)
admin.site.register(Comment)
admin.site.register(CommentLike)
admin.site.register(FollowRequest)
admin.site.register(FeedBlock)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('username', 'display_name', 'is_approved')
    list_filter = ('is_approved',)
    search_fields = ('username', 'display_name')
    actions = ['approve_authors', 'unapprove_authors']

    def approve_authors(self, request, queryset):
        queryset.update(is_approved=True)
    approve_authors.short_description = "Approve selected authors"

    def unapprove_authors(self, request, queryset):
        queryset.update(is_approved=False)
    unapprove_authors.short_description = "Unapprove selected authors"