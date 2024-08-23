import argparse

def add_verbose_flag(parser):
    """Adds a verbose flag to the parser."""
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode")

def handle_verbose_flag(args):
    """Handles the verbose flag."""
    if args.verbose:
        print("Verbose mode is active!")
