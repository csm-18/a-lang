# entry point to a-lang compiler

import sys
from compiler import compile

#cli args
args = sys.argv[1:]

#cli args parsing
if len(args) == 0:
    print("c 0.0.1")
elif len(args) == 1 and args[0].endswith(".a"):
    compile(args[0])

