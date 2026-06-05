# REC-CS23221

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/) [![NumPy](https://img.shields.io/badge/NumPy-2.x-013243?style=flat-square&logo=numpy&logoColor=white)](https://numpy.org/) [![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/) [![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-11557c?style=flat-square&logo=python&logoColor=white)](https://matplotlib.org/) [![Ruff](https://img.shields.io/badge/Ruff-Linter-D7FF64?style=flat-square&logo=ruff&logoColor=black)](https://github.com/astral-sh/ruff) [![uv](https://img.shields.io/badge/uv-DE5FE9?style=flat-square&logo=python&logoColor=white)](https://github.com/astral-sh/uv) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](https://opensource.org/licenses/MIT) [![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)](https://github.com/Tams3d/REC-CS23221)

**Python Programming Lab (CS23221)** work from Rajalakshmi Engineering College.

## Contents

- [Quick Start](#quick-start)
- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Topics Covered](#topics-covered)
- [About](#about)
- [License](#license)

## Quick Start

[](#quick-start)

```bash
git clone https://github.com/Tams3d/REC-CS23221.git
cd REC-CS23221
python Week-1/COD_1_Swapping.py
```

Each program reads from standard input and prints to standard output. No packages to install for the early weeks.

## Overview

[](#overview)

My submissions for the **Python Programming Lab (CS23221)** at **Rajalakshmi Engineering College**.

> [!NOTE]
> The lab is graded by an online portal that runs each program against hidden test cases, so the code is structured as plain `.py` scripts: read from stdin, print to stdout, exit.

Not every week is here. The repo has the weeks I want to revisit and the problems that taught me something. A few had more than one valid approach and I wanted to keep both.

A few files have more than one solution, or show a refactor in the commit history. That's me working out which version reads better as I understood the problem.

## Repository Structure

[](#repository-structure)

```text
REC-CS23221/
|-- Week-1/        # input/output, types, operators
|-- Week-2.1/      # conditionals
|-- Week-2.2/      # loops and patterns
|-- Week-3/        # strings
|-- Week-4/        # lists
|-- Week-5/        # functions
|-- Week-6/        # tuples
+-- Week-7/        # sets
```

The split between `Week-2.1` and `Week-2.2` matches how the lab portal groups them: conditionals first, then loops as a separate block.

| Tier | Prefix | What it is |
|---|---|---|
| **COD** | `COD_N_*.py` | The basics of the topic. Direct, no tricks. |
| **CY**  | `CY_N_*.py`  | Challenge Yourself. Same topic, more thought required. |
| **PAH** | `PAH_N_*.py` | Practice at Home. Extra exercises for revision. |

## Topics Covered

[](#topics-covered)

- [Week 1](#week-1)
- [Week 2.1](#week-21)
- [Week 2.2](#week-22)
- [Week 3](#week-3)
- [Week 4](#week-4)
- [Week 5](#week-5)
- [Week 6](#week-6)
- [Week 7](#week-7)

### Week 1

[](#week-1)

Input/output, type conversion, and the operators that don't show up in higher-level courses much.

- **Variables and types**: parsing ints and floats, mixing them safely, `int(input())` vs `float(input())` gotchas.
- **Swapping**: tuple unpacking, the `a, b = b, a` trick, printing with f-strings and format specifiers.
- **Complex numbers**: real and imaginary parts, swapping them, basic arithmetic on them.
- **Arithmetic**: salary and allowance problems, delivery cost with rates, interest formulas.
- **Bitwise**: XOR encoding (the classic "swap without a temp" by masking), left shift, target sum verification.

### Week 2.1

[](#week-21)

Decision-making with `if`, `elif`, `else`. No loops here yet.

- **Classification**: even/odd, positive/negative, sign detection.
- **Tiered logic**: slab-based electricity bills, conditional discounts that depend on the total, bonus tiers for salary.
- **Domain mapping**: zodiac sign from birthdate, weather category from temperature, grade from score.
- **Input validation**: guarding operations against out-of-range or invalid choices, error prints.
- **Aggregates with conditions**: max, average, sum across a list with a filter.

### Week 2.2

[](#week-22)

Iteration with `for` and `while`. Patterns, number theory, and stateful programs.

- **Star patterns**: half pyramids, full pyramids, diamonds, hollow squares, symmetric layouts, Floyd's triangle, Pascal's triangle. The classic screen-fill exercises.
- **Number theory**: primes within a range, factorial, digit sums, digit power checks.
- **Menu-driven programs**: print a menu, read a choice, do the thing, loop until exit.
- **State**: seat booking with availability tracking across bookings.
- **Loop variants**: divisor parity, sum of odds up to N, while-loop factorial with a counter.

### Week 3

[](#week-3)

Strings. Slicing, manipulation, formatting quirks.

- **Core operations**: slicing with stride, concatenation, reversal, replacement.
- **Interleaving**: merging two strings character by character.
- **Validation**: pattern checks (digits only, alphanumeric), format verification (length, prefix).
- **Deduplication**: removing repeated characters while keeping the original order.
- **Alignment**: `center`, `ljust`, `rjust`, custom padding characters.
- **Number and string**: digit-by-digit extraction, palindromes (numeric and string), leading zero padding.

### Week 4

[](#week-4)

Lists. The workhorse collection in Python.

- **Rearrangement**: stable partition (negatives before positives, preserving order), right rotation by N, rearranging in place.
- **Search**: smallest missing positive integer, divisor lookup within a list, peak element detection.
- **Comprehensions**: conditional slicing in one line, pair sums with even-only filtering.
- **Aggregates**: sum, average, comparing the sum of the first half against the second half.
- **Mutations**: `append`, `pop` from front and back, `remove` by value, `extend` with another list.

### Week 5

[](#week-5)

Functions. The point where the lab stops being a sequence of scripts.

- **Definitions**: parameters, return values, default arguments.
- **Lambdas**: inline functions for one-liners (even/odd count, filtering).
- **Builtins**: `pow()`, `abs()`, `max()`, `min()`, `sum()`, `map()`, `filter()`.
- **Recursion**: digit sum, vowel count, both as recursive calls.
- **Scope**: global constants for configuration (tax rates, prices, limits).

### Week 6

[](#week-6)

Tuples. Immutable sequences and the operations you can do on them.

- **Construction**: empty tuple, single-element tuple (the trailing comma gotcha), tuple from a list.
- **Selection**: every-nth element, conditional inclusion based on position.
- **Derived tuples**: building a new tuple from a list of differences, pairwise operations.
- **Conversion**: list to tuple, set to tuple, tuple of tuples.

### Week 7

[](#week-7)

Sets. Unordered collections and the algebra you can do with them.

- **Deduplication**: `set()` removes duplicates, sort the result for stable output.
- **Set algebra**: union, intersection, difference, symmetric difference, both via operators (`|`, `&`, `-`, `^`) and methods.
- **Membership**: fast `in` checks against a set vs a list.
- **Iteration**: building a set from a stream of inputs, accumulating across multiple reads.

## About

[](#about)

19. Self-taught. CS at Rajalakshmi Engineering College.

I'm interested in DSA, competitive programming, and ML. I learn by writing code that runs and re-reading it line by line. This repo is part of that.

## License

[](#license)

MIT - free to use, study, and modify. See [LICENSE](LICENSE) for the full text.
