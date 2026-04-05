# Statements and Functions Specification

Detailed specification of statements and functions in a-lang.

## Statements

### Overview

A statement is an instruction that performs an action. Statements are the basic executable units in a-lang.

### Statement Types

#### Call Statement

**Syntax:** `identifier ( expression )`

Invokes a built-in function with a single argument.

**Current Built-in Functions:**

- `print(expr)` - Output a value

**Examples:**

```
print(42)
print("Hello")
print(3 + 4)
print(true)
```

**Restrictions:**

- Only one built-in function: `print`
- Only one argument per call
- Argument can be any expression

### Statement Sequencing

**Syntax:** Multiple statements in sequence

Statements are executed in the order they appear, top to bottom.

```
main() do
  print(1)
  print(2)
  print(3)
end
```

Output:
```
1
2
3
```

### Empty Statements

a-lang does **not** support empty statements. Every statement must be a valid call.

Invalid:

```
main() do
  ;           # ERROR
  print(1)
end
```

## Functions

### Function Definition

**Syntax:**

```
main() do
  <statements>
end
```

**Structure:**

- **Keyword:** `main` (identifier, currently required)
- **Parameters:** `()` (must be empty)
- **Body:** `do...end` block
- **Statements:** Zero or more statements

### Current Restrictions

1. **Single Function:** Only `main()` can be defined
2. **No Parameters:** `()` must be empty
3. **No Return Value:** Functions don't return values
4. **No Recursion:** Cannot call user-defined functions

### Function Body

The body contains a sequence of statements executed in order.

**Examples:**

```
main() do
  print("First")
  print("Second")
end
```

```
main() do
end
```

(Empty function is valid)

### Entry Point

The program starts execution at `main()`.

If `main()` is not defined, the compiler will fail.

### Scope

a-lang has no concept of scope (no variables yet).

## Built-in Functions

### print()

**Signature:** `print(expr: any) → void`

Outputs the value of the expression, followed by a newline.

**Parameters:**

- `expr`: An expression of any type (number, string, or boolean)

**Output Behavior:**

| Type | Output Format |
|------|---------------|
| number | Decimal integer |
| string | String content with escapes interpreted |
| boolean | "true" or "false" |

**Examples:**

```
print(42)                       # Output: 42
print("Hello, World!")          # Output: Hello, World!
print(3 + 4)                    # Output: 7
print(true)                     # Output: true
print("Line 1\nLine 2")         # Output: Line 1
                                #         Line 2
```

**Side Effects:**

- Writes to standard output
- Adds newline after each call
- No return value

**Limitations:**

- Exactly one argument (no overloading)
- No format specifiers
- No multiple arguments

## Future Function Support (Not Yet Implemented)

These features are planned for future releases:

### User-Defined Functions

```
factorial(n) do
  ...
end

main() do
  print(factorial(5))
end
```

### Function Parameters

```
add(a, b) do
  ...
end
```

### Function Return Values

```
square(x) do
  return x * x
end
```

### Function Calls

```
main() do
  result = foo(42)
  print(result)
end
```

## Execution Model

### Program Startup

1. Compiler parses and compiles the source
2. Generated C program is compiled via GCC
3. Binary is executed
4. `main()` is called (by C runtime)
5. Statements in `main()` execute in order

### Program Termination

- After last statement in `main()` completes
- Exit code: 0 (success)

### Error Handling

- Compile-time errors: Compiler prints error and exits with code 1
- Runtime errors: Undefined behavior (depends on C runtime)

## Grammar

```
program         → function

function        → IDENTIFIER "(" ")" "do" statements "end"

statements      → statement*

statement       → call_statement

call_statement  → IDENTIFIER "(" expression ")"

expression      → ... (see EXPRESSIONS.md)

IDENTIFIER      → [a-zA-Z_][a-zA-Z0-9_]*
```

## Restrictions on Function Names

Valid function names:
- Must be a valid identifier
- Currently only `main` is recognized by runtime

Invalid names:
- Keywords: `do`, `end`, `true`, `false`, `bool`, `string`
- Built-in functions: `print` (reserved for print statements)

## Example Programs

### Minimal Program

```
main() do
end
```

Output: (nothing)

### Single Statement

```
main() do
  print("Hello")
end
```

Output: `Hello`

### Multiple Statements

```
main() do
  print(1)
  print(2)
  print(3)
end
```

Output:
```
1
2
3
```

### With Expressions

```
main() do
  print(2 + 3)
  print(10 * 5)
  print("Done")
end
```

Output:
```
5
50
Done
```

### Mixed Types

```
main() do
  print("Answer:")
  print(2 + 2)
  print("Bool:")
  print(true)
end
```

Output:
```
Answer:
4
Bool:
true
```
