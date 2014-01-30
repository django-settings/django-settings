django-settings
===============

Django Settings organizes your project settings for use in various environments including production, local development, Linux, OS X, and Windows.

## Usage

1. Copy all [*_settings.py](https://github.com/django-settings/django-settings/tree/master/myproject/myproject) files into the same directory where your settings.py file is located.
2. Add `from custom_settings import *` to the bottom of your `settings.py`.
3. You're done. Settings for production, development, Linux, OS X, and Windows will now be included when run in their respective environments.

If you need an environment-specific setting, add the setting in the respective file. For example, to just turn on debugging when your project is run on a Windows server, add `DEBUG = True` in `win32_settings.py`.

## Development settings

    $ cd myproject
    $ export PRODUCTION=0
    $ python manage.py runserver
![django-settings screenshot](https://raw.github.com/django-settings/django-settings/master/screenshot/development-settings.png "")

## Production settings

    $ cd myproject
    $ export PRODUCTION=1
    $ python manage.py runserver

![django-settings screenshot](https://raw.github.com/django-settings/django-settings/master/screenshot/production-settings.png "")

## Configuration of settings files

### settings.py
Default settings as created by `django-admin.py startproject`. Imports custom_settings, otherwise untouched. Always loaded. Don't modify. Modifications you typically make here will be made in either `custom_settings.py` or `project_settings.py`.

### custom_settings.py
Settings that present in settings.py that you want to override or append to (e.g. INSTALLED_APPS, MIDDLEWARE_CLASSES, LANGUAGE_CODE, TIME_ZONE, etc.). Always loaded.

### user_settings.py
Settings that are not present in settings.py that you want to add (e.g. TEMPLATE_DIRS, USE_THOUSAND_SEPARATOR, GRAPPELLI_ADMIN_TITLE, CELERYBEAT_SCHEDULER, CELERYD_PREFETCH_MULTIPLIER, etc.). Always loaded.

### production_settings.py
Settings that are specific to a production environment (e.g. SECRET_KEY, DEBUG = False, TEMPLATE_DEBUG = False, ALLOWED_HOSTS, DATABASES, STATIC_URL, etc.). Loaded by default unless `export PRODUCTION=0` is specified on the command line.

### local_settings.py
Settings that are specific to a local development environment (e.g. DEBUG = True, TEMPLATE_DEBUG = True, INSTALLED_APPS += ('debug_toolbar',), DATABASES, INTERNAL_IPS, etc.). Loaded when `export PRODUCTION=0` is specified on the command line.

### linux_settings.py
Settings that are specific to a Linux environment.

### os_x_settings.py
Settings that are specific to an OS X environment.

### win32_settings.py
Settings that are specific to a Windows environment.
