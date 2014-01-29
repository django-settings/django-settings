# Custom Settings - Settings that exist in settings.py that you want to
# append to or override.

ADMINS = (
    ('Django Settings', 'django-settings@example.com'),
)

TIME_ZONE = 'America/Los_Angeles'

TEMPLATE_DIRS = (
    '',
)

from settings import INSTALLED_APPS
INSTALLED_APPS += (
    # 'grappelli',
)

from project_settings import *
