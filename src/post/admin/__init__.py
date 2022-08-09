from django.contrib import admin
from comment import CommentAdmin
from post import PostAdmin
from post.models import Comment as CommentModel, Post as PostModel

admin.site.register(CommentModel, CommentAdmin)
admin.site.register(PostModel, PostAdmin)
