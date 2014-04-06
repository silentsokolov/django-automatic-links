django-automatic-links
===============

django-automatic-links is a reusable application for Django, that allows you to adding keywords that will be automatically converted into links.


Installation
===============

### Requires

    django >= 1.4


Install with ``pip``:

Run ``pip install git+https://github.com/SilentSokolov/django-automatic-links.git``

Or ``pip install django-automatic-links``

Open ``settings.py`` and add ``automatic_links`` to your ``INSTALLED_APPS``:

    INSTALLED_APPS = (
        ...
        'automatic_links',
        ...
    )

Run ``manager.py syncdb``


Settings
===============

``LINK_DEFAULT_LIMIT`` (default: ``0``)
``LINK_DEFAULT_EVERY`` (default: ``1``)
``LINK_DEFAULT_TARGET`` (default: ``'_blank'``)
``LINK_DEFAULT_NOFOLLOW`` (default: ``False``)
``LINK_DEFAULT_CSS_CLASS`` (default: ``None``)

These values ​​are only used in the model (by default), you will still be able to customize for each link their values​​.


Example usage
===============

##  In templates

    {% load automatic_link_tags %}
    {{ object.text|add_links|safe }}


##  In code

    from automatic_links.utils import render_links

    text = render_links('text')
