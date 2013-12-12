#!/usr/bin/env python3

import json
import argparse
import sys

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
            'infile',
            help='input file from which to pick json content to be inserted.'\
                    ' defaults to stdin if absent.',
            type = argparse.FileType('r'),
            nargs = '?',
            default = sys.stdin)

    parser.add_argument(
            'outfile',
            help='output json guide file',
            type = argparse.FileType('wr'))

    args = parser.parse_args()

    # read the editorial content.
    ec = json.load(args.infile)

    # insert it in the guide.
    print(guide)
    return

def ec_insert(ec, guide):

    # read the json guide into a data structure.
    # replace the


if __name__ == '__main__':
    main()

