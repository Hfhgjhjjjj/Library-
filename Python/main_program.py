import argparse
from verbose_flag import add_verbose_flag, handle_verbose_flag

parser = argparse.ArgumentParser(description="Program with standalone verbose flag")
add_verbose_flag(parser)
args = parser.parse_args()
handle_verbose_flag(args)
print("Main program running...")
