# Lexical Conventions Specification

Detailed specification of lexical conventions, tokens, and syntax in a-lang.

## Source Code Organization

### File Format

- **Extension:** `.a`
- **Encoding:** ASCII (7-bit printable characters)
- **Line Endings:** Unix (LF, `\n`) or Windows (CRLF, `\r\n`)

### Character Set

a-lang uses the printable ASCII character set (0x20 to 0x7E) plus whitespace.

**Valid Characters:**

- Letters: `a-z`, `A-Z`
- Digits: `0-9`
- Punctuation: `! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ { | } ~`
- Whitespace: space, tab, newline, carriage return

## Tokens

### Token Types

| Token Type | Description | Example |
|-----------|-------------|---------|
| Keyword | Reserved word | `do`, `end`, `true`, `false` |
| Identifier | Variable/function name | `main`, `foo_bar` |
| Literal | Constant value | `42`, `"hello"`, `true` |
| Operator | Operation symbol | `+`, `-`, `*`, `/` |
| Delimiter | Grouping symbol | `(`, `)` |
| Comment | Documentation/note | `# comment` |

### Token Separators

Tokens are separated by:

- Whitespace: space, tab, newline
- Operators and delimiters act as separators

Examples:

```
print(42)       # 3 tokens: print, (, 42, ), with implicit separators
print (42)      # Same 3 tokens (whitespace is ignored between tokens)
print(42)print  # 4 tokens: print, (, 42, ), print
```

## Keywords

Reserved words that have special meaning and cannot be identifiers:

| Keyword | Purpose | Context |
|---------|---------|---------|
| `do` | Begin function body | `main() do` |
| `end` | End function body | `end` |
| `true` | Boolean true | Literal |
| `false` | Boolean false | Literal |
| `bool` | Boolean type | Type keyword (reserved) |
| `string` | String type | Type keyword (reserved) |

### Case Sensitivity

Keywords are case-sensitive.

Valid:
- `true`, `false` (lowercase)

Invalid:
- `True`, `False` (uppercase)
- `TRUE`, `FALSE` (uppercase)

## Identifiers

### Definition

A sequence of letters, digits, and underscores, starting with a letter or underscore.

### Syntax

```
identifier = [a-zA-Z_][a-zA-Z0-9_]*
```

### Examples

Valid:
- `main`
- `_private`
- `foo_bar`
- `var1`
- `x`
- `_`
- `CamelCase`

Invalid:
- `123var` (starts with digit)
- `-name` (contains invalid character)
- `foo-bar` (hyphen is not allowed)
- `foo.bar` (dot is not allowed)
- `foo bar` (space is not allowed)

### Keywords vs. Identifiers

Identifiers cannot be keywords:

```
do = 5          # ERROR: 'do' is a keyword
end()           # ERROR: 'end' is a keyword
x = 42          # OK: 'x' is a valid identifier
```

### Scope and Uniqueness

Currently, a-lang has no scope. All identifiers are global (not yet implemented).

## Literals

### Number Literals

**Syntax:** `[0-9]+`

Sequence of decimal digits representing an integer.

**Examples:**

Valid:
- `0`
- `42`
- `1000`
- `9999999`

Invalid:
- `3.14` (floating point not supported)
- `0x10` (hexadecimal not supported)
- `0o10` (octal not supported)
- `10_000` (digit separators not supported)
- `-5` (negative sign is separate operator)

### String Literals

**Syntax:** `" <content> "`

Sequence of characters enclosed in double quotes.

**Content:** Any ASCII character except:
- Unescaped double quote `"`
- Unescaped backslash `\` (must be escaped)

**Escape Sequences:**

| Escape | Character | Code Point | Output |
|--------|-----------|-----------|--------|
| `\\` | Backslash | 92 | `\` |
| `\"` | Double quote | 34 | `"` |
| `\n` | Newline | 10 | (line break) |
| `\t` | Tab | 9 | (tab) |

**Invalid Escapes:**

- `\s` → Undefined (not supported)
- `\0` → Null character (not supported)
- `\x41` → Hex escapes (not supported)

**Examples:**

Valid:
- `""` (empty string)
- `"hello"` (simple string)
- `"Hello, World!"` (with punctuation)
- `"Line 1\nLine 2"` (with newline)
- `"Path: C:\\Users\\name"` (with backslash)
- `"Quote: \"Hello\""` (with quote)

Invalid:
- `"Hello` (unterminated string)
- `"Quote: "Hello""` (unescaped internal quote)
- `"Path: C:\Users\name"` (unescaped backslash)

### Boolean Literals

**Syntax:** `true` | `false`

Two keyword literals representing boolean values.

**Examples:**

Valid:
- `true`
- `false`

