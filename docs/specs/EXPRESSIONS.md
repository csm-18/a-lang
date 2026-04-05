# Expression Specification

Detailed specification of expressions in a-lang.

## Overview

Expressions are sequences of operators and operands that evaluate to a value. All expressions in a-lang evaluate to a single value of type `number`, `string`, or `boolean`.

## Expression Categories

### Primary Expressions

Expressions that don't contain operators:

| Expression | Type | Example |
|-----------|------|---------|
| Number literal | `number` | `42` |
| String literal | `string` | `"hello"` |
| Boolean literal | `boolean` | `true` |
| Identifier | (varies) | `x` |
| Parenthesized | (same as inner) | `(expr)` |

### Composite Expressions

Expressions containing operators:

- Arithmetic expressions

## Arithmetic Expressions

### Operators

| Operator | Description | Precedence | Associativity | Input Types | Result Type |
|----------|-------------|-----------|---------------|-------------|-------------|
| `+` | Addition | 1 (lower) | Left | number, number | number |
| `-` | Subtraction | 1 (lower) | Left | number, number | number |
| `*` | Multiplication | 2 (higher) | Left | number, number | number |
| `/` | Division | 2 (higher) | Left | number, number | number |

### Precedence and Associativity

**Precedence** (highest to lowest):

1. Parenthesized expressions, literals, identifiers
2. `*`, `/` (multiplication/division)
3. `+`, `-` (addition/subtraction)

**Associativity:** All operators are left-associative.

### Evaluation Examples

```
3 + 4
→ 7

5 * 2 - 1
→ (5 * 2) - 1    (multiplication first, then subtraction)
→ 10 - 1
→ 9

2 + 3 * 4
→ 2 + (3 * 4)    (multiplication before addition)
→ 2 + 12
→ 14

(2 + 3) * 4
→ 5 * 4          (parentheses override precedence)
→ 20

10 - 5 - 2
→ (10 - 5) - 2   (left-to-right associativity)
→ 5 - 2
→ 3

10 / 2 / 5
→ (10 / 2) / 5   (left-to-right associativity)
→ 5 / 5
→ 1
```

### Division Semantics

- **Operation:** Integer division (truncation toward zero)
- **Rounding:** Truncates fractional part
- **Zero divisor:** Undefined behavior (compiler doesn't check)

Examples:

```
10 / 3  → 3
7 / 2   → 3
1 / 2   → 0
-10 / 3 → -3
10 / 10 → 1
0 / 5   → 0
```

### Operator Validation

All arithmetic operators require both operands to be of type `number`.

Invalid:

```
"hello" + 5          # ERROR: Cannot add string and number
true * false         # ERROR: Cannot multiply booleans
"3" + "4"            # ERROR: No string concatenation
```

## Parentheses

Parentheses `( expr )` group expressions and override precedence.

Examples:

```
(2 + 3) * 4          # Parentheses force addition first
((1 + 2) * 3) + 4    # Nested parentheses
(42)                 # Valid but redundant
((((5))))            # Valid but unusual
```

Unmatched parentheses are a syntax error.

## Type Consistency

All operands in an expression must be compatible with the operator.

- Arithmetic operators require `number` operands
- Result is always `number`
- No implicit type conversion

## Expression Context

Expressions can appear in:

- **Call statements:** `print(expr)`, `foo(expr)`
- **Nested expressions:** `(expr op expr)`

Expressions **cannot** appear in:

- Variable declarations (no variables yet)
- Conditionals (no conditionals yet)
- Return statements (no returns yet)

## Complex Nested Expressions

Examples with multiple levels of nesting:

```
(1 + 2) * (3 + 4)
→ 3 * 7
→ 21

((1 + 2) * 3) / (2 + 1)
→ (3 * 3) / 3
→ 9 / 3
→ 3

1 + 2 * 3 - 4 / 2 + 5
→ 1 + (2 * 3) - (4 / 2) + 5
→ 1 + 6 - 2 + 5
→ ((1 + 6) - 2) + 5
→ (7 - 2) + 5
→ 5 + 5
→ 10
```

## Non-Expressions

In a-lang, the following are **not** expressions:

- Variable names (no variables)
- Function calls (cannot call user functions)
- Assignments (no variables)
- Boolean operators like `&&`, `||`, `!`
- Comparison operators like `==`, `!=`, `<`, `>`
- Conditional expressions like `? :`

## Evaluation Guarantees

- **Left-to-right evaluation:** For operators of equal precedence
- **Parentheses:** Always respected
- **No side effects:** Expression evaluation doesn't affect program state
- **No short-circuit:** All operands are fully evaluated

## Error Conditions

Compile-time errors:

- Type mismatch in operators (e.g., `"x" + 5`)
- Unmatched parentheses
- Invalid tokens

Runtime undefined behavior:

- Division by zero: C runtime behavior
- Integer overflow: C int overflow behavior

## Grammar

```
expression      → term (("+"|"-") term)*

term            → factor (("*"|"/") factor)*

factor          → "(" expression ")"
                | NUMBER
                | STRING
                | BOOLEAN
                | IDENTIFIER

NUMBER          → [0-9]+
STRING          → "\"" ... "\""
BOOLEAN         → "true" | "false"
IDENTIFIER      → [a-zA-Z_][a-zA-Z0-9_]*
```
