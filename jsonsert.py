#!/usr/bin/env python3

import json
import argparse
import sys

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
            'incontent',
            help='input file from which to pick json content to be inserted.'\
                    ' defaults to stdin if absent.',
            type = argparse.FileType('r'),
            nargs = '?',
            default = sys.stdin)

    parser.add_argument(
            'inguide',
            help='input file guide. The editorial content will be inserted'\
                    ' in that guide in order to produce a new guide.',
            type = argparse.FileType('r'))


    args = parser.parse_args()

    editorial_content = json.load(args.incontent)
    guide_content = json.load(args.inguide)

    ec_merge(editorial_content, guide_content)

    return

def ec_merge(editorial_content, guide_content):
    """ takes the editorial content and merge it with the guide_content. """
    print("EC:",editorial_content)
    print("GC:",guide_content)
    return

if __name__ == '__main__':
    main()

