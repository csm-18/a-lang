from pathlib import Path
import sys

def line_pos_from_index(code,index):
    line = 1
    pos = 1

    for i in range(index):
        if code[i] == "\n":
            line += 1
            pos = 1
        else:
            pos += 1

    return line,pos


class File:
    def __init__(self,name,txt):
        self.name = name
        self.txt = txt


def read_file(filename):
    name = str(filename)
    txt = ""
    try:
        with open(filename, "r") as f:
            txt = f.read()
    except:
        print("error: Unable to read file",filename)
        sys.exit(1)
    return File(name,txt)
def print_error(msg,index,src):
    line,pos = line_pos_from_index(src.txt,index)
    print("error:",msg)
    print(f" -->({src.name})[{line}:{pos}]")
    sys.exit(1)


def resolve_import_path(current_file, import_path):
    current_file = Path(current_file)
    import_path = Path(import_path)

    # Resolve relative to current file's directory
    full_path = (current_file.parent / import_path).resolve(strict=False)
    return full_path


## extra helper functions
def _pretty_print_ast(node, indent=0, out=None, visited=None):
    if out is None:
        out = sys.stdout
    if visited is None:
        visited = set()

    spacer = "  " * indent

    if node is None:
        print(f"{spacer}None", file=out)
        return

    if id(node) in visited:
        print(f"{spacer}<recursive reference {node.__class__.__name__}>", file=out)
        return

    if isinstance(node, (str, int, float, bool)):
        print(f"{spacer}{repr(node)}", file=out)
        return

    if isinstance(node, (list, tuple)):
        if len(node) == 0:
            print(f"{spacer}[]", file=out)
            return
        print(f"{spacer}[", file=out)
        for item in node:
            _pretty_print_ast(item, indent + 1, out, visited)
        print(f"{spacer}]", file=out)
        return

    # Node-like object
    attrs = getattr(node, "__dict__", None)
    cls_name = node.__class__.__name__
    if attrs is None:
        print(f"{spacer}{cls_name}: {repr(node)}", file=out)
        return

    visited.add(id(node))
    header = f"{spacer}{cls_name}"
    if len(attrs) == 0:
        print(header, file=out)
        visited.remove(id(node))
        return

    print(header + ":", file=out)
    for key in sorted(attrs.keys()):
        value = attrs[key]
        # Skip private/internal keys
        if key.startswith("_"):
            continue

        if isinstance(value, (list, tuple)):
            print(f"{spacer}  {key}:", file=out)
            _pretty_print_ast(value, indent + 2, out, visited)
        elif isinstance(value, (str, int, float, bool)) or value is None:
            print(f"{spacer}  {key}: {repr(value)}", file=out)
        else:
            print(f"{spacer}  {key}:", file=out)
            _pretty_print_ast(value, indent + 2, out, visited)

    visited.remove(id(node))


def pretty_print_ast(node, out=None):
    """Print an AST tree in a human-readable form.

    Example usage:
      from helper_functions import pretty_print_ast
      pretty_print_ast(ast)

    This supports all node types (ProgramNode, SourceFileNode, FunctionDefNode,
    BlockNode, FunctionCallStmtNode, StringLiteralNode, NumberLiteralNode,
    BooleanLiteralNode, ImportStmtNode, etc.) and nested structures.
    """
    _pretty_print_ast(node, indent=0, out=out)
