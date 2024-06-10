from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class Status(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name=_('name'),
    )

    created = models.DateTimeField(
        default=timezone.now,
        verbose_name=_('created'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Status')
        verbose_name_plural = _('Statuses')
