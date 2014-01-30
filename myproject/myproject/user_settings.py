# Imports environment-specific settings.

import os
import sys


try:
    from colorama import init as colorama_init
except ImportError:
    def colorama_init(autoreset=False, convert=None, strip=None, wrap=True):
        """
        Fallback function that initializes colorama.
        """
        pass

try:
    from termcolor import colored
except ImportError:
    def colored(text, color=None, on_color=None, attrs=None):
        """
        Fallback function to colorize text when termcolor is not installed.
        """
        return text


# Use production settings by default as it is the secure setup. To use local
# settings: $ export PRODUCTION=0
production = 'PRODUCTION' not in os.environ or os.environ['PRODUCTION'].lower() in [True, 'y', 'yes', '1',]
local = not production

platform = sys.platform
linux = platform == 'linux2'
os_x = platform == 'darwin'
win32 = platform == 'win32'

# Don't initialize colorama when on Windows and running the shell because the
# ipython colors get confused.
if not win32 or not 'shell' in sys.argv:
    colorama_init()

current_settings = []

if production:
    current_settings.append(colored('Production', 'green', attrs=['bold']))
    from production_settings import *
if local:
    current_settings.append(colored('Local', 'yellow', attrs=['bold']))
    from local_settings import *
if linux:
    current_settings.append(colored('Linux', 'blue', attrs=['bold']))
    from linux_settings import *
if os_x:
    current_settings.append(colored('OS X', 'blue', attrs=['bold']))
    from os_x_settings import *
if win32:
    current_settings.append(colored('Windows', 'blue', attrs=['bold']))
    from win32_settings import *

if 'runserver' in sys.argv:
    print '-' * 80
    print ' :: '.join(current_settings)
    print '-' * 80

    color = '[1;93m' # Bold High Intensity Yellow + Underline
    version = 'Development'
    if production:
        color = '[1;92m' # Bold High Intensity Green + Underline
        version = 'Production'
    print '\n{star}  \x1b{color}{version}\x1b[0m {star}\n'.format(color=color,
                                                                  star='\xE2\x98\x85',
                                                                  version=version)
