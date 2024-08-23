import argparse
import math

def greet_user(name, times):
    """Prints a greeting message."""
    for _ in range(times):
        print(f"Hello, {name}!")

def calculate_square(number):
    """Calculates and prints the square of a number."""
    print(f"The square of {number} is {number ** 2}.")

def calculate_factorial(number):
    """Calculates and prints the factorial of a number."""
    print(f"The factorial of {number} is {math.factorial(number)}.")

def find_fibonacci(nth):
    """Calculates and prints the nth Fibonacci number."""
    a, b = 0, 1
    for _ in range(nth):
        a, b = b, a + b
    print(f"The {nth} Fibonacci number is {a}.")

def show_verbose_message():
    """Prints a verbose message."""
    print("Verbose mode is active! Detailed operations will be shown.")

def convert_temperature(temp, to_celsius):
    """Converts temperature between Celsius and Fahrenheit."""
    if to_celsius:
        converted = (temp - 32) * 5/9
        print(f"{temp}°F is {converted:.2f}°C.")
    else:
        converted = (temp * 9/5) + 32
        print(f"{temp}°C is {converted:.2f}°F.")

# Initialize the argument parser
parser = argparse.ArgumentParser(description="Super Duper Program with custom flags")

# Add custom flags
parser.add_argument("-g", "--greet", type=str, help="Greet a user by name")
parser.add_argument("-t", "--times", type=int, default=1, help="Number of times to greet the user")
parser.add_argument("-s", "--square", type=int, help="Calculate the square of a number")
parser.add_argument("-f", "--factorial", type=int, help="Calculate the factorial of a number")
parser.add_argument("-fib", "--fibonacci", type=int, help="Find the nth Fibonacci number")
parser.add_argument("-c", "--celsius", type=float, help="Convert Fahrenheit to Celsius")
parser.add_argument("-fah", "--fahrenheit", type=float, help="Convert Celsius to Fahrenheit")
parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode")

# Parse the command-line arguments
args = parser.parse_args()

# Handle the flags
if args.verbose:
    show_verbose_message()

if args.greet:
    greet_user(args.greet, args.times)

if args.square is not None:
    calculate_square(args.square)

if args.factorial is not None:
    calculate_factorial(args.factorial)

if args.fibonacci is not None:
    find_fibonacci(args.fibonacci)

if args.celsius is not None:
    convert_temperature(args.celsius, to_celsius=True)

if args.fahrenheit is not None:
    convert_temperature(args.fahrenheit, to_celsius=False)

# Default message if no flags are provided
if not any(vars(args).values()):
    print("Welcome to the Super Duper Program! Use -h for help.")
