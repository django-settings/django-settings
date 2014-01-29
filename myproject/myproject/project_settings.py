# Project Settings: Settings that are not defined settings.py that you want to
# use.

# USE_THOUSAND_SEPARATOR = True

# GRAPPELLI_ADMIN_TITLE = ''


import os
import sys

if 'PRODUCTION' in os.environ and os.environ['PRODUCTION'].lower() in [True, 'y', 'yes', '1',]:
    version = 'PRODUCTION'
    color = '[1;92m' # Bold High Intensity Green + Underline
    print '\n{star}  \x1b{color}{version}\x1b[0m {star}\n'.format(color=color,
                                                                  star='\xE2\x98\x85',
                                                                  version=version)
    from production_settings import *
else:
    if 'runserver' in sys.argv:
        version = 'DEVELOPMENT'
        color = '[1;93m' # Bold High Intensity Yellow + Underline
        print '\n{star}  \x1b{color}{version}\x1b[0m {star}\n'.format(color=color,
                                                                      star='\xE2\x98\x85',
                                                                      version=version)
    from local_settings import *
