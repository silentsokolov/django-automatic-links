.. image:: https://travis-ci.org/silentsokolov/django-automatic-links.svg?branch=master
   :target: https://travis-ci.org/silentsokolov/django-automatic-links

.. image:: https://codecov.io/gh/silentsokolov/django-automatic-links/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/silentsokolov/django-automatic-links


django-automatic-links
======================

django-automatic-links is a application, that allows
you to adding keywords that will be automatically converted into links.


Requirements
------------

* Python 2.7+ or Python 3.2+
* Django 1.8+


Installation
------------

Use your favorite Python package manager to install the app from PyPI, e.g.

Example:

``pip install django-automatic-links``


Add ``automatic_links`` to ``INSTALLED_APPS``:

Example:

.. code:: python

    INSTALLED_APPS = (
        ...
        'automatic_links',
        ...
    )


After run command ``manager.py migrate automatic_links``.

Example usage
-------------

In templates
~~~~~~~~~~~~

.. code:: html

    {% load automatic_link_tags %}
    ...
    <p>{{ object.text|add_links|safe }}</p>


In code
~~~~~~~

.. code:: python

    from automatic_links.utils import render_links

    text = render_links('text')


If you have many links and the process takes a long time, you need to
concern yourself with cache.


Settings
--------

``LINK_DEFAULT_LIMIT`` (default: ``0``)

``LINK_DEFAULT_EVERY`` (default: ``1``)

``LINK_DEFAULT_TARGET`` (default: ``'_blank'``)

``LINK_DEFAULT_NOFOLLOW`` (default: ``False``)

``LINK_DEFAULT_CSS_CLASS`` (default: ``None``)

These values ​​are only used in the model, you will still be able to
customize for each link their values​​.
