from django.db import models
from django.utils.translation import gettext


class GeneralModel(models.Model):
    """
    log of every query received from a client,
    """
    created_at = models.DateTimeField(
        verbose_name=gettext('Created Time'),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=gettext('Updated Time'),
        auto_now=True
    )

    class Meta:
        """
        ignore migration with use abstract
        """
        abstract = True
