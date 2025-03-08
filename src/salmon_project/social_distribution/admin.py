from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(PostLike)
admin.site.register(Comment)
admin.site.register(CommentLike)
admin.site.register(FollowRequest)
admin.site.register(FeedBlock)