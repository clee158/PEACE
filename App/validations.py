
import os, sys
from os.path import isfile

import App.constants as const

# Environment variable checks
def env_check(env_list):
    missing = []
    for env in env_list:
        if env not in os.environ:
            missing.append(env)

    if len(missing) > 0:
        sys.exit('Please set environment variable: {}'.format(missing))

# Checking for file existance
def check_file(path):
    if not isfile(path):
        sys.exit('File {} does not exist'.format(path))
    elif not path.endswith('.jpg'):
        remove(path)
        sys.exit('File {} is not a .jpg file.'.format(path))

# Removing a file
def remove_file(path):
    os.remove(path)


