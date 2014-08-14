import re

from django.utils import unittest

from automatic_links.link import Link
from automatic_links.models import AutomaticLink
from automatic_links.templatetags.automatic_link_tags import add_links
from automatic_links.utils import render_links


class AutomaticLinksTest(unittest.TestCase):
    def setUp(self):
        self.simple_link = AutomaticLink.objects.create(keyword='keyword', link='/page.html', limit=1)
        self.link_with_space = AutomaticLink.objects.create(keyword='key word', link='/page.html')
        self.link_with_every_n = AutomaticLink.objects.create(keyword='every', link='/page.html', every=2)
        self.no_active_link = AutomaticLink.objects.create(active=False, keyword='noactive', link='/page.html')
        self.link_with_params = AutomaticLink.objects.create(keyword='params', link='/page.html',
                                                             css_class='class', nofollow=True)

    def test_keyword_in_beginning_of_line(self):
        original_text = 'keyword in the beginning of the line'
        done_text = '<a href="/page.html" target="_blank">keyword</a> in the beginning of the line'
        render_text = render_links(original_text)
        self.assertEqual(render_text, done_text)

    def test_keyword_in_ending_of_line(self):
        original_text = 'in the ending of the line keyword'
        done_text = 'in the ending of the line <a href="/page.html" target="_blank">keyword</a>'
        render_text = render_links(original_text)
        self.assertEqual(render_text, done_text)

    def test_keyword_with_space(self):
        original_text = 'text with key word'
        done_text = 'text with <a href="/page.html" target="_blank">key word</a>'
        render_text = render_links(original_text)
        self.assertEqual(render_text, done_text)

    def test_keyword_surrounded_by_tags_no_p(self):
        original_text = 'tags: <b>keyword</b>, <i>keyword</i>, <other>keyword</other> <a href="#">keyword</a>'
        done_text = 'tags: <b>keyword</b>, <i>keyword</i>, <other>keyword</other> <a href="#">keyword</a>'
        render_text = render_links(original_text)
        self.assertEqual(render_text, done_text)

    def test_keyword_surrounded_by_tags_with_p(self):
        original_text = 'tags: <p>keyword</p>, <i>keyword</i>, <b>keyword</b>'
        done_text = 'tags: <p><a href="/page.html" target="_blank">keyword</a></p>, <i>keyword</i>, <b>keyword</b>'
        render_text = render_links(original_text)
        self.assertEqual(render_text, done_text)

    def test_link_with_params(self):
        original_text = 'params'
        done_text = '<a href="/page.html" target="_blank" rel="nofollow" class="class">params</a>'
        render_text = render_links(original_text)
        self.assertEqual(render_text, done_text)

    def test_link_with_limit(self):
        original_text = 'keyword, keyword, keyword'
        done_text = '<a href="/page.html" target="_blank">keyword</a>, keyword, keyword'
        render_text = render_links(original_text)
        self.assertEqual(render_text, done_text)

    def test_link_with_every_n(self):
        original_text = 'every, every, every, every'
        done_text = 'every, <a href="/page.html" target="_blank">every</a>, every, <a href="/page.html" target="_blank">every</a>'
        render_text = render_links(original_text)
        self.assertEqual(render_text, done_text)

    def test_only_active_link(self):
        original_text = 'keyword, noactive, key word'
        done_text = '<a href="/page.html" target="_blank">keyword</a>, noactive, <a href="/page.html" target="_blank">key word</a>'
        render_text = render_links(original_text)
        self.assertEqual(render_text, done_text)

    def test_templatetags_add_links(self):
        original_text = 'keyword in the line'
        done_text = '<a href="/page.html" target="_blank">keyword</a> in the line'
        render_text = add_links(original_text)
        self.assertEqual(render_text, done_text)

    def test_link_word_boundaries(self):
        original_text = 'longkeywordsuper'
        done_text = 'longkeywordsuper'
        render_text = render_links(original_text)
        self.assertEqual(render_text, done_text)

    def tearDown(self):
        self.simple_link.delete()
        self.link_with_space.delete()
        self.link_with_every_n.delete()
        self.no_active_link.delete()
        self.link_with_params.delete()


class LinkTest(unittest.TestCase):
    def setUp(self):
        self.link = Link('keyword', '/page.html')

    def test_link_get_render_link(self):
        done_link = '<a href="/page.html" target="_blank">keyword</a>'
        self.assertEqual(self.link.get_render_link(), done_link)

    def test_link_get_regex(self):
        done_regex = re.compile(r'(?<![^p]>)keyword(\b)')
        self.assertEqual(self.link.regex.pattern, done_regex.pattern)

    def test_link_render(self):
        original_text = 'keyword in the line'
        done_text = '<a href="/page.html" target="_blank">keyword</a> in the line'
        self.assertEqual(self.link.render(original_text), done_text)