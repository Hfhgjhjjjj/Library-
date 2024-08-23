#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description="Count the number of lines in a text file")
parser.add_argument("-f", "--file", type=str, required=True, help="File to count lines")
args = parser.parse_args()

with open(args.file, "r") as file:
    lines = file.readlines()
    print(f"Number of lines in {args.file}: {len(lines)}")
