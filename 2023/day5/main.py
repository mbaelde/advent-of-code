import re
from typing import Dict
from tqdm import tqdm

class RangeMap:
    def __init__(self, maps_txt: str):
        self._maps_txt = maps_txt
        self._destination_ranges = []
        self._source_ranges = []
        self._min_val = 0
        self._max_val = 0
        for map in self._maps_txt:
            destination_range_start, source_range_start, range_length = map.split(" ")
            destination_range_start = int(destination_range_start)
            source_range_start = int(source_range_start)
            range_length = int(range_length)

            self._destination_ranges.append(
                range(destination_range_start, destination_range_start + range_length)
            )
            self._source_ranges.append(
                range(source_range_start, source_range_start + range_length)
            )
            self._max_val = max(
                self._max_val,
                destination_range_start + range_length - 1,
                source_range_start + range_length - 1,
            )

    def generate_map(self, min_val: int = None, max_val: int = None) -> Dict[int, int]:
        if min_val is None:
            min_val = self._min_val
        if max_val is None:
            max_val = self._max_val

        map = {i: i for i in range(min_val, max_val + 1)}
        for source_range, destination_range in zip(
            self._source_ranges, self._destination_ranges
        ):
            dict_map = {k: v for k, v in zip(source_range, destination_range)}
            map.update(dict_map)
        return map

    def get_map(self, source_value: int) -> int:
        destination_value = None
        for source_range, destination_range in zip(self._source_ranges, self._destination_ranges):
            if source_value in source_range:
                destination_value = source_value - source_range.start + destination_range.start
                break
        if destination_value is None:
            destination_value = source_value
        return destination_value


seeds_key = "seeds: "
seed_to_soil_map_key = "seed-to-soil map:"
soil_to_fertilizer_map_key = "soil-to-fertilizer map:"
fertilizer_to_water_map_key = "fertilizer-to-water map:"
water_to_light_map_key = "water-to-light map:"
light_to_temperature_map_key = "light-to-temperature map:"
temperature_to_humidity_map_key = "temperature-to-humidity map:"
humidity_to_location_map_key = "humidity-to-location map:"

with open("input.txt", "r") as file:
    data = file.read()

# extract seeds
min_seed = 0
max_seed = int(max(re.findall("\d+", data)))
data = data.splitlines()


# Part 1
seeds = [
    int(x)
    for x in [d for d in data if seeds_key in d][0].split(seeds_key)[-1].split(" ")
]

def get_seed_location(seed, data):
    # extrad seed_to_soil map
    seed_to_soil_map_txt = data[
        data.index(seed_to_soil_map_key) + 1 : data.index(soil_to_fertilizer_map_key) - 1
    ]
    seed_to_soil_range_map = RangeMap(seed_to_soil_map_txt)
    soil = seed_to_soil_range_map.get_map(seed)

    # extrad soil_to_fertilizer map
    soil_to_fertilizer_map_txt = data[
        data.index(soil_to_fertilizer_map_key)
        + 1 : data.index(fertilizer_to_water_map_key)
        - 1
    ]
    soil_to_fertilizer_range_map = RangeMap(soil_to_fertilizer_map_txt)
    fertilizer = soil_to_fertilizer_range_map.get_map(soil)

    # extrad fertilizer_to_water map
    fertilizer_to_water_map_txt = data[
        data.index(fertilizer_to_water_map_key) + 1 : data.index(water_to_light_map_key) - 1
    ]
    fertilizer_to_water_range_map = RangeMap(fertilizer_to_water_map_txt)
    water = fertilizer_to_water_range_map.get_map(fertilizer)

    # extrad water_to_light map
    water_to_light_map_txt = data[
        data.index(water_to_light_map_key)
        + 1 : data.index(light_to_temperature_map_key)
        - 1
    ]
    water_to_light_range_map = RangeMap(water_to_light_map_txt)
    light = water_to_light_range_map.get_map(water)

    # extrad fertilizer_to_water map
    light_to_temperature_map_txt = data[
        data.index(light_to_temperature_map_key)
        + 1 : data.index(temperature_to_humidity_map_key)
        - 1
    ]
    light_to_temperature_range_map = RangeMap(light_to_temperature_map_txt)
    temperature = light_to_temperature_range_map.get_map(light)

    # extrad temperature_to_humidity map
    temperature_to_humidity_map_txt = data[
        data.index(temperature_to_humidity_map_key)
        + 1 : data.index(humidity_to_location_map_key)
        - 1
    ]
    temperature_to_humidity_range_map = RangeMap(temperature_to_humidity_map_txt)
    humidity = temperature_to_humidity_range_map.get_map(temperature)

    # extrad humidity_to_location map
    humidity_to_location_map_txt = data[data.index(humidity_to_location_map_key) + 1 :]
    humidity_to_location_range_map = RangeMap(humidity_to_location_map_txt)
    location = humidity_to_location_range_map.get_map(humidity)

    return location

seeds_locations = {}
for seed in seeds:
    seeds_locations[seed] = get_seed_location(seed, data)
print(min(seeds_locations.values()))

# Part 2
seeds = [
    int(x)
    for x in [d for d in data if seeds_key in d][0].split(seeds_key)[-1].split(" ")
]

seeds_ranges = [range(seeds[i], seeds[i]+seeds[i+1]) for i in [x for x in range(len(seeds)) if x%2==0]]

min_location = max_seed
for seed_range in tqdm(seeds_ranges, desc="seed_range"):
    for seed in tqdm(seed_range, "seed"):
        location = get_seed_location(seed, data)
        min_location = min(min_location, location)

print(min_location)
#result : 12634632