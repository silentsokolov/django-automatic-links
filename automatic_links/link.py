import re
from itertools import cycle
from django.utils.functional import cached_property
from django.utils.text import normalize_newlines
try:
    from django.utils.encoding import force_text
except ImportError:
    # Historical name of force_text(), Django 1.4
    from django.utils.encoding import force_unicode as force_text


class Link(object):
    def __init__(self, keyword, link, every=1, limit=0, target='_blank', nofollow=False, css_class=None):
        self.keyword = keyword
        self.link = link
        self.every = every
        self.limit = limit
        self.target = target
        self.nofollow = nofollow
        self.css_class = css_class
        self._count = 0
        self._cycle = cycle(range(1, self.every+1))

    def repl(self, match):
        """
        This method applies to all matches found
        """
        value = match.group()
        if self.limit == 0 or self._count < self.limit:
            if next(self._cycle) == self.every:
                self._count += 1
                return self.get_render_link(value)
        return value

    @cached_property
    def regex(self):
        """
        Return compile regex

        Default: r'(?<![^p]>)%s(?!<[^/p])' use re.IGNORECASE
        Ignores all keywords are already in tags, except p
        """
        keyword = self.keyword.replace(' ', '(\s)').lower()
        regex = re.compile(r'(?<![^p]>)%s(\b)' % keyword, re.IGNORECASE)
        return regex

    def get_render_link(self, replace_word=None):
        # create params for tag <a ... ></a>, class, target, etc
        tag_params = ' target="%s"' % self.target
        if self.nofollow:
            tag_params += ' rel="nofollow"'
        if self.css_class:
            tag_params += ' class="%s"' % self.css_class

        # replace_word need as we use re.IGNORECASE
        html = '<a href="%s"%s>%s</a>' % (self.link, tag_params, replace_word or self.keyword)
        return html

    def render(self, text):
        """
        Returns a new text from the replaced keyword
        """
        text = normalize_newlines(force_text(text))
        return re.sub(self.regex, self.repl, text)