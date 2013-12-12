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

    args = parser.parse_args()

    guide = json.load(args.infile)
    return


if __name__ == '__main__':
    main()

