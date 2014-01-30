django-settings
===============

Django Settings organizes your project settings for use in various environments including production, local development, Linux, OS X, and Windows.

## Usage

1. Copy all [*_settings.py](https://github.com/django-settings/django-settings/tree/master/myproject/myproject) files into the same directory where your settings.py file is located.
2. Add `from custom_settings import *` to the bottom of your `settings.py`.
3. You're done. Settings for production, development, Linux, OS X, and Windows will now be included when run in their respective environments.

If you need an environment-specific setting, add the setting in the respective file. For example, to turn on debugging when your project is run on a Windows server, add `DEBUG = True` in `win32_settings.py`.

## Development settings

    $ cd myproject
    $ python manage.py runserver
![django-settings screenshot](https://raw.github.com/django-settings/django-settings/master/screenshot/development-settings.png "")

## Production settings

    $ cd myproject
    $ export PRODUCTION=1
    $ python manage.py runserver

![django-settings screenshot](https://raw.github.com/django-settings/django-settings/master/screenshot/production-settings.png "")

## Settings Files

### settings.py
Default settings as created by `django-admin.py startproject`. Imports custom_settings, otherwise untouched. Always loaded. Don't modify. Modifications you typically make here will be made in either `custom_settings.py` or `project_settings.py`.

### custom_settings.py
Settings that exist in settings.py that you want to override or append to (e.g. ADMINS, TIME_ZONE, MEDIA_ROOT, MEDIA_URL, STATIC_ROOT, MIDDLEWARE_CLASSES, TEMPLATE_DIRS, INSTALLED_APPS, etc.). Always loaded.

### user_settings.py
Settings that don't exist in settings.py that you want to add (e.g. USE_THOUSAND_SEPARATOR, GRAPPELLI_ADMIN_TITLE, CELERYBEAT_SCHEDULER, CELERYD_PREFETCH_MULTIPLIER, etc.). Always loaded.

### production_settings.py
Settings that are specific to a production environment (e.g. DEBUG, DATABASES, ALLOWED_HOSTS, TEMPLATE_DEBUG, DATABASES, etc.). Loaded by default unless the using development runserver or `export PRODUCTION=0` is specified on the command line.

### local_settings.py
Settings that are specific to a development environment (e.g. DATABASES, DEBUG, INTERNAL_IPS, INSTALLED_APPS, etc.). Loaded with the runserver unless `export PRODUCTION=1` is specified on the command line.
