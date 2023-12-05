import re
from typing import Dict

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

            self._destination_ranges.append(range(destination_range_start, destination_range_start+range_length))
            self._source_ranges.append(range(source_range_start, source_range_start+range_length))
            self._max_val = max(self._max_val, destination_range_start+range_length-1, source_range_start+range_length-1)

    def generate_map(self, min_val: int = None, max_val: int = None) -> Dict[int, int]:
        if min_val is None:
            min_val = self._min_val
        if max_val is None:
            max_val = self._max_val
        
        map = {i: i for i in range(min_val, max_val+1)}
        for source_range, destination_range in zip(self._source_ranges, self._destination_ranges):
            dict_map = {k:v for k,v in zip(source_range, destination_range)}
            map.update(dict_map)
        return map
    
with open("test.txt", "r") as file:
    data = file.read()

seeds_key = "seeds: "
seed_to_soil_map_key = "seed-to-soil map:"
soil_to_fertilizer_map_key = "soil-to-fertilizer map:"
fertilizer_to_water_map_key = "fertilizer-to-water map:"
water_to_light_map_key = "water-to-light map:"
light_to_temperature_map_key = "light-to-temperature map:"
temperature_to_humidity_map_key = "temperature-to-humidity map:"
humidity_to_location_map_key = "humidity-to-location map:"

# extract seeds
min_seed = 0
max_seed = int(max(re.findall("\d+", data)))
data = data.splitlines()
seeds = [int(x) for x in 
    [d for d in data if seeds_key in d][0].split(seeds_key)[-1].split(" ")
]

# extrad seed_to_soil map      
seed_to_soil_map_txt = data[data.index(seed_to_soil_map_key)+1:data.index(soil_to_fertilizer_map_key)-1]
seed_to_soil_range_map = RangeMap(seed_to_soil_map_txt)
seed_to_soil_map = seed_to_soil_range_map.generate_map(min_seed, max_seed)

# extrad soil_to_fertilizer map      
soil_to_fertilizer_map_txt = data[data.index(soil_to_fertilizer_map_key)+1:data.index(fertilizer_to_water_map_key)-1]
soil_to_fertilizer_range_map = RangeMap(soil_to_fertilizer_map_txt)
soil_to_fertilizer_map = soil_to_fertilizer_range_map.generate_map(min_seed, max_seed)

# extrad fertilizer_to_water map      
fertilizer_to_water_map_txt = data[data.index(fertilizer_to_water_map_key)+1:data.index(water_to_light_map_key)-1]
fertilizer_to_water_range_map = RangeMap(fertilizer_to_water_map_txt)
fertilizer_to_water_map = fertilizer_to_water_range_map.generate_map(min_seed, max_seed)


# extrad water_to_light map      
water_to_light_map_txt = data[data.index(water_to_light_map_key)+1:data.index(light_to_temperature_map_key)-1]
water_to_light_range_map = RangeMap(water_to_light_map_txt)
water_to_light_map = water_to_light_range_map.generate_map(min_seed, max_seed)


# extrad fertilizer_to_water map      
light_to_temperature_map_txt = data[data.index(light_to_temperature_map_key)+1:data.index(temperature_to_humidity_map_key)-1]
light_to_temperature_range_map = RangeMap(light_to_temperature_map_txt)
light_to_temperature_map = light_to_temperature_range_map.generate_map(min_seed, max_seed)


# extrad temperature_to_humidity map      
temperature_to_humidity_map_txt = data[data.index(temperature_to_humidity_map_key)+1:data.index(humidity_to_location_map_key)-1]
temperature_to_humidity_range_map = RangeMap(temperature_to_humidity_map_txt)
temperature_to_humidity_map = temperature_to_humidity_range_map.generate_map(min_seed, max_seed)


# extrad humidity_to_location map      
humidity_to_location_map_txt = data[data.index(humidity_to_location_map_key)+1:]
humidity_to_location_range_map = RangeMap(humidity_to_location_map_txt)
humidity_to_location_map = humidity_to_location_range_map.generate_map(min_seed, max_seed)

seeds_locations = {seed: humidity_to_location_map[
        temperature_to_humidity_map[
        light_to_temperature_map[
        water_to_light_map[fertilizer_to_water_map[soil_to_fertilizer_map[seed_to_soil_map[seed]]]]
    ]]]
    for seed in seeds
    }

print(min(seeds_locations.values()))