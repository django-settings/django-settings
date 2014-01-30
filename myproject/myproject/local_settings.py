# Define settings that are specific to the local environment.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database.db',
    }
}

INTERNAL_IPS = ('127.0.0.1',)

from custom_settings import INSTALLED_APPS
INSTALLED_APPS += (
    # 'debug_toolbar',
)
