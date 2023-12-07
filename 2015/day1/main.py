from collections import Counter
from typing import NamedTuple

import pandas as pd

# Part 1
def compute_direction(input_str: str) -> int:
    """
    Compute the floor direction based on the input string.

    Args:
        input_str (str): The input string containing parentheses.

    Returns:
        int: The floor direction (positive for up, negative for down).
    """
    count = Counter(input_str)
    return count["("] - count[")"]

TestCase = NamedTuple("TestCase", [("input", str), ("output", int)])

tests = [
    TestCase("(())", 0),
    TestCase("()()", 0),
    TestCase("(((", 3),
    TestCase("(()(()(", 3),
    TestCase("))(((((", 3),
    TestCase("())", -1),
    TestCase("))(", -1),
    TestCase(")))", -3),
    TestCase(")())())", -3),
]

with open("input.txt", "r") as file:
    data = file.read()

direction_map = {"(": 1, ")": -1}

for test in tests:
    assert compute_direction(test.input) == test.output

print(compute_direction(data))

# Part 2
tests = [
    TestCase(")", 1),
    TestCase("()())", 5),
]

def compute_basement_position(input_str: str) -> int:
    """
    Compute the position where Santa first enters the basement.

    Args:
        input_str (str): The input string containing parentheses.

    Returns:
        int: The position where Santa first enters the basement.
    """
    cumulative_sum = pd.Series([c for c in input_str]).map(direction_map).cumsum()
    return (cumulative_sum == -1).idxmax() + 1

for test in tests:
    assert compute_basement_position(test.input) == test.output

print(compute_basement_position(data))
