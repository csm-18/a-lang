from helper_functions import print_error
from ast import SourceFileNode, FunctionDefNode, BlockNode, FunctionCallStmtNode, StringLiteralNode, NumberLiteralNode, BooleanLiteralNode

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
    func_def_node = FunctionDefNode(name="",params=[],block=None,index=tokens[index].index)
    
    if x+1 < len(tokens) and tokens[x].type == "identifier" and tokens[x+1].type == "left_paren":
        func_def_node.name = tokens[x].value
        
        if x+2 < len(tokens) and tokens[x+2].type == "right_paren":
            x = x+3
        else:
            pass # TODO: parse parameter list    

    else:
        print_error("Expected function name and parameter list",tokens[index].index,src)

    
    # TODO: parse return type annotation
    
    if x < len(tokens) and tokens[x].type == "left_brace":
        block_node, new_index = parse_block(x,tokens,src)
        func_def_node.body = block_node
        x = new_index
    else:
        print_error("Expected function body",tokens[index].index,src)


    return func_def_node,x    

def parse_block(index,tokens,src):
    block_node = BlockNode(statements=[],index=tokens[index].index)
    x = index+1
    while x < len(tokens):
        if tokens[x].type == "identifier" and x+1 < len(tokens) and tokens[x+1].type == "left_paren":
            func_call_stmt_node, new_index = parse_function_call_stmt(x,tokens,src)
            block_node.statements.append(func_call_stmt_node)
            x = new_index
            continue
        elif tokens[x].type == "right_brace":
            x = x+1
            break
        else:
            print_error("Unexpected token in block",tokens[x].index,src)
        x+=1


    return block_node,x

def parse_function_call_stmt(index,tokens,src):
    func_call_stmt_node = FunctionCallStmtNode(name=tokens[index].value,args=[],index=tokens[index].index)
    x = index+2

    # TODO: parse function call arguments
    while x < len(tokens):
        if tokens[x].type == "string_literal":
            string_literal_node = StringLiteralNode(value=tokens[x].value,index=tokens[x].index)
            func_call_stmt_node.args.append(string_literal_node)
        elif tokens[x].type == "number_literal":
            number_literal_node = NumberLiteralNode(value=tokens[x].value,index=tokens[x].index)
            func_call_stmt_node.args.append(number_literal_node)
        elif tokens[x].type == "boolean_literal":
            boolean_literal_node = BooleanLiteralNode(value=tokens[x].value,index=tokens[x].index)
            func_call_stmt_node.args.append(boolean_literal_node)
        elif tokens[x].type == "identifier":
            pass # TODO: handle identifier arguments (variables, function calls, etc.)
        elif tokens[x].type == "comma":
            if x == index+2:
                print_error("Unexpected comma in function call arguments",tokens[x].index,src)
        elif tokens[x].type == "right_paren":
            break
        else:
            print_error("Unexpected token in function call arguments",tokens[x].index,src)

        x+=1

    if x < len(tokens) and tokens[x].type == "right_paren":
        x = x+1
    else:
        print_error("Expected closing parenthesis in function call",tokens[index].index,src)

    if x < len(tokens) and tokens[x].type == "semicolon":
        x = x+1
    else:
        print_error("Expected semicolon after function call",tokens[index].index,src)    


    return func_call_stmt_node,x     