#!/usr/bin/env python3
import argparse
import os

parser = argparse.ArgumentParser(description="Search for files by keyword")
parser.add_argument("-d", "--directory", type=str, default=".", help="Directory to search in")
parser.add_argument("-k", "--keyword", type=str, required=True, help="Keyword to search for in filenames")
args = parser.parse_args()

for root, dirs, files in os.walk(args.directory):
    for file in files:
        if args.keyword in file:
            print(os.path.join(root, file))
