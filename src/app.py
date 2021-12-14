#!/usr/bin/env python

import sys
import logging

def set_logging_level(debug):
    logging.basicConfig(format='%(asctime)s,%(msecs)03d [%(levelname)s] %(message)s'\
        , datefmt='%H:%M:%S', level=(logging.DEBUG if debug else logging.INFO))
    logging.debug('logging level set to %s' %('debug' if debug == True else 'logging'))


def main(args):
    set_logging_level('--debug' in args or '-d' in args)

if __name__ == '__main__':
    main(sys.argv)
