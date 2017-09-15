#!/usr/bin/env python

import argparse, os, re

def print_file_name(fname):
    print(fname)


def savevcard(out_file, card):
    with open(out_file, 'a') as final:
        final.write(card)

def processCards(in_file, out_file):
    card = ''
    count = 0
    with open(in_file) as f:
        for line in f:
            line = line.replace('\r\n', '').replace('\n', '').strip()
            card = card + line + '\n'
            if line == 'END:VCARD':
                if valid:
                    savevcard(out_file, card)
                card = ''
                count += 1
                print("Total contacts parsed : {}".format(count))
            elif re.search('^FN:', line):
                fullname = line[3:-1]
                if fullname != '':
                    valid = 1
                else:
                    valid = 0

def processArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help="Input File Name", required=True)
    parser.add_argument('-o', '--output', help="Output File Name", required=True)
    args = parser.parse_args()
    in_file = args.input
    out_file = args.output

    if not os.path.isfile(in_file):
        print("File does not exist")
        return

    processCards(in_file, out_file)


    print_file_name(in_file)
    print_file_name(out_file)


if __name__ == '__main__':
    processArguments()