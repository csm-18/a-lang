from parser import NodeType
import sys

def code_gen(ast,symbol_table):
    # check if main function is defined
    if symbol_table.main_function_defined == False:
        print("Error: No main function defined in the program")
        sys.exit(1)


    # check imports
    if len(symbol_table.builtin_imports) > 1:
        print("Only io module is supported in code generation for now")
        sys.exit(1)
    elif len(symbol_table.builtin_imports) == 1:
        if symbol_table.builtin_imports[0] != "io":
            print("Only io module is supported in code generation for now")
            sys.exit(1)

        if symbol_table.print_statements_count == 0:
            print("Warning: io module imported but no print statements found in main function")


    # generate code
    output = []
    output.append("#include <stdio.h>\n")
    output.append("\n")
    output.append("int main() {\n")

    if symbol_table.print_statements_count > 0:
        ast_nodes = ast.children
        for node in ast_nodes:
            if node.type == NodeType.MAIN_FUNCTION:
                for stmt in node.body:
                    if stmt.type == NodeType.PRINT_STATEMENT:
                        message = stmt.message.value
                        output.append(f'    puts({message});\n')


    output.append("\n")
    output.append("    return 0;\n")   
    output.append("}")

    return "".join(output)   



