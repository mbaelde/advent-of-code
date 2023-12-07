from dataclasses import dataclass
from enum import Enum
from collections import Counter


with open("test.txt", "r") as file:
    data = file.read().splitlines()

# Part 1
card_scores = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}

class CardType(Enum):
    high_card = "High card"
    one_pair = "One pair"
    two_pair = "Two pair"
    three_of_a_kind = "Three of a kind"
    full_house = "Full house"
    four_of_a_kind = "Four of a kind"
    five_of_a_kind = "Five of a kind"

    def __gt__(self, other):
        return list(CardType).index(self) > list(CardType).index(other)


def match_type(cards):
    card_count = list(Counter(cards).values())
    numbers_count = Counter(card_count)
    if len(card_count) == 5:
        card_type = CardType.high_card
    elif len(card_count) == 4:
        card_type = CardType.one_pair
    elif len(card_count) == 3:
        if 2 in numbers_count.keys():
            card_type = CardType.two_pair
        else:
            card_type = CardType.three_of_a_kind
    elif len(card_count) == 2:
        if 2 in numbers_count.keys():
            card_type = CardType.full_house
        else:
            card_type = CardType.four_of_a_kind
    else:
        card_type = CardType.five_of_a_kind
    return card_type

@dataclass
class Hand:
    cards: str
    bid: int
    type: str = ""
    rank: int = 0

    def __gt__(self, other):
        for i in range(5):
            A,B = card_scores[self.cards[i]], card_scores[other.cards[i]]
            if A > B:
                return True
            elif A < B:
                return False
            
    def __lt__(self, other):
        for i in range(5):
            A,B = card_scores[self.cards[i]], card_scores[other.cards[i]]
            if A < B:
                return True
            elif A > B:
                return False
            
    def __eq__(self, other):
        return self.cards == other.cards


hands = []

for x in data:
    card, bid = x.split(" ")
    bid = int(bid)
    card_type = match_type(card)
    hands.append(Hand(card,bid,card_type))

def insertion_sort(hands):
    for i in range(1, len(hands)):
        key = hands[i]
        j = i - 1
        while j >= 0 and (hands[j].type > key.type or (hands[j].type == key.type and hands[j] > key)):
            hands[j + 1] = hands[j]
            j -= 1
        hands[j + 1] = key

insertion_sort(hands)

for i, hand in enumerate(hands):
    hand.rank = i + 1

print(sum([hand.rank * hand.bid for hand in hands]))

# Part 2
card_scores = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}

hands = []

for x in data:
    cards, bid = x.split(" ")
    bid = int(bid)
    card_type = match_type(cards)
    hands.append(Hand(cards,bid,card_type))

# TODO trouver le meilleur type avec le joker
