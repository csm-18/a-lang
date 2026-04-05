import sys
from compiler.lexer import lexer, SourceFile
from compiler.parser import parser
from compiler.code_gen import code_gen

def read_source_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except IOError:
        print(f"Error: Could not read file: {filename}")
        sys.exit(1)

def compile(filename):
    source_code = read_source_file(filename)
    source = SourceFile(filename, source_code)
    tokens = lexer(source)
    ast = parser(tokens)
    code_gen(ast, filename)
