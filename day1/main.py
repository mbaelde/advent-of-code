import re

with open("input.txt", "r") as file:
    lines = file.read().splitlines()

# Part 1
calibration = []
for line in lines:
    digits = re.sub("[^1-9]", "", line)
    number = int(f"{digits[0]}{digits[-1]}")
    calibration.append(number)

calibration_value = sum(calibration)
print(f"part1: {calibration_value}")
# réponse : 55029

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
for line in lines:
    for number_, correction_ in correction_map.items():
        line = line.replace(number_, correction_)
    for number_, digit_ in number_map.items():
        line = line.replace(number_, digit_)
    digits = re.sub("[^1-9]", "", line)
    number = int(f"{digits[0]}{digits[-1]}")
    calibration.append(number)

calibration_value = sum(calibration)
print(f"part2: {calibration_value}")
# réponse : 55686
