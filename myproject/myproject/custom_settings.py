# Custom Settings - Settings that exist in settings.py that you want to
# override or append to (e.g. ADMINS, TIME_ZONE, MEDIA_ROOT, MEDIA_URL,
# STATIC_ROOT, MIDDLEWARE_CLASSES, TEMPLATE_DIRS, INSTALLED_APPS, etc.)

#ADMINS = (('Django Settings', 'django-settings@example.com'),)

#TIME_ZONE = 'America/Los_Angeles'

#MEDIA_ROOT = 'media'

#MEDIA_URL = '/media/'

#STATIC_ROOT = 'static'

from settings import MIDDLEWARE_CLASSES
MIDDLEWARE_CLASSES += (
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

from settings import TEMPLATE_DIRS
TEMPLATE_DIRS += (
    #'',
)

from settings import INSTALLED_APPS
INSTALLED_APPS += (
    #'grappelli',
    #'django.contrib.admin',
    #'django.contrib.admindocs',
    #'djcelery',
    #'south',
)

from project_settings import *
