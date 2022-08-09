from django.db import models
from django.utils.translation import gettext


class GeneralModel(models.Model):
    created_at = models.DateTimeField(
        verbose_name=gettext('Created Time'),
        auto_now_add=True
    #     برای زمانی که رکوردی به دیتابیس اضافه میشه بیاد تاریخ همون لحظه رو بزنه برامون
    )
    updated_at = models.DateTimeField(
        verbose_name=gettext('Updated Time'),
        auto_now=True
    )

    class Meta:
        """
        جلوگیری از مایگریت شدن
        """
        abstract = True
