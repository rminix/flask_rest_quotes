import os
from glob import glob


def exporter():
    for var in glob('/run/secrets/*'):
        k = var.split('/')[-1]
        v = open(var).read().rstrip('\n')
        os.environ[k] = v
