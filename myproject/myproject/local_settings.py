# Local Settings - Settings that are specific to a development environment (
# e.g. DATABASES, INTERNAL_IPS, INSTALLED_APPS, etc.)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database.db',
    }
}

# INTERNAL_IPS = ('127.0.0.1',)

from custom_settings import INSTALLED_APPS
INSTALLED_APPS += (
    # 'debug_toolbar',
)
