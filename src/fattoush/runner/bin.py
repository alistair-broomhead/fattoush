#!/usr/bin/env python
#
"""
This script uses fattoush to run lettuce
"""


def console():
    from fattoush.config import FattoushConfigGroup
    FattoushConfigGroup.from_cli_args().run()


if __name__ == '__main__':
    console()