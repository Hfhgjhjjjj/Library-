#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description="Super Tool with a custom flag")
parser.add_argument("-x", "--execute", type=str, help="Execute a specific command")
args = parser.parse_args()

if args.execute:
    print(f"Executing command: {args.execute}")

print("Super Tool finished.")
