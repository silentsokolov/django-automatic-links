from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from automatic_links.models import AutomaticLink


class AdminAutomaticLink(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['keyword', 'link']}),
        (_('Option'), {'fields': ['active', 'limit', 'every', ('target', 'nofollow', 'css_class')]})
    ]

    list_display = ('active', 'keyword', 'link')
    list_display_links = ('keyword', 'link')
    list_filter = ('active',)


admin.site.register(AutomaticLink, AdminAutomaticLink)
