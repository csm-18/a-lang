# lexical analysis for a-lang

import sys
from dataclasses import dataclass
from enum import Enum
import re

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
                line, col = line_col_from_index(code, x)
                print(f"Error: Unterminated string literal starting at line {line}, column {col}")
                sys.exit(1)
            tokens.append(Token(TokenType.StringLiteral, code[x:y+1], x))
            x = y
        elif code[x].isalnum() or code[x] == "_" or code[x] == ".":
            y = x
            while y < len(code) and (code[y].isalnum() or code[y] == "_" or code[y] == "."):
                y+=1
            word = code[x:y]
            if word in ["use","fun"]:
                tokens.append(Token(TokenType.Keyword, word, x))
            elif is_number_literal(word):
                tokens.append(Token(TokenType.Num, word, x))
            elif word.isalnum() or "_" in word and not word[0].isdigit() and "." not in word:
                tokens.append(Token(TokenType.Identifier, word, x))
            else:
                line, col = line_col_from_index(code, x)
                print(f"Error: Invalid token '{word}' at line {line}, column {col}")
                sys.exit(1)    
            x = y-1    
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

def is_number_literal(s):
    return bool(re.fullmatch(r"(0|[1-9]\d*)(\.\d+)?", s))

def line_col_from_index(code, index):
    line = 1
    col = 1
    for i in range(index):
        if code[i] == "\n":
            line += 1
            col = 1
        else:
            col += 1
    return line, col
