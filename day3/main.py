import re

with open("test.txt", "r") as file:
    data = file.read().splitlines()

# Part 1
part_number = []
previous_line = ""
n_cols = len(data[0])
for i, line in enumerate(data):
    if i < len(data) - 1:
        next_line = data[i + 1]
    else:
        next_line = ""
        # find all numbers on a line
    numbers = re.findall("[0-9]+", line)
    for number in numbers:
        len_number = len(number)
        # find all characters adjacent to any digit in the number
        idx_start = line.find(number)
        idx_end = len_number + idx_start
        candidate_chars = (
            previous_line[max(idx_start - 1, 0) : min(idx_end + 1, n_cols - 1)]
            + line[max(idx_start - 1, 0)]
            + line[min(idx_end, n_cols - 1)]
            + next_line[max(idx_start - 1, 0) : min(idx_end + 1, n_cols - 1)]
        )
        if re.findall("[^0-9.]", candidate_chars):
            part_number.append(int(number))
    previous_line = line

print(sum(part_number))
# trop petit : 530097
# bonne réponse : 530849

# Part 2 TODO
part_number = []
previous_line = ""
n_cols = len(data[0])
for i, line in enumerate(data):
    if i < len(data) - 1:
        next_line = data[i + 1]
    else:
        next_line = ""
        # find all numbers on a line
    numbers = re.findall("[0-9]+", line)
    for number in numbers:
        len_number = len(number)
        # find all characters adjacent to any digit in the number
        idx_start = line.find(number)
        idx_end = len_number + idx_start
        candidate_chars = (
            previous_line[max(idx_start - 1, 0) : min(idx_end + 1, n_cols - 1)]
            + line[max(idx_start - 1, 0)]
            + line[min(idx_end, n_cols - 1)]
            + next_line[max(idx_start - 1, 0) : min(idx_end + 1, n_cols - 1)]
        )
        if re.findall("[^0-9.]", candidate_chars):
            part_number.append(int(number))
    previous_line = line

print(sum(part_number))
# trop petit :
# bonne réponse : 84900879
