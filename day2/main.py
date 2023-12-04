with open("input.txt", "r") as file:
    lines = file.read().splitlines()

colors = ["blue", "red", "green"]

# Part 1
max_colors = {"red": 12, "green": 13, "blue": 14}

sum_value = 0
for line in lines:
    game, cubes = line.split(": ")
    game_id = int(game[5:])
    sets = cubes.split("; ")
    color_dict = {c: 0 for c in colors}
    is_ok = []
    for set_ in sets:
        numbers_cubes = [x.split(" ") for x in set_.split(", ")]
        color_dict = {x[1]: int(x[0]) for x in numbers_cubes}
        is_ok.append((color_dict.get("green",0) <= max_colors["green"]) 
                and (color_dict.get("blue",0) <= max_colors["blue"]) 
                and (color_dict.get("red",0) <= max_colors["red"]))
    if all(is_ok):
        sum_value += game_id

print(sum_value)

# Part 2
sum_value = 0
for line in lines:
    game, cubes = line.split(": ")
    game_id = int(game[5:])
    sets = cubes.split("; ")
    color_dict = {c: 0 for c in colors}
    is_ok = []
    for set_ in sets:
        numbers_cubes = [x.split(" ") for x in set_.split(", ")]
        for x in numbers_cubes:
            color_dict.update({x[1]: max(int(x[0]), color_dict.get(x[1],0)) for x in numbers_cubes})
    power = color_dict.get("green",1) * color_dict.get("red",1) * color_dict.get("blue",1)
    sum_value += power

print(sum_value)
