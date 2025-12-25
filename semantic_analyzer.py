# semantic analysis for a-lang

from lexer import line_col_from_index
from parser import NodeType
import sys


def semantic_analyzer(ast,code):
    symbol_table = SymbolTable()

    if ast.type != NodeType.ROOT:
        print("Internal Error in semantic analyzer: AST root node is not RootNode")
        sys.exit(1)

    nodes = ast.children
    x = 0
    while x < len(nodes):
        node = nodes[x]
        if node.type == NodeType.IMPORT_STATEMENT and node.module_type == "built-in":
            if node.module_name in symbol_table.builtin_imports:
                line,col = line_col_from_index(code, node.start_index)
                print(f"Error: Duplicate import of module '{node.module_name}' at line {line}, column {col}")
                sys.exit(1)
            else:
                symbol_table.builtin_imports.append(node.module_name) 
        elif node.type == NodeType.MAIN_FUNCTION:
            if symbol_table.main_function_defined:
                line,col = line_col_from_index(code, node.start_index)
                print(f"Error: Multiple main function definitions found. Duplicate at line {line}, column {col}")
                sys.exit(1)
            else:
                symbol_table.main_function_defined = True

            # check main function body
            for stmt in node.body:
                if stmt.type == NodeType.PRINT_STATEMENT:
                    if stmt.message.type != NodeType.STRING_LITERAL:
                        line,col = line_col_from_index(code, stmt.start_index)
                        print(f"Error: Print statement at line {line}, column {col} can only print string literals")
                        sys.exit(1)
                    else:
                        symbol_table.print_statements_count += 1    
                else:
                    line,col = line_col_from_index(code, stmt.start_index)
                    print(f"Error: Unsupported statement type '{stmt.type}' in main function body at line {line}, column {col}")
                    sys.exit(1)
        else:
            line,col = line_col_from_index(code, node.start_index)
            print(f"Error: Unsupported top-level node type '{node.type}' at line {line}, column {col}")
            sys.exit(1)
        x += 1
    return symbol_table
        
class SymbolTable:
    builtin_imports = []
    main_function_defined = False
    print_statements_count = 0
