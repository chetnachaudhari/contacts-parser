#!/usr/bin/env python

import argparse, os, re
from VCard import VCard

def print_file_name(fname):
    print(fname)


def savevcard(out_file, card):
    with open(out_file, 'a') as final:
        final.write("BEGIN:VCARD")
        final.write("\nVERSION:3.0")
        final.write("\nN:{}".format(card.n))
        final.write("\nFN:{}".format(card.fn))
        for (k,v) in card.tel:
            final.write("\n{}:{}".format(k,v))
        for (k,v) in card.email:
            final.write("\n{}:{}".format(k,v))

        final.write("\nEND:VCARD\n")


def validateTel(card):
    return 0

def validateEmail(card):
    return 0

def validateContact():
    # if all clear then 1 else 0
    return 0


def processCard(card):
    validateTel(card)
    validateEmail(card)
    validateContact()

def processCards(in_file, out_file):
    card = ''
    count = 0
    with open(in_file) as f:
        for line in f:
            line = line.replace('\r\n', '').replace('\n', '').strip()
            if re.search('BEGIN:VCARD', line):
                card = VCard()
            elif re.search('^N:', line):
                card.n = line[2:-1]
            elif re.search('^FN:', line):
                card.fn = line[3:-1]
            elif re.search('^EMAIL', line):
                splits = line.split(':')
                card.email.append((splits[0], splits[1]))
            elif re.search('^TEL', line):
                splits = line.split(':')
                card.tel.append((splits[0],splits[1]))
            elif re.search('END:VCARD', line):
                processCard(card)
                savevcard(out_file, card)
                count += 1
                print("Total contacts parsed : {}".format(count))

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