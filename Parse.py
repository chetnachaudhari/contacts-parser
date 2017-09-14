#!/usr/bin/env python

import argparse, os

def print_file_name(fname):
    print(fname)

def processFile():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help="Input File Name", required=True)
    parser.add_argument('-o', '--output', help="Output File Name", required=True)
    args = parser.parse_args()
    in_file = args.input
    out_file = args.output


    
    print_file_name(in_file)
    print_file_name(out_file)


if __name__ == '__main__':
    processFile()