from django.contrib import admin
from user.models import (
    User as UserModel,
    SocialLink as SocialLinkModel,
    ProfileImage as ProfileImageModel,
    ActivationCode as ActivationCodeModel
)
from .user import UserAdmin
from .social_link import SocialLinkAdmin
from .profile_image import ProfileImageAdmin
from .activation_code import ActivationCodeAdmin

admin.site.register(UserModel, UserAdmin)
admin.site.register(SocialLinkModel, SocialLinkAdmin)
admin.site.register(ProfileImageModel, ProfileImageAdmin)
admin.site.register(ActivationCodeModel, ActivationCodeAdmin)
