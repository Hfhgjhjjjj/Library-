#!/usr/bin/env python3
import argparse
import os

parser = argparse.ArgumentParser(description="Bulk rename files by adding a prefix or suffix")
parser.add_argument("-d", "--directory", type=str, required=True, help="Directory containing files to rename")
parser.add_argument("-p", "--prefix", type=str, help="Prefix to add to filenames")
parser.add_argument("-s", "--suffix", type=str, help="Suffix to add to filenames")
args = parser.parse_args()

for filename in os.listdir(args.directory):
    new_name = filename
    if args.prefix:
        new_name = args.prefix + new_name
    if args.suffix:
        name, ext = os.path.splitext(new_name)
        new_name = name + args.suffix + ext
    os.rename(os.path.join(args.directory, filename), os.path.join(args.directory, new_name))
    print(f"Renamed {filename} to {new_name}")
