from django.db import models
from utils import GeneralModel
from django.contrib.auth import get_user_model
from django.utils.translation import gettext

User = get_user_model()


class Comment(GeneralModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=gettext('Author'),
        related_name='comments',
    )
    post = models.ForeignKey(
        'post.Post',
        on_delete=models.CASCADE,
        related_name='Comments'
    )
    text = models.TextField(
        verbose_name=gettext('Text')
    )
    parent = models.ForeignKey(
        'comment.Comment',
        verbose_name=gettext('Parent'),
        on_delete=models.CASCADE,
        related_name='replies',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.user} - {self.post} - {self.text[:10]}'
