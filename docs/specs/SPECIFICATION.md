# a-lang Language Specification

Complete specification of the a-lang programming language.

## Table of Contents

1. [Lexical Conventions](#lexical-conventions)
2. [Data Types](#data-types)
3. [Expressions](#expressions)
4. [Statements](#statements)
5. [Functions](#functions)
6. [Built-in Functions](#built-in-functions)
7. [Grammar](#grammar)

---

## Lexical Conventions

### Comments

Comments start with `#` and extend to the end of the line:

```
# This is a comment
main() do
  print(42)  # Inline comment
end
```

Comments cannot appear inside strings.

### Identifiers

An identifier is a sequence of letters, digits, and underscores, starting with a letter or underscore.

Valid: `main`, `_private`, `foo_bar`, `var123`
Invalid: `123var`, `-name`, `foo-bar`

### Keywords

Reserved keywords that cannot be used as identifiers:

| Keyword | Purpose |
|---------|---------|
| `do` | Start function body |
| `end` | End function body |
| `true` | Boolean literal |
| `false` | Boolean literal |
| `bool` | Boolean type keyword |
| `string` | String type keyword |

### Literals

#### Number Literals

Integer literals only. Decimal numbers without signs.

Valid: `0`, `42`, `1000`, `9999`
Invalid: `-5`, `3.14`, `0x10`

#### String Literals

Strings are enclosed in double quotes and can contain:

- Regular ASCII characters
- Escape sequences:
  - `\\` - Backslash
  - `\"` - Double quote
  - `\n` - Newline
  - `\t` - Tab

Invalid characters: None explicitly forbidden, but unescaped quotes will terminate the string prematurely.

Examples:
```
"Hello, World!"
"Line 1\nLine 2"
"Path: C:\\Users\\name"
"Quote: \"Hello\""
```

#### Boolean Literals

`true` and `false`

### Tokens

Whitespace (space, tab, newline, carriage return) is ignored except where it separates tokens.

---

## Data Types

a-lang supports three data types:

### Number

- **Description:** Signed 32-bit integers
- **Literals:** `42`, `0`, `-5`
- **Operations:** Can be used in arithmetic expressions
- **String Representation:** Printed as decimal integers

### String

- **Description:** Sequence of characters
- **Literals:** `"hello"`, `""`
- **Operations:** Limited to print; no string concatenation
- **String Representation:** Printed as-is

### Boolean

- **Description:** Truth value
- **Literals:** `true`, `false`
- **Operations:** Limited to print; displays as "true" or "false"
- **String Representation:** Printed as "true" or "false"

---

## Expressions

### Overview

Expressions are evaluated left-to-right with operator precedence. Parentheses can override precedence.

### Primary Expressions

| Expression | Type | Example |
|-----------|------|---------|
| Number literal | number | `42` |
| String literal | string | `"hello"` |
| Boolean literal | boolean | `true`, `false` |
| Identifier | varies | `x` |
| Grouped expression | varies | `(expr)` |

### Arithmetic Expressions

**Operators (in precedence order):**

| Precedence | Operators | Associativity |
|-----------|-----------|---------------|
| Higher | `*`, `/` | Left-to-right |
| Lower | `+`, `-` | Left-to-right |

**Operator Behavior:**

- `+` Addition of two numbers
- `-` Subtraction of two numbers
- `*` Multiplication of two numbers
- `/` Integer division (truncates toward zero)

**Examples:**

```
3 + 4           # 7
5 * 2 - 1       # 9
2 + 3 * 4       # 14 (multiplication first)
(2 + 3) * 4     # 20 (parentheses override)
10 / 2 / 5      # 1 (left-to-right: (10/2)/5)
```

### Type Requirements

- Operands must be numbers
- Cannot mix types (e.g., `"hello" + 5` is invalid)
- Result is always a number

---

## Statements

### Overview

A statement is the basic unit of execution. Currently, only call statements are supported.

### Call Statement

Syntax: `identifier ( expression )`

Calls a built-in function with a single expression argument.

Example:
```
print(42)
print("Hello")
print(3 + 4)
```

### Statement Sequence

Multiple statements are executed in order:

```
main() do
  print(1)
  print(2)
  print(3)
end
```

---

## Functions

### Function Definition

Syntax:
```
main() do
  <statements>
end
```

**Current Limitations:**

- Only one function: `main()`
- No parameters
- No return values
- Empty parameter list: `()`
- Body enclosed in `do...end`

### Function Body

- Contains zero or more statements
- Statements executed in sequence
- No explicit return

Example:
```
main() do
  print("First")
  print("Second")
  print("Third")
end
```

---

## Built-in Functions

### print

Outputs a value followed by a newline.

**Signature:** `print(expr)`

**Parameters:**
- `expr`: Any expression (number, string, or boolean)

**Output:**
- Numbers: Printed as decimal integers
- Strings: Printed as-is with escape sequences interpreted
- Booleans: Printed as "true" or "false"

**Examples:**

```
print(42)                   # Output: 42
print("Hello, World!")      # Output: Hello, World!
print(3 + 4)                # Output: 7
print(true)                 # Output: true
print("Line 1\nLine 2")     # Output: Line 1
                            #         Line 2
```

**Current Limitation:** Only one argument supported.

---

## Grammar

### Formal Grammar (BNF-like)

```
program          → function

function         → IDENTIFIER "(" ")" "do" statements "end"

statements       → statement*

statement        → call_statement

call_statement   → IDENTIFIER "(" expression ")"

expression       → term (("+"|"-") term)*

term             → factor (("*"|"/") factor)*

factor           → NUMBER
                 | STRING
                 | BOOLEAN
                 | IDENTIFIER
                 | "(" expression ")"

IDENTIFIER       → [a-zA-Z_][a-zA-Z0-9_]*
NUMBER           → [0-9]+
STRING           → "\"" (<char>|<escape>)* "\""
BOOLEAN          → "true" | "false"
```

### Escape Sequences in Strings

```
escape           → "\\" | "\"" | "\n" | "\t"
```

---

## Type System

a-lang uses **static typing** at compile time but does **not require explicit type annotations**.

### Type Compatibility

| Operation | Valid Types | Result Type |
|-----------|------------|-------------|
| `+` | number, number | number |
| `-` | number, number | number |
| `*` | number, number | number |
| `/` | number, number | number |
| `print()` | any | (side effect) |

---

## Compilation and Execution

### Compilation Process

1. **Lexing:** Source code → Tokens
2. **Parsing:** Tokens → Abstract Syntax Tree
3. **Code Generation:** AST → C code
4. **Compilation:** C code → Binary (via GCC)

### Execution Model

- Program starts at `main()`
- Statements execute in order
- Output via `print()`
- Program exits with code 0

---

## Limitations and Constraints

### Currently Not Supported

- Variables and variable declaration
- Type annotations
- Conditionals (if/else)
- Loops (while, for)
- Multiple functions
- Function parameters
- Return statements
- Arrays
- Objects
- String concatenation
- Boolean operators
- Comparison operators

### Parser Constraints

- No error recovery; first error stops compilation
- Limited error messages
- No warnings

### Runtime Constraints

- 32-bit signed integer overflow behavior follows C semantics
- Division by zero results in undefined behavior

---

## Examples

### Hello World

```
main() do
  print("Hello, World!")
end
```

### Arithmetic

```
main() do
  print(2 + 3)
  print(10 - 4)
  print(3 * 7)
  print(20 / 4)
end
```

### Mixed Types

```
main() do
  print("Answer: ")
  print(2 + 2)
  print(true)
  print("Done")
end
```

### Complex Expression

```
main() do
  print(1 + 2 * 3 + 4)
  print((10 + 5) * 2)
  print(100 / (2 + 3))
end
```
