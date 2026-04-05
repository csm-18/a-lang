# Data Types Specification

Detailed specification of a-lang data types.

## Overview

a-lang has three built-in data types: `number`, `string`, and `boolean`.

## Number Type

### Definition

A signed 32-bit integer value.

### Literals

- **Format:** Sequence of decimal digits `[0-9]+`
- **Range:** -2,147,483,648 to 2,147,483,647
- **Examples:** `0`, `42`, `1000`, `999999`

### Representation

Numbers are stored as C `int` (typically 32-bit signed).

### Operations

- **Arithmetic:** `+`, `-`, `*`, `/`
- **Print:** Outputs as decimal integer

### Examples

```
print(42)                  # 42
print(3 + 4)               # 7
print(10 * 5)              # 50
print(100 / 3)             # 33 (integer division)
```

## String Type

### Definition

An immutable sequence of characters.

### Literals

**Syntax:** `" <content> "`

- Enclosed in double quotes
- Can be empty: `""`

### Valid Characters

Printable ASCII characters (0x20 to 0x7E) plus escaped sequences:

- Letters: `a-z`, `A-Z`
- Digits: `0-9`
- Punctuation: `! @ # $ % ^ & * ( ) - _ = + [ ] { } ; : ' , . < > ? / | \ ~ \``
- Space: ` `

### Escape Sequences

| Escape | Meaning | Output |
|--------|---------|--------|
| `\\` | Backslash | `\` |
| `\"` | Double quote | `"` |
| `\n` | Newline | (line break) |
| `\t` | Tab | (4 spaces typically) |

### Invalid Content

- Unescaped double quote (`"`) terminates string
- No null characters (`\0`)
- No Unicode support (ASCII only)

### Examples

```
print("Hello")                          # Hello
print("Path: C:\\Users\\name")          # Path: C:\Users\name
print("Quote: \"Hello\"")               # Quote: "Hello"
print("Line 1\nLine 2")                 # Line 1
                                        # Line 2
print("Tab\tSeparated")                 # Tab    Separated
print("")                               # (empty line)
```

### Storage

Strings are immutable. No string concatenation or manipulation operations exist.

## Boolean Type

### Definition

A truth value: either true or false.

### Literals

- `true` - Represents true
- `false` - Represents false

### Storage

Stored as C `bool` (1 byte).

### Operations

- **Print:** Outputs "true" or "false"

### Examples

```
print(true)                # true
print(false)               # false
```

## Type Coercion

a-lang does **not perform implicit type coercion**.

Invalid operations:

```
print("Number: " + 42)    # ERROR: Cannot add string and number
print(true + 1)            # ERROR: Cannot add boolean and number
print("true" == true)      # ERROR: No equality operator
```

## Default Values

a-lang has no variable declaration; this section is N/A.

## Type Checking

Type checking occurs at:

1. **Compile Time (during parsing/codegen):**
   - Arithmetic operators check operands are numbers
   - print() accepts any type

2. **Runtime:** No type checking (already verified at compile time)

## Comparison with C

| a-lang | C | Notes |
|--------|---|-------|
| number | int | 32-bit signed |
| string | char* | Null-terminated in C |
| boolean | bool | True/false |
