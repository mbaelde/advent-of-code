import re
from pathlib import Path
from typing import List


def part_1(data: List[str]) -> int:
    # Part 1
    calibration = []
    for line in data:
        digits = re.sub("[^1-9]", "", line)
        number = int(f"{digits[0]}{digits[-1]}")
        calibration.append(number)

    calibration_value = sum(calibration)
    return calibration_value


def part_2(data: List[str]) -> int:
    # Part 2
    correction_map = {
        "one": "one1one",
        "two": "two2two",
        "three": "three3three",
        "four": "four4four",
        "five": "five5five",
        "six": "six6six",
        "seven": "seven7seven",
        "eight": "eight8eight",
        "nine": "nine9nine",
    }
    number_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    calibration = []
    for line in data:
        for number_, correction_ in correction_map.items():
            line = line.replace(number_, correction_)
        for number_, digit_ in number_map.items():
            line = line.replace(number_, digit_)
        digits = re.sub("[^1-9]", "", line)
        number = int(f"{digits[0]}{digits[-1]}")
        calibration.append(number)

    calibration_value = sum(calibration)
    return calibration_value


def test():
    with open(Path(__file__).parent.joinpath("test_1.txt"), "r") as file:
        data = file.read().splitlines()
    calibration_value = part_1(data)
    assert calibration_value == 142

    with open(Path(__file__).parent.joinpath("test_2.txt"), "r") as file:
        data = file.read().splitlines()
    calibration_value = part_2(data)
    assert calibration_value == 281
    print("Tests OK")


if __name__ == "__main__":
    test()

    with open(Path(__file__).parent.joinpath("input.txt"), "r") as file:
        data = file.read().splitlines()
    calibration_value = part_1(data)
    print(f"part1: {calibration_value}")
    # réponse : 55029

    calibration_value = part_2(data)
    print(f"part2: {calibration_value}")
    # réponse : 55686
