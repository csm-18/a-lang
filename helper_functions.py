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
    name = filename
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
