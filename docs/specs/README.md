# a-lang Language Specification Index

Complete language specification for a-lang, organized by topic.

## Quick Navigation

### Core Documentation

- [**SPECIFICATION.md**](SPECIFICATION.md) - Full language specification overview
- [**LEXICAL_CONVENTIONS.md**](LEXICAL_CONVENTIONS.md) - Tokens, keywords, literals, operators
- [**DATA_TYPES.md**](DATA_TYPES.md) - Number, String, Boolean types
- [**EXPRESSIONS.md**](EXPRESSIONS.md) - Operators, precedence, evaluation
- [**STATEMENTS_AND_FUNCTIONS.md**](STATEMENTS_AND_FUNCTIONS.md) - Statements, functions, built-ins

## Topic Index

### Language Fundamentals

- **Lexical Structure**
  - Comments: [LEXICAL_CONVENTIONS.md#comments](LEXICAL_CONVENTIONS.md)
  - Identifiers: [LEXICAL_CONVENTIONS.md#identifiers](LEXICAL_CONVENTIONS.md)
  - Keywords: [LEXICAL_CONVENTIONS.md#keywords](LEXICAL_CONVENTIONS.md)
  - Tokens: [LEXICAL_CONVENTIONS.md#tokens](LEXICAL_CONVENTIONS.md)
  - Whitespace: [LEXICAL_CONVENTIONS.md#whitespace](LEXICAL_CONVENTIONS.md)

- **Data Types**
  - Number: [DATA_TYPES.md#number-type](DATA_TYPES.md)
  - String: [DATA_TYPES.md#string-type](DATA_TYPES.md)
  - Boolean: [DATA_TYPES.md#boolean-type](DATA_TYPES.md)
  - Type Coercion: [DATA_TYPES.md#type-coercion](DATA_TYPES.md)

### Operations and Expressions

- **Arithmetic Expressions**
  - Operators: [EXPRESSIONS.md#operators](EXPRESSIONS.md)
  - Precedence: [EXPRESSIONS.md#precedence-and-associativity](EXPRESSIONS.md)
  - Evaluation: [EXPRESSIONS.md#evaluation-examples](EXPRESSIONS.md)
  - Division: [EXPRESSIONS.md#division-semantics](EXPRESSIONS.md)

- **Primary Expressions**
  - Number Literals: [LEXICAL_CONVENTIONS.md#number-literals](LEXICAL_CONVENTIONS.md)
  - String Literals: [LEXICAL_CONVENTIONS.md#string-literals](LEXICAL_CONVENTIONS.md)
  - Boolean Literals: [LEXICAL_CONVENTIONS.md#boolean-literals](LEXICAL_CONVENTIONS.md)
  - Parentheses: [EXPRESSIONS.md#parentheses](EXPRESSIONS.md)

### Program Structure

- **Functions**
  - Definition: [STATEMENTS_AND_FUNCTIONS.md#function-definition](STATEMENTS_AND_FUNCTIONS.md)
  - main(): [STATEMENTS_AND_FUNCTIONS.md#entry-point](STATEMENTS_AND_FUNCTIONS.md)
  - Body: [STATEMENTS_AND_FUNCTIONS.md#function-body](STATEMENTS_AND_FUNCTIONS.md)

- **Statements**
  - Call Statements: [STATEMENTS_AND_FUNCTIONS.md#call-statement](STATEMENTS_AND_FUNCTIONS.md)
  - Sequences: [STATEMENTS_AND_FUNCTIONS.md#statement-sequencing](STATEMENTS_AND_FUNCTIONS.md)

- **Built-in Functions**
  - print(): [STATEMENTS_AND_FUNCTIONS.md#print](STATEMENTS_AND_FUNCTIONS.md)

### Detailed Reference

- **String Details**
  - Valid Characters: [DATA_TYPES.md#valid-characters](DATA_TYPES.md)
  - Escape Sequences: [DATA_TYPES.md#escape-sequences](DATA_TYPES.md)
  - Examples: [DATA_TYPES.md#examples](DATA_TYPES.md)

- **Lexical Details**
  - Character Set: [LEXICAL_CONVENTIONS.md#character-set](LEXICAL_CONVENTIONS.md)
  - Token Recognition: [LEXICAL_CONVENTIONS.md#token-recognition-order](LEXICAL_CONVENTIONS.md)
  - Escape Handling: [LEXICAL_CONVENTIONS.md#escape-sequences](LEXICAL_CONVENTIONS.md)

- **Error Handling**
  - Compile-time Errors: [EXPRESSIONS.md#error-conditions](EXPRESSIONS.md)
  - Runtime Behavior: [EXPRESSIONS.md#error-conditions](EXPRESSIONS.md)

## Quick Reference

### Keywords

```
do      - Begin function body
end     - End function body
true    - Boolean true
false   - Boolean false
bool    - Boolean type (reserved)
string  - String type (reserved)
```

### Operators (by Precedence)

| Precedence | Operators | Associativity |
|-----------|-----------|---------------|
| Highest | `*`, `/` | Left |
| Lower | `+`, `-` | Left |

### Data Types

| Type | Literals | Operations |
|------|----------|-----------|
| number | `0`, `42`, `-5` | `+`, `-`, `*`, `/` |
| string | `"hello"` | `print()` |
| boolean | `true`, `false` | `print()` |

### Built-in Functions

| Function | Purpose | Example |
|----------|---------|---------|
| `print()` | Output value | `print(42)` |

## Document Map

```
docs/specs/
├── README.md                        (this file)
├── SPECIFICATION.md                 (overview)
├── LEXICAL_CONVENTIONS.md           (tokens, keywords, literals)
├── DATA_TYPES.md                    (type definitions)
├── EXPRESSIONS.md                   (operators, evaluation)
└── STATEMENTS_AND_FUNCTIONS.md      (control flow, functions)
```

## Version

- **Specification Version:** 1.0
- **Compiler Version:** 0.1.0
- **Language:** a-lang
- **Status:** Stable (limited feature set)

## What's Not Supported

The following features are **not** currently supported in a-lang:

- Variables and variable declaration
- Type annotations
- Conditionals (`if`, `else`, `switch`)
- Loops (`while`, `for`, `do...while`)
- User-defined functions (only `main()`)
- Function parameters and return values
- Arrays and data structures
- String operations and concatenation
- Boolean operators (`&&`, `||`, `!`)
- Comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- Assignment operator (`=`)
- Scoping
- Modules/imports
- Exception handling

## Examples by Topic

### Hello World

```
main() do
  print("Hello, World!")
end
```

See: [STATEMENTS_AND_FUNCTIONS.md#example-programs](STATEMENTS_AND_FUNCTIONS.md)

### Arithmetic

```
main() do
  print(2 + 3)
  print(10 - 4)
  print(3 * 7)
  print(20 / 4)
end
```

See: [EXPRESSIONS.md#examples](EXPRESSIONS.md)

### Multiple Statements

```
main() do
  print("First")
  print("Second")
  print(1 + 2)
end
```

See: [STATEMENTS_AND_FUNCTIONS.md#statement-sequencing](STATEMENTS_AND_FUNCTIONS.md)

### Operator Precedence

```
main() do
  print(2 + 3 * 4)      # 14 (mul first)
  print((2 + 3) * 4)    # 20 (parens override)
end
```

See: [EXPRESSIONS.md#precedence-and-associativity](EXPRESSIONS.md)

## How to Use This Documentation

1. **New to a-lang?** Start with [SPECIFICATION.md](SPECIFICATION.md)
2. **Learning syntax?** Read [LEXICAL_CONVENTIONS.md](LEXICAL_CONVENTIONS.md)
3. **Need operator info?** See [EXPRESSIONS.md](EXPRESSIONS.md)
4. **Type questions?** Check [DATA_TYPES.md](DATA_TYPES.md)
5. **Function details?** Read [STATEMENTS_AND_FUNCTIONS.md](STATEMENTS_AND_FUNCTIONS.md)
6. **Specific topic?** Use the Topic Index above

## Feedback and Updates

This specification may be updated as the language evolves. Check the version number and dates when referencing.
