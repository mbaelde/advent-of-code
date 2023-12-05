import re

with open("input.txt", "r") as file:
    data = file.read().splitlines()

# Part 1
total_points = 0
n_points = []
for line in data:
    card, numbers = line.split(": ")
    winning_numbers, given_numbers = numbers.split(" | ")
    winning_numbers = re.findall("\d+", winning_numbers)
    given_numbers = re.findall("\d+", given_numbers)
    my_winning_numbers = set(winning_numbers).intersection(given_numbers)
    if my_winning_numbers:
        n_points.append(2 ** (len(my_winning_numbers) - 1))
    else:
        n_points.append(0)
total_points = sum(n_points)

print(total_points)

# Part 2
def compute_n_match_per_line(line):
    card, numbers = line.split(": ")
    card_id = int(re.findall("\d+", card)[0])
    winning_numbers, given_numbers = numbers.split(" | ")
    winning_numbers = re.findall("\d+", winning_numbers)
    given_numbers = re.findall("\d+", given_numbers)
    my_winning_numbers = set(winning_numbers).intersection(given_numbers)
    n_match = len(my_winning_numbers)
    return card_id, n_match


def compute_n_match(data):
    card_matches = {i: 0 for i in range(1, len(data))}
    for line in data:
        card_id, n_match = compute_n_match_per_line(line)
        card_matches[card_id] = n_match
    return card_matches


card_matches = compute_n_match(data)

n_cards = {card_id: 1 for card_id in card_matches.keys()}
for card_id, n_matches in card_matches.items():
    cards = list(range(card_id + 1, card_id + n_matches + 1))
    for card in cards:
        n_cards[card] += n_cards[card_id]

total_cards = sum(n_cards.values())
print(total_cards)
