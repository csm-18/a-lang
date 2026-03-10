from helper_functions import print_error

keywords = ["fun"]

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
    tokens = []

    x = 0
    while x < len(src.code):
        if src.code[x] == "#": #ignore comments
            newline = False
            y = x+1
            while y < len(src.code):
                if src.code[y] == "\n":
                    newline = True
                    break
                y +=1 

            if newline:
                x = y
                continue
            else:
                break
        elif src.code[x] == '"': #string literal
            end_quote = False
            y = x+1

            while y < len(src.code):
                if src.code[y] == '"' and src.code[y-1] != '\\':
                    end_quote = True
                    break
                elif src.code[y] == '"' and src.code[y-1] == '\\':
                    if y-2 >= 0 and src.code[y-2] == '\\':
                        end_quote = True
                        break        
                y +=1

            if end_quote:
                tokens.append(Token(token_types["string_literal"],src.code[x+1:y],x))
                x = y+1
                continue
            else:
                print_error("Unterminated string literal",x,src)
        elif src.code[x] == "\n" or src.code[x] == " ": #ignore whitespace and newline
            x+=1
            continue
        elif src.code[x] == "(":
            tokens.append(Token(token_types["left_paren"],"(",x))
        elif src.code[x] == ")":
            tokens.append(Token(token_types["right_paren"],")",x))
        elif src.code[x] == "{":
            tokens.append(Token(token_types["left_brace"],"{",x))
        elif src.code[x] == "}":
            tokens.append(Token(token_types["right_brace"],"}",x))
        elif src.code[x] == ";":
            tokens.append(Token(token_types["semicolon"],";",x))
        elif src.code[x].isalpha() or src.code[x] == '_': #keyword or identifier
            identifier = ""

            y = x
            while y < len(src.code) and src.code[y].isalnum() or src.code[y] == "_":
                identifier += src.code[y]
                y +=1

            if identifier in keywords:
                tokens.append(Token(token_types["keyword"],identifier,x))
            else:
                tokens.append(Token(token_types["identifier"],identifier,x))
            x = y
            continue
        else:
            print_error("Unexpected character",x,src)

        x+=1 

    return tokens    