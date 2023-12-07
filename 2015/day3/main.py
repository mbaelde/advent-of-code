from dataclasses import dataclass
from typing import Callable, List, NamedTuple


class TestCase(NamedTuple):
    """
    Represents a test case with input and expected output.
    """

    input: str
    output: int


def run_tests(test_cases: List[TestCase], compute_function: Callable[[str], int]):
    """
    Run a set of test cases for a given compute function.

    Args:
        test_cases (List[TestCase]): List of NamedTuples containing input and expected output.
        compute_function (Callable[[str], int]): The function to be tested.
    """
    for test_case in test_cases:
        result = compute_function(test_case.input)
        assert result == test_case.output


@dataclass
class Position:
    """
    Represents a position with coordinates (x, y).
    """

    x: int = 0
    y: int = 0

    def step(self, char: str) -> None:
        """
        Update the position based on the given character.

        Args:
            char (str): The character representing the movement direction.
        """
        match char:
            case "^":
                self.y += 1
            case "v":
                self.y -= 1
            case "<":
                self.x -= 1
            case ">":
                self.x += 1

    def __hash__(self) -> int:
        """
        Compute the hash of the position.

        Returns:
            int: The hash value.
        """
        return hash((self.x, self.y))

    @property
    def coordinates(self) -> tuple[int, int]:
        """
        Get the coordinates of the position.

        Returns:
            tuple[int, int]: The (x, y) coordinates.
        """
        return (self.x, self.y)


def compute_n_houses_delivered(input_str: str) -> int:
    """
    Compute the number of houses delivered to at least once.

    Args:
        input_str (str): The input string representing movements.

    Returns:
        int: The number of houses delivered to at least once.
    """
    position = Position()
    map_var: List[Position] = [position.coordinates]
    for c in input_str:
        position.step(c)
        map_var.append(position.coordinates)
    n_houses = len(set(map_var))
    return n_houses


# Part 1
tests_part1 = [TestCase(">", 2), TestCase("^>v<", 4), TestCase("^v^v^v^v^v", 2)]

run_tests(tests_part1, compute_n_houses_delivered)

with open("input.txt", "r") as file:
    data_part1 = file.read()

total_houses = compute_n_houses_delivered(data_part1)
print(total_houses)

# Part 2
def compute_n_houses_delivered_robo(input_str: str) -> int:
    """
    Compute the number of houses delivered to at least once with Robo-Santa.

    Args:
        input_str (str): The input string representing movements.

    Returns:
        int: The number of houses delivered to at least once.
    """
    position_santa = Position()
    position_robosanta = Position()
    map_var: List[Position] = [position_santa.coordinates]
    for i, c in enumerate(input_str):
        if i % 2 == 0:
            position_santa.step(c)
            map_var.append(position_santa.coordinates)
        else:
            position_robosanta.step(c)
            map_var.append(position_robosanta.coordinates)
    n_houses = len(set(map_var))
    return n_houses


tests_part2 = [TestCase("^v", 3), TestCase("^>v<", 3), TestCase("^v^v^v^v^v", 11)]

run_tests(tests_part2, compute_n_houses_delivered_robo)

total_houses = compute_n_houses_delivered_robo(data_part1)
print(total_houses)
