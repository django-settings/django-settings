# Project Settings - Settings that don't exist in settings.py that you want to
# add (e.g. USE_THOUSAND_SEPARATOR, GRAPPELLI_ADMIN_TITLE, CELERYBEAT_SCHEDULER,
# CELERYD_PREFETCH_MULTIPLIER, etc.)

#USE_THOUSAND_SEPARATOR = True

#GRAPPELLI_ADMIN_TITLE = ''

#import djcelery
#djcelery.setup_loader()
#CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
#CELERYD_PREFETCH_MULTIPLIER = 1


import os
import sys

version = 'PRODUCTION'
color = '[1;92m' # Bold High Intensity Green + Underline
if 'PRODUCTION' in os.environ and os.environ['PRODUCTION'].lower() in [True, 'y', 'yes', '1',]:
    from local_settings import *
elif 'runserver' in sys.argv:
    version = 'DEVELOPMENT'
    color = '[1;93m' # Bold High Intensity Yellow + Underline
    from local_settings import *
else:
    from local_settings import *
print '\n{star}  \x1b{color}{version}\x1b[0m {star}\n'.format(color=color,
                                                              star='\xE2\x98\x85',
                                                              version=version)
