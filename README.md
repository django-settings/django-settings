# django-settings
Django Settings Organized for Production and Development Environments.

### Use development settings
    $ cd myproject
    $ python manage.py runserver

### Use production settings
    $ cd myproject
    $ export PRODUCTION=1
    $ python manage.py runserver

## Settings File

**settings.py** - Default settings as created by `django-admin.py startproject`. Imports custom_settings, otherwise untouched. Don't touch. Always loaded.

**custom_settings.py** - Settings that exist in settings.py that you want to override or append to (e.g. ADMINS, TIME_ZONE, MEDIA_ROOT, MEDIA_URL, STATIC_ROOT, MIDDLEWARE_CLASSES, TEMPLATE_DIRS, INSTALLED_APPS, etc.). Always loaded.

**project_settings.py** - Settings that don't exist in settings.py that you want to add (e.g. USE_THOUSAND_SEPARATOR, GRAPPELLI_ADMIN_TITLE, CELERYBEAT_SCHEDULER, CELERYD_PREFETCH_MULTIPLIER, etc.). Always loaded.

**production_settings.py** - Settings that are specific to a production environment (e.g. DEBUG, TEMPLATE_DEBUG, DATABASES, etc.). Loaded by default unless the using development runserver or `export PRODUCTION=0` is specified on the command line.

**local_settings.py** - Settings that are specific to a development environment (e.g. DATABASES, INTERNAL_IPS, INSTALLED_APPS, etc.). Loaded with the runserver unless `export PRODUCTION=1` is specified on the command line.

Settings are loaded in this manner:

    settings.py
        custom_settings.py
            project_settings.py
                production_settings.py OR local_settings.py
