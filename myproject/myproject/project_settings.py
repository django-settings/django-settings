# Project Settings - Settings that don't exist in settings.py that you want to
# add (e.g. USE_THOUSAND_SEPARATOR, GRAPPELLI_ADMIN_TITLE, CELERYBEAT_SCHEDULER,
# CELERYD_PREFETCH_MULTIPLIER, etc.)

#USE_THOUSAND_SEPARATOR = True

#GRAPPELLI_ADMIN_TITLE = ''

#import djcelery
#djcelery.setup_loader()
#CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
#CELERYD_PREFETCH_MULTIPLIER = 1


import sys

if 'runserver' in sys.argv:
    from local_settings import *
else:
    from production_settings import *
