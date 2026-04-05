import sys
import subprocess
import os
from compiler.parser import AstNode, AstKind

def escape_c_string(value: str) -> str:
    """Escape a Python string for use in C code."""
    result = ""
    for c in value:
        if c == '\\':
            result += "\\\\"
        elif c == '"':
            result += "\\\""
        elif c == '\n':
            result += "\\n"
        elif c == '\t':
            result += "\\t"
        else:
            result += c
    return result

def generate_expression(node: AstNode) -> str:
    """Generate C code for an expression."""
    if node.kind == AstKind.NUMBER_LITERAL:
        return node.value
    elif node.kind == AstKind.STRING_LITERAL:
        return f'"{escape_c_string(node.value)}"'
    elif node.kind == AstKind.BOOL_LITERAL:
        return node.value
    elif node.kind == AstKind.BINARY_OP:
        left = generate_expression(node.children[0])
        right = generate_expression(node.children[1])
        return f"({left} {node.value} {right})"
    elif node.kind == AstKind.IDENTIFIER:
        return node.value
    return "0"

def generate_statement(node: AstNode) -> str:
    """Generate C code for a statement."""
    if node.kind == AstKind.CALL and node.value == "print" and len(node.children) == 1:
        expr = node.children[0]
        if expr.kind == AstKind.STRING_LITERAL:
            return f'    printf("%s\\n", "{escape_c_string(expr.value)}");\n'
        elif expr.kind == AstKind.BOOL_LITERAL:
            return f'    printf("%s\\n", {generate_expression(expr)} ? "true" : "false");\n'
        else:
            return f'    printf("%d\\n", {generate_expression(expr)});\n'
    return ""

def generate_c(ast: AstNode) -> str:
    """Generate the complete C program."""
    body = "#include <stdio.h>\n#include <stdbool.h>\n\nint main() {\n"
    for stmt in ast.children:
        body += generate_statement(stmt)
    body += "    return 0;\n}"
    return body

def code_gen(ast: AstNode, input_filename: str = "a.out"):
    """Generate C code, compile with gcc, and clean up temp files."""
    # Extract base name from input filename (remove .a extension)
    output_name = input_filename.rsplit('.', 1)[0] if '.' in input_filename else input_filename
    output_name = os.path.basename(output_name)
    
    c_code = generate_c(ast)
    
    try:
        with open("temp.c", "w") as f:
            f.write(c_code)
    except IOError:
        print("Error writing C file")
        sys.exit(1)
    
    result = subprocess.run(["gcc", "temp.c", "-o", output_name], capture_output=True)
    
    if result.returncode != 0:
        if os.path.exists("temp.c"):
            os.remove("temp.c")
        print("Error compiling C code")
        sys.exit(1)
    
    if os.path.exists("temp.c"):
        os.remove("temp.c")
    
    print(f"Compiled to {output_name}")
