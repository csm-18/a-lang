from helper_functions import print_error

class AST_Node:
    def __init__(self):
        pass
        
class SourceFileNode(AST_Node):
    def __init__(self, filename, body):
        self.filename = filename
        self.body = body

class FunctionDefNode(AST_Node):
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

class FunctionCallNode(AST_Node):
    def __init__(self, name, args):
        self.name = name
        self.args = args

class StringLiteralNode(AST_Node):
    def __init__(self, value):
        self.value = value

def parse(tokens,src):
    ast = SourceFileNode(filename=src.filename, body=[])

    x = 0
    while x < len(tokens):
        if tokens[x].type == "keyword" and tokens[x].value == "fun":
            pass
        else:
            print_error("Unexpected token",tokens[x].index,src)
        x+=1
    return ast