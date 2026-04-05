import sys
from enum import Enum
from dataclasses import dataclass
from typing import List

class TokenKind(Enum):
    IDENTIFIER = "identifier"
    NUMBER_LITERAL = "number_literal"
    STRING_LITERAL = "string_literal"
    BOOL_LITERAL = "bool_literal"
    PLUS = "plus"
    MINUS = "minus"
    STAR = "star"
    SLASH = "slash"
    LEFT_PAREN = "left_paren"
    RIGHT_PAREN = "right_paren"
    KEYWORD_DO = "keyword_do"
    KEYWORD_END = "keyword_end"
    KEYWORD_BOOL = "keyword_bool"
    KEYWORD_STRING = "keyword_string"

@dataclass
class Token:
    kind: TokenKind
    value: str

@dataclass
class SourceFile:
    filename: str
    code: str

def error_at(error: str, source: SourceFile, index: int):
    line = 1
    col = 1
    for i in range(index):
        if source.code[i] == '\n':
            line += 1
            col = 1
        else:
            col += 1
    print(f"Error in {source.filename} at line {line}, col {col}: {error}")
    sys.exit(1)

def lexer(source: SourceFile) -> List[Token]:
    tokens = []
    x = 0
    code = source.code
    
    while x < len(code):
        c = code[x]
        
        # Skip whitespace
        if c in (' ', '\t', '\n', '\r'):
            x += 1
            continue
        
        # Skip comments
        if c == '#':
            while x < len(code) and code[x] != '\n':
                x += 1
            continue
        
        # Parentheses
        if c == '(':
            tokens.append(Token(TokenKind.LEFT_PAREN, "("))
            x += 1
            continue
        
        if c == ')':
            tokens.append(Token(TokenKind.RIGHT_PAREN, ")"))
            x += 1
            continue
        
        # Operators
        if c == '+':
            tokens.append(Token(TokenKind.PLUS, "+"))
            x += 1
            continue
        
        if c == '-':
            tokens.append(Token(TokenKind.MINUS, "-"))
            x += 1
            continue
        
        if c == '*':
            tokens.append(Token(TokenKind.STAR, "*"))
            x += 1
            continue
        
        if c == '/':
            tokens.append(Token(TokenKind.SLASH, "/"))
            x += 1
            continue
        
        # String literals
        if c == '"':
            x += 1
            start = x
            while x < len(code) and code[x] != '"':
                x += 1
            if x >= len(code):
                error_at("Unterminated string literal", source, start - 1)
            value = code[start:x]
            tokens.append(Token(TokenKind.STRING_LITERAL, value))
            x += 1
            continue
        
        # Numbers
        if '0' <= c <= '9':
            start = x
            while x < len(code) and '0' <= code[x] <= '9':
                x += 1
            value = code[start:x]
            tokens.append(Token(TokenKind.NUMBER_LITERAL, value))
            continue
        
        # Identifiers and keywords
        if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or c == '_':
            start = x
            while x < len(code) and (('a' <= code[x] <= 'z') or ('A' <= code[x] <= 'Z') or ('0' <= code[x] <= '9') or code[x] == '_'):
                x += 1
            value = code[start:x]
            
            kind = TokenKind.IDENTIFIER
            if value == "do":
                kind = TokenKind.KEYWORD_DO
            elif value == "end":
                kind = TokenKind.KEYWORD_END
            elif value in ("true", "false"):
                kind = TokenKind.BOOL_LITERAL
            elif value == "bool":
                kind = TokenKind.KEYWORD_BOOL
            elif value == "string":
                kind = TokenKind.KEYWORD_STRING
            
            tokens.append(Token(kind, value))
            continue
        
        # Unknown character
        error_at(f"Unexpected character: {c}", source, x)
    
    return tokens
