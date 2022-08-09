from django.db import models
from utils import GeneralModel, file_path, base_errors
from django.utils.translation import gettext
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
import os, uuid


def get_file_path(instance, file_name):
    ext = file_name.split('.')[-1]
    file_name = '{}.{}'.format(uuid.uuid4(), ext)
    return os.path.join(f'user/{instance.user.id}/cover/', file_name)


class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None):
        if not email:
            raise ValueError(base_errors.BaseErrors.user_must_have_email)
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staff_user(self, email=None, password=None):
        if not email:
            raise ValueError(base_errors.BaseErrors.user_must_have_email)
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None):
        if not email:
            raise ValueError(base_errors.BaseErrors.user_must_have_email)
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, GeneralModel):
    username = models.CharField(
        verbose_name=gettext('Username'),
        unique=True,
        max_length=128,
        null=True,
        blank=True
    )
    email = models.EmailField(
        verbose_name=gettext('Email'),
        unique=True,
        max_length=256
    )
    email_verified = models.BooleanField(
        verbose_name=gettext('Email Verified'),
        default=False
    )
    main_image = models.ImageField(
        verbose_name=gettext('Main Image'),
        max_length=1024,
        null=True,
        blank=True,
        unique=True
    )
    cover = models.ImageField(
        verbose_name=gettext('Cover'),
        # upload_to=file_path.get_file_path('cover'),
        upload_to=get_file_path,
        max_length=128,
        null=True,
        blank=True
    )
    description = models.TextField(
        verbose_name=gettext('Description'),
        null=True,
        blank=True,
        default=None
    )
    follow = models.ManyToManyField(
        'user.User',
        verbose_name=gettext('Follow')
    )
    follower_count = models.PositiveIntegerField(
        verbose_name=gettext('Follower Count'),
        default=0
    )
    following_count = models.PositiveIntegerField(
        verbose_name=gettext('Following Count'),
        default=0
    )
    post_count = models.PositiveIntegerField(
        verbose_name=gettext('Post Count'),
        default=0
    )
    staff = models.BooleanField(
        verbose_name=gettext('Staff'),
        default=False
    )
    is_superuser = models.BooleanField(
        verbose_name=gettext('Admin'),
        default=False
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = UserManager()

    def __str__(self):
        return f'{self.email}'

    def is_staff(self):
        return self.staff

    def has_perm(self, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_lable):
        return self.is_superuser
