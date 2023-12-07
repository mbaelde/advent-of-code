import math
from typing import NamedTuple
import numpy as np

import re

with open("input.txt", "r") as file:
    data = file.read().splitlines()

# Part 1
times = re.findall("\d+", data[0])
distances = re.findall("\d+", data[1])

Race = NamedTuple("Race", [("time", int), ("distance", int)])

races = [
    Race(int(time), int(distance))
    for time, distance in zip(times, distances)
]

def compte_number_wins(race):
    speed = np.arange(race.time+1)
    t = np.arange(race.time+1)
    remaining_time = race.time - t
    distance_per_time = speed * remaining_time
    return sum(distance_per_time > race.distance)

number_wins = []
for race in races:
    number_wins.append(compte_number_wins(race))

print(math.prod(number_wins))

# Part 2
time = int(''.join(times))
distance = int(''.join(distances))

race = Race(time, distance)

number_wins = compte_number_wins(race)

print(number_wins)
# reponse : 41513103