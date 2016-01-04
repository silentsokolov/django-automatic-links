# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import AutomaticLink


class AdminAutomaticLink(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('keyword', 'link')
        }),
        (_('Option'), {
            'fields': ('active', 'limit', 'every', ('target', 'nofollow', 'css_class'))
        })
    )

    list_display = ('active', 'keyword', 'link')
    list_display_links = ('keyword', 'link')
    list_filter = ('active',)
    search_fields = ('keyword',)


admin.site.register(AutomaticLink, AdminAutomaticLink)
