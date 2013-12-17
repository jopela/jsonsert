#!/usr/bin/env python3

import json
import argparse
import sys

def main():

    parser = argparse.ArgumentParser(description="insert editorial content"\
            " into an mtrip travel guide.")
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

    new_guide = ec_merge(editorial_content, guide_content)
    encoded_guide = json.dumps(new_guide)
    print(encoded_guide)
    return

def ec_merge(editorial_content, guide_content):
    """ takes the editorial content and merge it with the guide_content. """
    guide_content['Cities'][0]['articles'] = editorial_content
    return guide_content

if __name__ == '__main__':
    main()

