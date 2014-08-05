#!/usr/bin/env python3

import json
import argparse
import sys
import collections

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

def jsonsert(content_string, guide_path):
    """
    takes the editorial content as a string and prints it into the
    guide.
    """

    content = json.loads(content_string, object_pairs_hook=collections.OrderedDict)
    guide = None
    with open(guide_path) as guide_file:
        guide = json.load(guide_file)

    guide['Cities'][0]['articles'] = content
    with open(guide_path,'w') as guide_file:
        json.dump(guide,guide_file)

    return

def imagesert(guidefilename, filename, url):
    """
    inserts the image property into the guide.
    """

    guide = None
    with open(guidefilename, 'r') as guide_file:
        guide = json.load(guide_file)

    if not guide:
        return True

    content = {"url":url, "file":filename}
    try:
        guide['Cities'][0]['image'] = content
    except KeyError:
        return True

    with open(guidefilename, 'w') as guide_file:
        json.dump(guide, guide_file)

    return False

def ec_merge(editorial_content, guide_content):
    """
    takes the editorial content and merge it with the guide_content.
    """
    guide_content['Cities'][0]['articles'] = editorial_content
    return guide_content

if __name__ == '__main__':
    main()

