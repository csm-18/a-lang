# lexical analysis for a-lang

from enum import Enum

def lexer(code):
    tokens = []
    x = 0
    while x < len(code):
        if code[x] == "#":
            newline = False

            y = x+1
            while y < len(code):
                if code[y] == "\n":
                    newline = True
                    break
                y+=1

            if newline:
                x = y
                continue
            else:
                return tokens        
        x+=1
    return tokens


class Token:
    def __init__(self, name, value,index):
        self.type = name    
        self.value = value
        self.index = index


class TokenType(Enum):
    NUM = 1