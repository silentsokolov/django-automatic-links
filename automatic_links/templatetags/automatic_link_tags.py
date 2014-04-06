from django import template
from automatic_links.utils import render_links

register = template.Library()


@register.filter()
def add_links(text):
    return render_links(text)
