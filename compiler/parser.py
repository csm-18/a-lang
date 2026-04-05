from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional
from compiler.lexer import Token, TokenKind

class AstKind(Enum):
    FUNCTION = "function"
    CALL = "call"
    BINARY_OP = "binary_op"
    NUMBER_LITERAL = "number_literal"
    STRING_LITERAL = "string_literal"
    BOOL_LITERAL = "bool_literal"
    IDENTIFIER = "identifier"

@dataclass
class AstNode:
    kind: AstKind
    value: str = ""
    children: List['AstNode'] = field(default_factory=list)

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
    
    def current_token(self) -> Optional[Token]:
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None
    
    def advance(self):
        self.pos += 1
    
    def parse(self) -> AstNode:
        return self.parse_function()
    
    def parse_function(self) -> AstNode:
        # identifier ( ) do statements end
        if not self.current_token():
            return AstNode(AstKind.FUNCTION)
        
        name = self.current_token().value
        self.advance()
        
        if not self.current_token() or self.current_token().kind != TokenKind.LEFT_PAREN:
            return AstNode(AstKind.FUNCTION)
        self.advance()
        
        if not self.current_token() or self.current_token().kind != TokenKind.RIGHT_PAREN:
            return AstNode(AstKind.FUNCTION)
        self.advance()
        
        if not self.current_token() or self.current_token().kind != TokenKind.KEYWORD_DO:
            return AstNode(AstKind.FUNCTION)
        self.advance()
        
        body = self.parse_statements()
        
        if not self.current_token() or self.current_token().kind != TokenKind.KEYWORD_END:
            return AstNode(AstKind.FUNCTION)
        self.advance()
        
        node = AstNode(kind=AstKind.FUNCTION, value=name)
        node.children = body
        return node
    
    def parse_statements(self) -> List[AstNode]:
        statements = []
        while self.current_token() and self.current_token().kind != TokenKind.KEYWORD_END:
            stmt = self.parse_statement()
            statements.append(stmt)
        return statements
    
    def parse_statement(self) -> AstNode:
        return self.parse_call()
    
    def parse_call(self) -> AstNode:
        if not self.current_token():
            return AstNode(AstKind.CALL)
        
        name = self.current_token().value
        self.advance()
        
        if not self.current_token() or self.current_token().kind != TokenKind.LEFT_PAREN:
            return AstNode(AstKind.CALL)
        self.advance()
        
        arg = self.parse_expression()
        
        if not self.current_token() or self.current_token().kind != TokenKind.RIGHT_PAREN:
            return AstNode(AstKind.CALL)
        self.advance()
        
        node = AstNode(kind=AstKind.CALL, value=name)
        node.children.append(arg)
        return node
    
    def parse_expression(self) -> AstNode:
        left = self.parse_term()
        
        while self.current_token():
            op = self.current_token()
            if op.kind not in (TokenKind.PLUS, TokenKind.MINUS):
                break
            self.advance()
            right = self.parse_term()
            node = AstNode(kind=AstKind.BINARY_OP, value=op.value)
            node.children.append(left)
            node.children.append(right)
            left = node
        
        return left
    
    def parse_term(self) -> AstNode:
        left = self.parse_factor()
        
        while self.current_token():
            op = self.current_token()
            if op.kind not in (TokenKind.STAR, TokenKind.SLASH):
                break
            self.advance()
            right = self.parse_factor()
            node = AstNode(kind=AstKind.BINARY_OP, value=op.value)
            node.children.append(left)
            node.children.append(right)
            left = node
        
        return left
    
    def parse_factor(self) -> AstNode:
        if not self.current_token():
            return AstNode(AstKind.IDENTIFIER)
        
        tok = self.current_token()
        
        if tok.kind == TokenKind.LEFT_PAREN:
            self.advance()
            node = self.parse_expression()
            if self.current_token() and self.current_token().kind == TokenKind.RIGHT_PAREN:
                self.advance()
            return node
        
        self.advance()
        
        if tok.kind == TokenKind.NUMBER_LITERAL:
            return AstNode(kind=AstKind.NUMBER_LITERAL, value=tok.value)
        elif tok.kind == TokenKind.STRING_LITERAL:
            return AstNode(kind=AstKind.STRING_LITERAL, value=tok.value)
        elif tok.kind == TokenKind.BOOL_LITERAL:
            return AstNode(kind=AstKind.BOOL_LITERAL, value=tok.value)
        elif tok.kind == TokenKind.IDENTIFIER:
            return AstNode(kind=AstKind.IDENTIFIER, value=tok.value)
        
        return AstNode(AstKind.IDENTIFIER)

def parser(tokens: List[Token]) -> AstNode:
    p = Parser(tokens)
    return p.parse()
