import lexer

class SourceFile:
    def __init__(self,filename,code):
        self.filename = filename
        self.code = code

def compile(filename: str):
    #to store source file
    src = SourceFile(filename=filename, code="")

    #read .a source file to string
    try:
        with open(filename, "r") as f:
            src.code = f.read()
    except:
        print("error: Unable to read file",filename)        

    #lexical analysis
    lexer.lex(src)