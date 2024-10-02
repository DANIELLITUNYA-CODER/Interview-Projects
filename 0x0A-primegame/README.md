# 0x0A. Prime Game

## Overview

This project involves solving a game scenario where players strategically remove prime numbers and their multiples from a set of consecutive integers. You will leverage your understanding of **prime numbers**, **game theory**, and **algorithm optimization** to determine the winner. The challenge involves implementing an efficient solution in Python that determines the winner based on optimal play.

## Game Description

Maria and Ben take turns playing a game where they choose a prime number from a set of consecutive integers starting from 1 to `n`. Upon selecting a prime number, they remove that number and all its multiples from the set. The player who cannot make a move loses the game. The game is played for `x` rounds, each with a different value of `n`.

### Objective

For each round, determine the winner, assuming both Maria and Ben play optimally. Maria always goes first.

### Function Prototype

```python
def isWinner(x, nums):
```

- `x`: Number of rounds.
- `nums`: Array containing the upper limit `n` for each round.
- **Return**: The name of the player with the most wins, or `None` if no clear winner.

### Example

```python
x = 3
nums = [4, 5, 1]

# Expected output:
# Maria wins round 2, Ben wins rounds 1 and 3.
# Overall winner: Ben
```

## Requirements

- Python version: `python3 (version 3.4.3)`
- Files interpreted/compiled on **Ubuntu 20.04 LTS**.
- All files should end with a new line.
- First line of each file must be `#!/usr/bin/python3`.
- Code should follow **PEP 8** style guidelines (version 1.7.x).
- Files must be executable.

## Tasks

### 0. Prime Game (mandatory)

- Implement the function `isWinner(x, nums)` to determine the winner after `x` rounds.
- The function must return:
  - The name of the player (`Maria` or `Ben`) who won the most rounds.
  - `None` if the result is inconclusive.

### Example Usage:

```bash
$ cat main_0.py
#!/usr/bin/python3
isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
$ ./main_0.py
Winner: Ben
```

### Constraints

- `n` and `x` will not exceed 10,000.
- You cannot import any external packages.

## Concepts Needed

1. **Prime Numbers**:
   - Understanding what prime numbers are.
   - Efficient algorithms for identifying prime numbers within a range.

2. **Sieve of Eratosthenes**:
   - Efficient algorithm for finding all prime numbers up to any given limit.
   - This is crucial for efficiently identifying primes in each round.

3. **Game Theory**:
   - Understanding turn-based games and optimal play strategies.
   - Win conditions based on the game's structure.

4. **Dynamic Programming/Memoization**:
   - Using previously computed results to optimize calculations in future rounds.

5. **Python Programming**:
   - Knowledge of loops, conditionals, arrays, and lists is essential for implementing the game logic.

## Resources

- **Prime Numbers and Sieve of Eratosthenes**:
  - Khan Academy: Introduction to prime numbers.
  - Sieve of Eratosthenes in Python.

- **Game Theory Basics**:
  - Introduction to Game Theory.

- **Dynamic Programming**:
  - What Is Dynamic Programming with Python Examples.

- **Python Documentation**:
  - [Python Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists): Managing lists for tracking game state.

## Additional Resources

- Mock Technical Interview Practice.
- Prime Game Checker released on **Oct 1, 2024, 6:00 AM**.
- Auto-review at the project deadline: **Oct 4, 2024, 6:00 AM**.

## Repository Structure

```
alx-interview/
    └── 0x0A-primegame/
        ├── 0-prime_game.py
        └── main_0.py
```

### License
```
© 2024 ALX, All rights reserved.
```
