from dataclasses import dataclass
from typing import Callable, List, NamedTuple


@dataclass
class Box:
    """
    Represents a box with length, width, and height.
    """

    length: int
    width: int
    height: int

    def __post_init__(self):
        """
        Calculate additional properties after box initialization.
        """
        self.area_1 = self.length * self.width
        self.area_2 = self.width * self.height
        self.area_3 = self.height * self.length
        self.min_area = min(self.area_1, self.area_2, self.area_3)
        sides = [self.length, self.width, self.height]
        sides.sort()
        self.min_lengths = sides[:2]

    def compute_surface(self) -> int:
        """
        Compute the total surface area of the box.

        Returns:
            int: The total surface area.
        """
        return 2 * (self.area_1 + self.area_2 + self.area_3) + self.min_area

    def compute_ribbon_length(self) -> int:
        """
        Compute the total ribbon length needed for the box.

        Returns:
            int: The total ribbon length.
        """
        return 2 * sum(self.min_lengths) + (self.length * self.width * self.height)


class TestCase(NamedTuple):
    """
    Represents a test case with input and expected output.
    """

    input: str
    output: int


def parse_string_input(input_str: str) -> Box:
    """
    Parse the dimensions from the input string and create a Box object.

    Args:
        input_str (str): The input string in the format "length x width x height".

    Returns:
        Box: A Box object with the specified dimensions.
    """
    length, width, height = map(int, input_str.split("x"))
    return Box(length, width, height)


def compute_required_surface(input_str: str) -> int:
    """
    Compute the total surface area required based on the box dimensions.

    Args:
        input_str (str): The input string in the format "length x width x height".

    Returns:
        int: The total surface area required.
    """
    box = parse_string_input(input_str)
    return box.compute_surface()


def compute_required_ribbon(input_str: str) -> int:
    """
    Compute the total ribbon length needed based on the box dimensions.

    Args:
        input_str (str): The input string in the format "length x width x height".

    Returns:
        int: The total ribbon length needed.
    """
    box = parse_string_input(input_str)
    return box.compute_ribbon_length()


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


# Part 1
tests_part1 = [TestCase("2x3x4", 58), TestCase("1x1x10", 43)]

run_tests(tests_part1, compute_required_surface)

with open("input.txt", "r") as file:
    data_part1 = file.read().splitlines()

total_surface_area = sum(compute_required_surface(line) for line in data_part1)
print(total_surface_area)

# Part 2
tests_part2 = [TestCase("2x3x4", 34), TestCase("1x1x10", 14)]

run_tests(tests_part2, compute_required_ribbon)

with open("input.txt", "r") as file:
    data_part2 = file.read().splitlines()

total_ribbon_length = sum(compute_required_ribbon(line) for line in data_part2)
print(total_ribbon_length)