Invalid:
- `True` (wrong case)
- `TRUE` (wrong case)
- `0` or `1` (not represented as numbers)

## Operators

### Arithmetic Operators

| Operator | Symbol | Precedence | Associativity |
|----------|--------|-----------|---------------|
| Multiplication | `*` | High | Left |
| Division | `/` | High | Left |
| Addition | `+` | Low | Left |
| Subtraction | `-` | Low | Left |

**Parsing:**

Operators are single-character tokens.

Examples:

```
3+4         # Three tokens: 3, +, 4
3 + 4       # Same three tokens
3+4*5       # Four tokens: 3, +, 4, *, 5
```

### Delimiters

| Delimiter | Purpose |
|-----------|---------|
| `(` | Open parenthesis |
| `)` | Close parenthesis |

**Parsing:**

Delimiters are single-character tokens that always separate adjacent tokens.

Examples:

```
print(42)   # Four tokens: print, (, 42, )
foo()       # Three tokens: foo, (, )
(1+2)       # Five tokens: (, 1, +, 2, )
```

## Comments

### Single-Line Comments

**Syntax:** `# <text>`

Starts with `#` and extends to end of line.

**Examples:**

```
# This is a comment
x = 42  # Inline comment
# Multiple lines of comments
# require multiple # symbols
```

### Comment Placement

Comments can appear:
- On their own line
- At the end of a statement line
- Between statements

**Invalid:**

- Inside strings: `"text # not a comment"`
- Inside numbers: `1 # 2` (parses as `1` followed by comment)

### Multi-Line Comments

a-lang does **not** support multi-line comments. Use multiple `#` lines:

```
# Line 1 of comment
# Line 2 of comment
# Line 3 of comment
```

## Whitespace

### Whitespace Characters

- Space (` `, U+0020)
- Tab (`\t`, U+0009)
- Newline (`\n`, U+000A)
- Carriage return (`\r`, U+000D)

### Significance

Whitespace is ignored between tokens and serves only to separate tokens.

**Examples:**

```
print(42)       # No spaces
print (42)      # Spaces ignored
print ( 42 )    # Extra spaces ignored
print(
  42
)               # Newlines ignored
```

One exception: Keywords and identifiers must be separated.

Invalid:

```
printx          # Single identifier, not 'print' + 'x'
doend           # Two keywords might appear as one token
```

Valid:

```
print x         # Two tokens separated by space
do end          # Valid (though end of a function)
```

## Tokens and Regular Expression

### Token Definitions

```
KEYWORD         = "do" | "end" | "true" | "false" | "bool" | "string"

IDENTIFIER      = [a-zA-Z_][a-zA-Z0-9_]*

NUMBER          = [0-9]+

STRING          = "\"" ([\x20-\x21\x23-\x5B\x5D-\x7E] | "\\\"" | "\\\\" | "\\n" | "\\t")* "\""

OPERATOR        = "+" | "-" | "*" | "/"

DELIMITER       = "(" | ")"

COMMENT         = "#" [^\n]* ("\n" | EOF)

WHITESPACE      = [ \t\n\r]+
```

## Lexing Rules

### Token Recognition Order

1. Skip whitespace
2. Skip comments
3. Check for operators and delimiters (single characters)
4. Check for string literals (starts with `"`)
5. Check for number literals (starts with digit)
6. Check for keywords or identifiers (starts with letter or `_`)
7. Unknown character: error

### Error Handling

Unknown characters cause a lexical error:

```
x = 42   # ERROR: Unexpected character '='
```

Valid characters in strings are:
- ASCII 0x20-0x21 (space to `!`)
- ASCII 0x23-0x5B (`#` to `[`)
- ASCII 0x5D-0x7E (`]` to `~`)
- Escape sequences: `\\`, `\"`, `\n`, `\t`

## Examples

### Simple Program Tokens

Source:

```
main() do
  print(42)
end
```

Tokens (in order):

```
IDENTIFIER(main)
DELIMITER(()
DELIMITER())
KEYWORD(do)
IDENTIFIER(print)
DELIMITER(()
NUMBER(42)
DELIMITER())
KEYWORD(end)
```

### String with Escapes

Source:

```
print("Hello\nWorld")
```

Tokens:

```
IDENTIFIER(print)
DELIMITER(()
STRING("Hello\nWorld")   # Note: \n is parsed as newline escape
DELIMITER())
```

### Comments are Ignored

Source:

```
# Start
main() do   # Entry point
  print(1)  # Output
end
```

Tokens:

```
IDENTIFIER(main)
DELIMITER(()
DELIMITER())
KEYWORD(do)
IDENTIFIER(print)
DELIMITER(()
NUMBER(1)
DELIMITER())
KEYWORD(end)
```
