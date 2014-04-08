#!/usr/bin/env python
import sys
from django.conf import settings #, global_settings as default_settings
from django.core.management import execute_from_command_line
from os import path

if not settings.configured:
    module_root = path.dirname(path.realpath(__file__))

    settings.configure(
        DEBUG=False,
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:'
            }
        },

        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sites',
            'django.contrib.admin',
            'django.contrib.sessions',
            'automatic_links',
        ),
        TEST_RUNNER='django.test.simple.DjangoTestSuiteRunner',
    )


# def runtests():
#     argv = sys.argv[:1] + ['test', 'parler'] + sys.argv[1:]
#     execute_from_command_line(argv)

def main():
    import sys
    from django.test.utils import get_runner

    TestRunner = get_runner(settings)

    test_runner = TestRunner()

    failures = test_runner.run_tests(('automatic_links',))
    sys.exit(failures)


if __name__ == '__main__':
    main()