from django.db import models
from utils import GeneralModel
from django.contrib.auth import get_user_model
from django.utils.translation import gettext

import os
import uuid

User = get_user_model()


def get_file_path(instance, file_name):
    ext = file_name.split('.')[-1]
    file_name = '%s.%s' % (uuid.uuid4(), ext)
    os.path.join(f'user/{instance.user.id}/post/', file_name)


class Post(GeneralModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=gettext('Author'),
        related_name='posts',
        null=True
    )
    caption = models.TextField(
        verbose_name=gettext('Caption')
    )
    file = models.ImageField(
        verbose_name=gettext('Media'),
        upload_to=get_file_path,
        max_length=128,
    )
    tag = models.ManyToManyField(
        'tag.tag',
        verbose_name=gettext('Tag'),
        null=True,
        blank=True
    )
    like = models.ManyToManyField(
        User,
        verbose_name=gettext('Like'),
        related_name='likers',
        blank=True,
    )
    feed = models.ManyToManyField(
        User,
        verbose_name=gettext('Feed'),
        blank=True,
    )
    reshare = models.ForeignKey(
        'post.Post',
        on_delete=models.CASCADE,
        verbose_name=gettext('Feed'),
        related_name='reshares',
        null=True,
        blank=True,
        default=None
    )
    reshare_count = models.PositiveIntegerField(
        verbose_name=gettext('Total Count'),
        default=0
    )
    comment_count = models.PositiveIntegerField(
        verbose_name=gettext('Total Comment'),
        default=0
    )
    like_count = models.PositiveIntegerField(
        verbose_name=gettext('Total Like'),
        default=0
    )

    def __str__(self):
        return f'{self.user} - {self.caption[:10]}'