from django.db import models
from utils import GeneralModel
from django.contrib.auth import get_user_model
from django.utils.translation import gettext

User = get_user_model()


class ActivationCode(GeneralModel):
    TYPE_CHOICES = (
        ('Register', 'REGISTER'),
        ('Forget', 'FORGET')
    )


    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=gettext('Activation Code')
    )
    type = models.CharField(
        verbose_name=gettext('Type'),
        max_length=8,
        choices=TYPE_CHOICES
    )
    code = models.CharField(
        max_length=32,
        unique=True,
        verbose_name=gettext('Code')
    )
    retry = models.PositiveSmallIntegerField(
        verbose_name=gettext('Retry'),
        default=0
    )
    used = models.BooleanField(
        verbose_name='Used',
        default=False
    )

    def __str__(self):
        return f'{self.user} - {self.code}'
