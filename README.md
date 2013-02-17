django-settings
===============

Django Settings Organized for Production and Development Environments.

**settings.py** - default settings. untouched except for custom_settings import. don't touch. always loaded.

**custom_settings.py** - settings that exist in settings.py that you wanted to change. always loaded.

**project_settings.py** - any additional project-specific settings that are not found in the default settings.py (e.g. USE_THOUSAND_SEPARATOR, GRAPPELLI_ADMIN_TITLE, CELERYBEAT_SCHEDULER, etc.). always loaded.

**production_settings.py** - production-specific settings. (e.g. DEBUG = False, DATABASES = {}, etc.). loaded by default unless running development server.

**local_settings.py** - development settings. (e.g. INTERNAL_IPS = ('127.0.0.1',), INSTALLED_APPS += ('debug_toolbar',), etc.). loaded with runserver.

Settings are loaded in this manner:

    settings.py
        custom_settings.py
            project_settings.py
                production_settings.py (default) OR local_settings.py
