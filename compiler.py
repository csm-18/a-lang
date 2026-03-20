from lexer import lex
from parser import parse
from helper_functions import read_file
from helper_functions import pretty_print_ast



class ParsedFile:
    def __init__(self, filename,ast,imports):
        self.name = filename
        self.ast = ast
        self.imports = imports

def compile(filename):
    parsed_files = []
    src_filenames = [filename]

    #parse all the files and their imports            
    while len(src_filenames) != 0:
        src_file = read_file(src_filenames.pop(0))
        parsed_file = stage1(src_file)
        if len(parsed_file.imports) > 0:
            src_filenames.extend(parsed_file.imports)
        parsed_files.append(parsed_file)    



def stage1(src_file):
    tokens = lex(src_file)
    ast = parse(tokens,src_file)
    #debug print
    pretty_print_ast(ast)
