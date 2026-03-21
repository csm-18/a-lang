

from lexer import lex
from parser import parse
from helper_functions import read_file
from helper_functions import pretty_print_ast
from ast import ImportStmtNode
from helper_functions import resolve_import_path


class ParsedFile:
    def __init__(self, filename,ast,imports):
        self.name = filename
        self.ast = ast
        self.imports = imports

def compile(filename):
    parsed_files = []
    src_filenames = []

    src_filenames.append(resolve_import_path(__file__,filename))

    #parse all the files and their imports            
    while len(src_filenames) != 0:
        src_file = read_file(src_filenames.pop(0))
        parsed_file = stage1(src_file)
        if len(parsed_file.imports) > 0:
            for import_stmt in parsed_file.imports:
                if import_stmt.is_stdlib_import:
                    continue
                else:
                    if import_stmt.filename not in src_filenames:
                        src_filenames.append(resolve_import_path(parsed_file.name,import_stmt.filename))
        parsed_files.append(parsed_file)    



def stage1(src_file):
    tokens = lex(src_file)
    ast = parse(tokens,src_file)
    #debug print
    pretty_print_ast(ast)
    imports = []
    y = 0
    while y < len(ast.body):
        node = ast.body[y]
        if isinstance(node, ImportStmtNode):
            imports.append(node)
        y += 1
    return ParsedFile(src_file.name,ast,imports)
