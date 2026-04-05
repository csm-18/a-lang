# a-lang

a-lang is a minimal, statically-typed toy programming language designed to demonstrate compiler fundamentals. It compiles to C code which is then compiled to a native binary using GCC.

**Features:**
- Simple, readable syntax
- Support for numbers, strings, and booleans
- Arithmetic expressions with operator precedence
- Function definitions and print statements
- Clear error messages with file, line, and column information

## Development Environment & Dependencies

### Requirements
- OS: Linux
- Python 3.6 or higher
- GCC (for compiling generated C code)

### Setup

Clone the repository:
```bash
git clone <repository-url>
cd a-lang
```

No additional Python packages are required - the compiler uses only Python's standard library.

## Compiler Usage

### Command Line Interface

```bash
python3 main.py <command>
```

**Available Commands:**

- `python3 main.py <filename.a>` - Compile an a-lang source file to a binary
- `python3 main.py version` - Print compiler version
- `python3 main.py help` - Print available commands
- `python3 main.py` - Show about message and help

### Example

```bash
python3 main.py examples/hello.a
./hello
```

## Example Code

### Hello World

**examples/hello.a:**
```
main() do
  print(23)
end
```

Compile and run:
```bash
python3 main.py examples/hello.a
./hello
```

Output:
```
23
```

### Arithmetic Expressions

**examples/math.a:**
```
main() do
  print(3 + 4)
  print(5 * 2 - 1)
  print(8 / 2)
end
```

Compile and run:
```bash
python3 main.py examples/math.a
./math
```

Output:
```
7
9
4
```

### Strings

**examples/string.a:**
```
main() do
  print("Hello, World!")
end
```

### Booleans

**examples/bool.a:**
```
main() do
  print(true)
  print(false)
end
```

## Language Syntax

### Basic Structure

```
main() do
  <statements>
end
```

### Expressions

a-lang supports the following expressions:

- **Numbers:** Integer literals (e.g., `42`, `0`, `1337`)
- **Strings:** String literals in double quotes (e.g., `"hello"`)
- **Booleans:** `true` and `false`
- **Arithmetic:** `+`, `-`, `*`, `/` with standard precedence
- **Grouping:** Use parentheses `()` for explicit grouping

### Operator Precedence

| Precedence | Operators |
|-----------|-----------|
| Highest   | `*`, `/`  |
| Lower     | `+`, `-`  |

### Comments

Use `#` for single-line comments:
```
# This is a comment
main() do
  print(42)  # Print the answer
end
```

## Project Structure

```
a-lang/
├── main.py                          # Entry point and CLI
├── compiler/
│   ├── __init__.py                 # Package marker
│   ├── compiler.py                 # Main compilation pipeline
│   ├── lexer.py                    # Lexical analyzer (tokenizer)
│   ├── parser.py                   # Parser (AST generation)
│   └── code_gen.py                 # Code generator (C output and compilation)
├── examples/                        # Example programs
│   ├── hello.a                     # Hello world example
│   ├── math.a                      # Arithmetic expressions example
│   ├── string.a                    # String example
│   └── bool.a                      # Boolean example
├── tests/                           # Comprehensive test suite
│   ├── test_runner.py              # Test runner script
│   ├── test_arithmetic.json        # Arithmetic test specifications
│   ├── test_types.json             # Type test specifications
│   ├── arithmetic/                 # Arithmetic test programs (13 tests)
│   │   ├── single_number.a
│   │   ├── addition.a
│   │   ├── subtraction.a
│   │   ├── multiplication.a
│   │   ├── division.a
│   │   ├── precedence_mul_add.a
│   │   ├── add_then_mul.a
│   │   ├── complex_expr.a
│   │   ├── parentheses_override.a
│   │   ├── nested_parens.a
│   │   ├── left_to_right.a
│   │   ├── with_zero.a
│   │   └── large_numbers.a
│   └── types/                      # Type test programs (5 tests)
│       ├── string_literal.a
│       ├── bool_true.a
│       ├── bool_false.a
│       ├── multiple_strings.a
│       └── string_special.a
├── .gitignore
├── LICENSE
└── README.md
```

## Testing

Comprehensive test suite covering arithmetic expressions, type handling, and edge cases.

### Running Tests

```bash
python3 tests/test_runner.py
```

### Test Coverage

**Arithmetic Tests (13 tests):**
- Basic operations: addition, subtraction, multiplication, division
- Operator precedence (multiplication before addition)
- Parentheses and grouping
- Complex expressions with multiple operators
- Left-to-right evaluation
- Edge cases: zero, large numbers

**Type Tests (5 tests):**
- String literals and escaping
- Boolean values (true/false)
- Multiple statements
- Special characters in strings

### Test Structure

Tests are defined in JSON format (`tests/test_*.json`) with corresponding test programs in subdirectories:

```
tests/
├── test_runner.py           # Test runner script
├── test_arithmetic.json     # Arithmetic test specifications
├── test_types.json          # Type test specifications
├── arithmetic/              # Arithmetic test programs
└── types/                   # Type test programs
```

Each test specifies a source file, expected output, and optionally whether it should fail during compilation.

## How It Works

1. **Lexing:** The source code is tokenized into a stream of tokens
2. **Parsing:** Tokens are parsed into an Abstract Syntax Tree (AST)
3. **Code Generation:** The AST is traversed and converted to C code
4. **Compilation:** GCC compiles the generated C code to a native binary

The temporary C file is automatically cleaned up after compilation.
