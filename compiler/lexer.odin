package compiler

lexer :: proc(code: string) -> []token {
    tokens := []token{}
    
    x := 0
    for x < len(code) {
        if code[x] == '#'{
            // skip comment
            for x < len(code) && code[x] != '\n' {
                x += 1
            }
            continue
        }
        x+=1
    }
    return tokens
}

token :: struct {
    kind: token_kind,
    value: string
}

token_kind :: enum {
    number_literal,
}
