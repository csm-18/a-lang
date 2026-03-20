from helper_functions import print_error
from ast import SourceFileNode, FunctionDefNode, BlockNode, FunctionCallStmtNode, FunctionCallExprNode, StringLiteralNode, IntegerLiteralNode

from rough import parse_function_def

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
    x = index+1
    func_def_node = FunctionDefNode(name="",params=[],body=None,index=tokens[index].index)
    
    if x+1 < len(tokens) and tokens[x].type == "identifier" and tokens[x+1].type == "left_paren":
        func_def_node.name = tokens[x].value
        
        if x+2 < len(tokens) and tokens[x+2].type == "right_paren":
            x = x+3
        else:
            pass # TODO: parse parameter list    

    else:
        print_error("Expected function name and parameter list",tokens[index].index,src)

    if x < len(tokens) and tokens[x].type == "left_brace":
        pass # TODO: parse function body
    else:
        print_error("Expected function body",tokens[index].index,src)

    if x < len(tokens) and tokens[x].type == "right_brace":
        x = x+1
    else:
        print_error("Expected closing brace",tokens[index].index,src)

    return func_def_node,x    
