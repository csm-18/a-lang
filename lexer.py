from helper_functions import print_error

keywords = ["fun","import"]

token_types = {
    "keyword":"keyword",
    "identifier": "identifier",
    "string_literal": "string_literal",
    "number_literal": "number_literal",
    "boolean_literal": "boolean_literal",
    "left_paren": "left_paren",
    "right_paren": "right_paren",
    "left_brace": "left_brace",
    "right_brace": "right_brace",
    "semicolon": "semicolon",
    "comma": "comma"
}

class Token:
    def __init__(self,type,value,index):
        self.type = type
        self.value = value
        self.index = index

def lex(src):
    tokens = []

    x = 0
    while x < len(src.txt):
        if src.txt[x] == "#": #ignore comments
            newline = False
            y = x+1
            while y < len(src.txt):
                if src.txt[y] == "\n":
                    newline = True
                    break
                y +=1 

            if newline:
                x = y
                continue
            else:
                break
        elif src.txt[x] == '"': #string literal
            end_quote = False
            y = x+1

            while y < len(src.txt):
                if src.txt[y] == '"' and src.txt[y-1] != '\\':
                    end_quote = True
                    break
                elif src.txt[y] == '"' and src.txt[y-1] == '\\':
                    if y-2 >= 0 and src.txt[y-2] == '\\':
                        end_quote = True
                        break        
                y +=1

            if end_quote:
                tokens.append(Token(token_types["string_literal"],src.txt[x+1:y],x))
                x = y+1
                continue
            else:
                print_error("Unterminated string literal",x,src)
        elif src.txt[x] == "\n" or src.txt[x] == " ": #ignore whitespace and newline
            x+=1
            continue
        elif src.txt[x] == "(":
            tokens.append(Token(token_types["left_paren"],"(",x))
        elif src.txt[x] == ")":
            tokens.append(Token(token_types["right_paren"],")",x))
        elif src.txt[x] == "{":
            tokens.append(Token(token_types["left_brace"],"{",x))
        elif src.txt[x] == "}":
            tokens.append(Token(token_types["right_brace"],"}",x))
        elif src.txt[x] == ";":
            tokens.append(Token(token_types["semicolon"],";",x))
        elif src.txt[x] == ",":
            tokens.append(Token(token_types["comma"],",",x))
        elif src.txt[x].isdigit(): #number literal
            number = ""

            y = x
            while y < len(src.txt) and src.txt[y].isdigit() or src.txt[y] == ".":
                number += src.txt[y]
                y +=1

            if number.count(".") > 1:
                print_error("Invalid number literal",x,src)
            elif number.startswith(".") or number.endswith("."):
                print_error("Invalid number literal",x,src)
                       

            tokens.append(Token(token_types["number_literal"],number,x))
            x = y
            continue        
        elif src.txt[x].isalpha() or src.txt[x] == '_': #keyword or identifier
            identifier = ""

            y = x
            while y < len(src.txt) and src.txt[y].isalnum() or src.txt[y] == "_":
                identifier += src.txt[y]
                y +=1

            if identifier == "true" or identifier == "false":
                tokens.append(Token(token_types["boolean_literal"],identifier,x))
            elif identifier in keywords:
                tokens.append(Token(token_types["keyword"],identifier,x))
            else:
                tokens.append(Token(token_types["identifier"],identifier,x))
            x = y
            continue
        else:
            print_error("Unexpected character",x,src)

        x+=1 

    return tokens    