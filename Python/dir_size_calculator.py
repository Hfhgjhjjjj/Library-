#!/usr/bin/env python3
import argparse
import os

def get_dir_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for file in filenames:
            fp = os.path.join(dirpath, file)
            total_size += os.path.getsize(fp)
    return total_size

parser = argparse.ArgumentParser(description="Calculate the size of a directory")
parser.add_argument("-d", "--directory", type=str, required=True, help="Directory to calculate size")
args = parser.parse_args()

size = get_dir_size(args.directory)
print(f"Total size of directory {args.directory}: {size / (1024*1024):.2f} MB")
