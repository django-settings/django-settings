# Production Settings - Settings that are specific to a production environment (
# e.g. DEBUG, TEMPLATE_DEBUG, DATABASES, etc.)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
