#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description="Perform basic math operations")
parser.add_argument("operation", type=str, choices=["add", "subtract", "multiply", "divide"], help="Operation to perform")
parser.add_argument("a", type=float, help="First number")
parser.add_argument("b", type=float, help="Second number")
args = parser.parse_args()

if args.operation == "add":
    result = args.a + args.b
elif args.operation == "subtract":
    result = args.a - args.b
elif args.operation == "multiply":
    result = args.a * args.b
elif args.operation == "divide":
    if args.b != 0:
        result = args.a / args.b
    else:
        result = "Error: Division by zero"
print(f"Result: {result}")
