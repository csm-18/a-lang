token_types = {
    "keyword":"keyword",
    "identifier": "identifier",
    "string_literal": "string_literal",
    "number_literal": "number_literal",
    "left_paren": "left_paren",
    "right_paren": "right_paren",
    "left_brace": "left_brace",
    "right_brace": "right_brace",
    "semicolon": "semicolon"
}

class Token:
    def __init__(self,type,value,index):
        self.type = type
        self.value = value
        self.index = index

def lex(src):
    pass