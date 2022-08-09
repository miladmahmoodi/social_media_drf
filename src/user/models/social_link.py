from django.db import models
from utils import GeneralModel
from django.contrib.auth import get_user_model
from django.utils.translation import gettext


User = get_user_model()


class SocialLink(GeneralModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=gettext('User Social Media'),
        related_name='social_links',
    )
    name = models.CharField(
        verbose_name=gettext('Social Media Name'),
        unique=True,
        max_length=128,
    )
    url = models.CharField(
        verbose_name=gettext('Social Media Url'),
    )


    def __str__(self):
        return self.name