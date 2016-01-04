# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import template

from ..utils import render_links

register = template.Library()


@register.filter()
def add_links(text):
    return render_links(text)
