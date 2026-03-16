from helper_functions import print_error
from ast import ProgramNode, SourceFileNode, FunctionDefNode, BlockNode, FunctionCallStmtNode, FunctionCallExprNode, StringLiteralNode, IntegerLiteralNode

def parse(tokens,src):
    ast = ProgramNode(program_name=src.filename, body=[])
    return ast