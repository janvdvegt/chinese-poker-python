from operator import ior, and_
from functools import reduce
from constants import prime_dict, rank_dict, suit_dict


class Card:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.prime = prime_dict[rank]
        self.value = 1 << rank_dict[rank] << 16
        self.value += suit_dict[suit] << 12
        self.value += rank_dict[rank] << 8
        self.value += prime_dict[rank]


class Hand:
    def __init__(self, cards, hand_evaluator=None):
        self.cards = cards
        self.values = [card.value for card in cards]
        self.hand_evaluator = hand_evaluator

    def is_flush(self):
        return reduce(and_, self.values + [15 << 12]) > 0

    def q_value(self):
        return reduce(ior, self.values) >> 16

    def p_value(self):
        return reduce(lambda x, y: x * y, [v & 255 for v in self.values])

    def __gt__(self, other):
        return self.hand_evaluator.get_rank(self) < self.hand_evaluator.get_rank(other)

    def __eq__(self, other):
        return self.hand_evaluator.get_rank(self) == self.hand_evaluator.get_rank(other)

    def __lt__(self, other):
        return self.hand_evaluator.get_rank(self) > self.hand_evaluator.get_rank(other)
