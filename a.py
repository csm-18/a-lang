import sys

# a compiler version
VERSION = "a 0.1.0"

def main():
    #cli args
    args = sys.argv[1:]

    if len(args) == 0:
        print(VERSION)
        print("a-lang is a toy programming language")
        print("for usage:")
        print("  a help")
    elif len(args) == 1:
        if args[0] == "version" or args[0] == "-v":
            print(VERSION)
        elif args[0] == "help" or args[0] == "-h":
            print("a compiler commands:")
            print(" 1. a <no args>     -> about info")
            print(" 2. a version|-v    -> print compiler version")
            print(" 3. a help|-h       -> print compiler commands list")
            print(" 4. a <filename.a>  -> compile .a file to binary")
        elif len(args[0]) > 2 and args[0].endswith(".a"):
            print("compiling...")            

if __name__ == "__main__":
    main()