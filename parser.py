# parsing (AST creation) for a-lang

from enum import Enum, auto
from dataclasses import dataclass
from lexer import Token, TokenType, line_col_from_index
import sys

def parser(tokens,code):
    ast = RootNode(type=NodeType.ROOT, children=[])

    ast_children = []
    x = 0
    while x < len(tokens):
        if tokens[x].type == TokenType.Keyword and tokens[x].value == "use":
            if x+2 < len(tokens) and tokens[x+1].type == TokenType.Identifier and tokens[x+2].type == TokenType.Semicolon:
                import_node = ImportStatementNode(NodeType.IMPORT_STATEMENT ,tokens[x+1].value, "built-in", tokens[x].index)
                ast_children.append(import_node)
                x += 3
                continue
            else:
                line,col = line_col_from_index(code, tokens[x].index)
                print(f"Error: Invalid import statement starting at line {line}, column {col}")
                sys.exit(1) 
        elif tokens[x].type == TokenType.Keyword and tokens[x].value == "fun":
            if x+4 < len(tokens) and tokens[x+1].type == TokenType.Identifier and tokens[x+1].value == "main" and tokens[x+2].type == TokenType.LeftParen and tokens[x+3].type == TokenType.RightParen and tokens[x+4].type == TokenType.LeftBrace:
                main_fun_node = MainFunctionNode(NodeType.MAIN_FUNCTION,[], tokens[x].index)
                
                main_fun_node_body = []
                y = x + 5
                while y < len(tokens):
                    # look for print statements
                    if tokens[y].type == TokenType.Identifier and tokens[y].value == "print" and y+4 < len(tokens) and tokens[y+1].type == TokenType.LeftParen and tokens[y+2].type == TokenType.StringLiteral and tokens[y+3].type == TokenType.RightParen and tokens[y+4].type == TokenType.Semicolon:
                        print_node = PrintStatementNode(NodeType.PRINT_STATEMENT,StringLiteralNode(NodeType.STRING_LITERAL,tokens[y+2].value, tokens[y+2].index), tokens[y].index)
                        main_fun_node_body.append(print_node)    
                        y += 5
                        continue
                    elif tokens[y].type == TokenType.RightBrace:
                        break
                    
                    else:
                        line,col = line_col_from_index(code, tokens[y].index)
                        print(f"Error: Unexpected token '{tokens[y].value}' in main function body at line {line}, column {col}")
                        sys.exit(1)
                    y+=1

                # append body to main function node
                main_fun_node.body = main_fun_node_body

                # append main function node to ast children
                ast_children.append(main_fun_node)

                # check for closing brace
                if y < len(tokens) and tokens[y].type == TokenType.RightBrace:
                    x = y + 1
                    continue
                else:
                    line,col = line_col_from_index(code, tokens[y-1].index)
                    print(f"Error: Missing closing brace for main function, at line {line}, column {col}")
                    sys.exit(1)    
            else:
                line,col = line_col_from_index(code, tokens[x].index)
                print(f"Error: Invalid main function declaration starting at line {line}, column {col}")
                sys.exit(1)
        else:
            line,col = line_col_from_index(code, tokens[x].index)
            print(f"Error: Unexpected token '{tokens[x].value}' at line {line}, column {col}")
            sys.exit(1)
                
        x += 1

    ast.children = ast_children
    return ast

@dataclass
class ASTNode:
    """Base AST node providing serialization and repr helpers."""
    type = "node"

    def to_dict(self):
        d = {"type": getattr(self, "type", self.__class__.__name__)}
        for k, v in self.__dict__.items():
            if isinstance(v, ASTNode):
                d[k] = v.to_dict()
            elif isinstance(v, list):
                d[k] = [item.to_dict() if isinstance(item, ASTNode) else item for item in v]
            else:
                d[k] = v
        return d

    def __repr__(self):
        from pprint import pformat
        return pformat(self.to_dict(), compact=False)

    def __str__(self):
        return self.__repr__()


class RootNode(ASTNode):
    type = 'NodeType'

    def __init__(self,type, children=None):
        self.type = type
        self.children = children if children is not None else []


class ImportStatementNode(ASTNode):
    type = 'NodeType'

    def __init__(self, type,module_name, module_type, start_index):
        self.type = type
        self.module_name = module_name
        self.module_type = module_type
        self.start_index = start_index

class MainFunctionNode(ASTNode):
    type = 'NodeType'

    def __init__(self,type, body, start_index):
        self.type = type
        self.body = body
        self.start_index = start_index        

class PrintStatementNode(ASTNode):
    type: 'NodeType'

    def __init__(self,type, message, start_index):
        self.type = type
        self.message = message
        self.start_index = start_index

class StringLiteralNode(ASTNode):
    type: 'NodeType'

    def __init__(self,type, value, start_index):
        self.type = type
        self.value = value
        self.start_index = start_index

class NodeType(Enum):
    ROOT = auto()
    IMPORT_STATEMENT = auto()
    MAIN_FUNCTION = auto()
    PRINT_STATEMENT = auto()
    STRING_LITERAL = auto()

def pretty_print(node, indent=0):
    """Recursively print AST nodes in a human-friendly tree format."""
    prefix = " " * indent
    # Print node type and attributes (excluding children)
    attrs = []
    for k, v in node.__dict__.items():
        if k == "children":
            continue
        attrs.append(f"{k}={v!r}")
    attrs_str = ", ".join(attrs)
    print(f"{prefix}{node.type}({attrs_str})")

    # Recurse into children if present
    children = getattr(node, "children", None)
    if isinstance(children, list):
        for c in children:
            pretty_print(c, indent + 2)


