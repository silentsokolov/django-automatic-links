from distutils.core import setup

setup(
    name='django-automatic-links',
    version='0.1',
    url='https://github.com/SilentSokolov/django-automatic-links',
    license='MIT',
    author='Dmitriy Sokolov',
    author_email='silentsokolov@gmail.com',
    description='Application for Django, that allows you to adding keywords that will be automatically converted into links.',
    packages=['automatic_links'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'django>=1.4',
    ],
)