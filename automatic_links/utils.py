from automatic_links.link import Link
from automatic_links.models import AutomaticLink


def render_links(text, queryset=None):
    """
    Returns a new text from the replaced other links.
    Using all links from queryset.

    Default queryset: AutomaticLink.objects.all()
    """
    if not queryset:
        queryset = AutomaticLink.objects.filter(active=True)

    for link in queryset:
        l = Link(link.keyword, link.link, every=link.every, limit=link.limit, target=link.target,
                 nofollow=link.nofollow, css_class=link.css_class)
        text = l.render(text)

    return text