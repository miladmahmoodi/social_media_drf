from django.db import models
from utils import GeneralModel
from django.contrib.auth import get_user_model
from django.utils.translation import gettext
import uuid, os

User = get_user_model()


def get_file_path(instance, file_name):
    ext = file_name.split('.')[-1]
    file_name = '{}.{}'.format(uuid.uuid4(), ext)
    return os.path.join(f'user/{instance.user.id}/profile_image/', file_name)


class ProfileImage(GeneralModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=gettext('User'),
        related_name='profile_images',
        null=True,
    )
    image = models.ImageField(
        verbose_name=gettext('Image'),
        upload_to=get_file_path,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.user} image'
