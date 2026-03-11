from helper_functions import print_error

class AST_Node:
    def __init__(self):
        pass
        
class SourceFileNode(AST_Node):
    def __init__(self, filename, body):
        self.filename = filename
        self.body = body

class FunctionDefNode(AST_Node):
    def __init__(self, name, params, body, index):
        self.name = name
        self.params = params
        self.body = body
        self.index = index

class FunctionCallNode(AST_Node):
    def __init__(self, name, args,index):
        self.name = name
        self.args = args
        self.index = index

class StringLiteralNode(AST_Node):
    def __init__(self, value,index):
        self.value = value
        self.index = index

def parse(tokens,src):
    ast = SourceFileNode(filename=src.filename, body=[])

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

def parse_function_def(x,tokens,src):
    func_def_node = FunctionDefNode(name="", params=[], body=[], index=tokens[x].index)

    if x + 1 < len(tokens) and tokens[x+1].type == "identifier":
        func_def_node.name = tokens[x+1].value
    else:
        print_error("Expected function name",tokens[x+1].index,src)

    if  x+2 < len(tokens) and tokens[x+2].type == "left_paren":
        x+=3
    else:
        print_error("Expected '(' after function name",tokens[x+2].index,src)   

    # to-do: parse parameters

    if x < len(tokens) and tokens[x].type == "right_paren":
        x+=1
    else:
        print_error("Expected ')' after function parameters",tokens[x].index,src)

    if x < len(tokens) and tokens[x].type == "left_brace":
        x+=1
    else:
        print_error("Expected '{' at the beginning of function body",tokens[x].index,src)

    # to-do: parse function body
    y = x
    while y < len(tokens):
        if y+1 < len(tokens) and tokens[y].type == "identifier" and tokens[y+1].type == "left_paren":
            # function call
            func_call_node, y = parse_function_call(y,tokens,src)
            func_def_node.body.append(func_call_node)
            continue
        elif tokens[y].type == "left_brace":
            x = y
            break
        else:
            print_error("Unexpected token in function body",tokens[y].index,src)
        y+=1

    if x < len(tokens) and tokens[x].type == "right_brace":
        x+=1
    else:
        print_error("Expected '}' at the end of function body",tokens[x].index,src)

    return func_def_node, x

def parse_function_call(x,tokens,src):
    pass        