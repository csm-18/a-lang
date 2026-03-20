from helper_functions import print_error
from ast import SourceFileNode, FunctionDefNode, BlockNode, FunctionCallStmtNode, FunctionCallExprNode, StringLiteralNode, IntegerLiteralNode

def parse(tokens,src):
    ast = SourceFileNode(name=src.name,body=[])

    x = 0
    while x < len(tokens):
        if tokens[x].type == "keyword" and tokens[x].value == "fun":
            func_def_node, new_index = parse_function_def(x,tokens,src)
            ast.body.append(func_def_node)
            x = new_index
            continue
        else:
            print_error("Unexpected token",tokens[x].index,src)
        x+=1
    return ast

def parse_function_def(index,tokens,src):
    pass

