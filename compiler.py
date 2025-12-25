# compilation code for a-lang

import os
import sys
import subprocess
from lexer import lexer
from parser import parser, pretty_print
from code_gen import code_gen

#compile a c file into binary
def compile(filename):
    #read c file to string
    code = open(filename, 'r', encoding='utf-8').read()

    #lexical analysis
    tokens = lexer(code)
    # pprint(tokens)

    #parsing
    ast = parser(tokens,code)
    pretty_print(ast)

    # #semantic analysis
    # semantic_analysis(ast)

    # #code generation
    # output_c_code = code_gen(ast)

    # #create output c file
    # output_c_filename = filename[:-1] + "c"
    # with open(output_c_filename, "w", encoding="utf-8") as f:
    #     f.write(output_c_code)

    # #build the c file
    # try: 
    #     subprocess.run(["gcc", output_c_filename, "-o", output_c_filename[:-2]], check=True)
    # except:
    #     print("Error while building!")
    #     sys.exit(1)