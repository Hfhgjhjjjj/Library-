#!/usr/bin/env python3
import argparse
import string
import random

parser = argparse.ArgumentParser(description="Generate a random password")
parser.add_argument("-l", "--length", type=int, default=12, help="Length of the password")
parser.add_argument("-s", "--special", action="store_true", help="Include special characters in the password")
args = parser.parse_args()

characters = string.ascii_letters + string.digits
if args.special:
    characters += string.punctuation

password = "".join(random.choice(characters) for _ in range(args.length))
print(f"Generated password: {password}")
