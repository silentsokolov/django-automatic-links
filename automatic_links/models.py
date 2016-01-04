# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

TARGET_BLANK = '_blank'
TARGET_SELF = '_self'
TARGET_PARENT = '_parent'
TARGET_TOP = '_top'

TARGET_CHOICES = (
    (TARGET_BLANK, '_blank'),
    (TARGET_SELF, '_self'),
    (TARGET_PARENT, '_parent'),
    (TARGET_TOP, '_top'),
)

DEFAULT_LIMIT = getattr(settings, 'LINK_DEFAULT_LIMIT', 0)
DEFAULT_EVERY = getattr(settings, 'LINK_DEFAULT_EVERY', 1)
DEFAULT_TARGET = getattr(settings, 'LINK_DEFAULT_TARGET', '_blank')
DEFAULT_NOFOLLOW = getattr(settings, 'LINK_DEFAULT_NOFOLLOW', False)
DEFAULT_CSS_CLASS = getattr(settings, 'LINK_DEFAULT_CSS_CLASS', None)


@python_2_unicode_compatible
class AutomaticLink(models.Model):
    keyword = models.CharField(_('keyword'), max_length=255, unique=True)
    link = models.CharField(_('link'), max_length=255)
    # options
    active = models.BooleanField(_('active'), default=True)
    limit = models.IntegerField(_('limit'), default=DEFAULT_LIMIT, help_text=_('zero - disabled'))
    every = models.IntegerField(
        _('every N'),
        default=DEFAULT_EVERY,
        help_text=_('Every "3" mean that this keyword will be replaced to link in every third content item')
    )
    target = models.CharField(_('target'), max_length=10, choices=TARGET_CHOICES, default=DEFAULT_TARGET)
    nofollow = models.BooleanField(_('rel="nofollow"'), default=DEFAULT_NOFOLLOW)
    css_class = models.CharField(_('css class'), max_length=100, blank=True, null=True, default=DEFAULT_CSS_CLASS)

    class Meta:
        unique_together = (('keyword', 'link'),)
        verbose_name = _('automatic link')
        verbose_name_plural = _('automatic links')

    def __str__(self):
        return self.keyword
