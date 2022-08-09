from django.db import models
from utils import GeneralModel
from django.contrib.auth import get_user_model
from django.utils.translation import gettext


User = get_user_model()


class Tag(GeneralModel):
    creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name=gettext('Creator'),
        related_name='tags'
    )
    name = models.CharField(
        verbose_name=gettext('Name'),
        unique=True,
        max_length=128
    )

    def __str__(self):
        return f'{self.creator} - {self.name}'
