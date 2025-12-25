# lexical analysis for a-lang

import sys
from dataclasses import dataclass
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

        elif code[x] == '"':
            end_quote = False
            y = x+1
            while y < len(code):
                if code[y] == '"' and code[y-1] != "\\":
                    end_quote = True
                    break
                y+=1
            if not end_quote:
                print("Error: Unterminated string literal")
                sys.exit(1)
            tokens.append(Token(TokenType.StringLiteral, code[x:y+1], x))
            x = y
        elif code[x] == "(":
            tokens.append(Token(TokenType.LeftParen, "(",x))
        elif code[x] == ")":
            tokens.append(Token(TokenType.RightParen, ")",x))
        elif code[x] == "{":
            tokens.append(Token(TokenType.LeftBrace, "{",x))
        elif code[x] == "}":
            tokens.append(Token(TokenType.RightBrace, "}",x))
        elif code[x] == ",":
            tokens.append(Token(TokenType.Comma, ",",x))
        elif code[x] == ";":
            tokens.append(Token(TokenType.Semicolon, ";",x))            
        x+=1
    return tokens

@dataclass
class Token:
    type: 'TokenType'
    value: str
    index: int

    def __repr__(self):
        return (f"Token(type={self.type}, value='{self.value}', index={self.index})")

class TokenType(Enum):
    Num = 1
    Keyword = 2
    Identifier = 3
    StringLiteral = 4
    LeftParen = 5
    RightParen = 6
    LeftBrace = 7
    RightBrace = 8
    Comma = 9
    Semicolon = 10
