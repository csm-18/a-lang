#!/usr/bin/env python3

import sys
from compiler.compiler import compile

COMPILER_VERSION = "0.1.0"

def print_about():
    """Print about message for a-lang."""
    print("a-lang compiler v" + COMPILER_VERSION)
    print("A simple programming language compiler written in Odin and Python")
    print()
    print_help()

def print_help():
    """Print available commands."""
    print("Commands:")
    print("  <filename.a>   Compile a-lang source file to binary")
    print("  version        Print compiler version")
    print("  help           Print this help message")

def print_version():
    """Print compiler version."""
    print("a-lang v" + COMPILER_VERSION)

def main():
    if len(sys.argv) == 1:
        # No arguments - print about and help
        print_about()
    elif len(sys.argv) == 2:
        arg = sys.argv[1]
        
        if arg == "version":
            print_version()
        elif arg == "help":
            print_help()
        elif arg.endswith(".a"):
            # Compile the file
            if len(arg) < 3:
                print("Error: File must be a-lang source file with .a extension")
                sys.exit(1)
            compile(arg)
        else:
            print(f"Error: Unknown command or invalid file: {arg}")
            print()
            print_help()
            sys.exit(1)
    else:
        print("Error: Too many arguments")
        print()
        print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
