class Node:    
    def __init__(self):
        pass

class ProgramNode(Node):
    def __init__(self,program_name, body):
        self.program_name = program_name
        self.body = body

class SourceFileNode(Node):
    def __init__(self, filename, body):
        self.filename = filename
        self.body = body

class FunctionDefNode(Node):
    def __init__(self, name, params, block, index):
        self.name = name
        self.params = params
        self.body = block
        self.index = index

class BlockNode(Node):
    def __init__(self, statements, index):
        self.statements = statements
        self.index = index

class FunctionCallStmtNode(Node):
    def __init__(self, name, args,index):
        self.name = name
        self.args = args
        self.index = index

class StringLiteralNode(Node):
    def __init__(self, value,index):
        self.value = value
        self.index = index    

class IntegerLiteralNode(Node):
    def __init__(self, value,index):
        self.value = value
        self.index = index