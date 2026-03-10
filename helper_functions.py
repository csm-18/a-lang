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

def print_error(msg,index,src):
    line,pos = line_pos_from_index(src.code,index)
    print("error:",msg)
    print(f" -->({src.filename})[{line}:{pos}]")
    sys.exit(1)
