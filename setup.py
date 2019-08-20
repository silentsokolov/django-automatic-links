#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
from os.path import join, dirname
from setuptools import setup


def get_version(package):
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def get_packages(package):
    return [dirpath for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}


setup(
    name='django-automatic-links',
    version=get_version('automatic_links'),
    url='https://github.com/silentsokolov/django-automatic-links',
    license='MIT',
    description='django-automatic-links is django app, that allows you to adding keywords that will be automatically converted into links.',
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    author='Dmitriy Sokolov',
    author_email='silentsokolov@gmail.com',
    packages=get_packages('automatic_links'),
    package_data=get_package_data('automatic_links'),
    include_package_data=True,
    install_requires=[],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    zip_safe=False,
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities',
    ],
)
