from django.contrib import admin
from tag.models import Tag as TagPost
from .tag import TagAdmin

admin.site.register(TagPost, TagAdmin)
