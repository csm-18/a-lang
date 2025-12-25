# parsing (AST creation) for a-lang

from enum import Enum
from lexer import Token, TokenType

def parser(tokens):
    ast = RootNode()

    ast_children = []
    x = 0
    while x < len(tokens):
        if tokens[x].type == TokenType.Keyword and tokens[x].value == "use" and x+2 < len(tokens) and tokens[x+1].type == TokenType.Identifier and tokens[x+2].type == TokenType.Semicolon:
            import_node = ImportStatementNode(tokens[x+1].value, "built-in", tokens[x].index)
            ast_children.append(import_node)
            x += 3
            continue
            
            

            
        x += 1

    ast.children = ast_children
    return ast

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
    type = "root"

    def __init__(self, children=None):
        self.children = children if children is not None else []


class ImportStatementNode(ASTNode):
    type = "import_statement"

    def __init__(self, module_name, module_type, start_index):
        self.module_name = module_name
        self.module_type = module_type
        self.start_index = start_index


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


