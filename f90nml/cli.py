"""f90nml.cli
   ==========

   Command line interface tools

   :copyright: Copyright 2014 Marshall Ward, see AUTHORS for details.
   :license: Apache License, Version 2.0, see LICENSE for details.
"""

import argparse

# Command line data
DESCRIPTION = 'Create and modify Fortran namelist files.'

def parse():
    """TODO"""

    parser = argparse.ArgumentParser(description=DESCRIPTION)

    parser.add_argument('--values', '-v')

    parser.add_argument('--patch', '-p',
                        action='store_true')

    print(parser.parse_args())
