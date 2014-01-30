# Define settings that are not specified in settings.py.

ADMINS = (
    ('Zach Borboa', 'zachborboa@example.com'),
)

TIME_ZONE = 'America/Los_Angeles'

TEMPLATE_DIRS = (
    '',
)

from settings import INSTALLED_APPS
INSTALLED_APPS += (
    # '',
)

from user_settings import *
