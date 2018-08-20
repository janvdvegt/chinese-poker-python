from card import Card, Hand
from itertools import combinations
from constants import ranks, rank_dict


class HandEvaluator:
    def __init__(self):
        self.instantiate_lookup_tables()
        self.instantiate_prime_table()

    def instantiate_lookup_tables(self):
        self.flush_lookup_table = [None for _ in range(7937)]
        self.instantiate_lookup_table(self.flush_lookup_table, 1, 323)
        self.unique_5_lookup_table = [None for _ in range(7937)]
        self.instantiate_lookup_table(self.unique_5_lookup_table, 1599, 6186)

    def instantiate_lookup_table(self, table, straight_offset, normal_offset):
        straight_index = straight_offset
        normal_index = normal_offset
        for c1, c2, c3, c4, c5 in combinations(reversed(ranks), 5):
            hand = Hand([Card(c1, 's'),
                         Card(c2, 's'),
                         Card(c3, 's'),
                         Card(c4, 's'),
                         Card(c5, 's')])
            if (rank_dict[c1] - rank_dict[c5] == 4):
                table[hand.q_value()] = straight_index
                straight_index += 1
            elif (c1, c2, c3, c4, c5) == ('A', '5', '4', '3', '2'):
                table[hand.q_value()] = straight_offset + 9
            else:
                table[hand.q_value()] = normal_index
                normal_index += 1

    def instantiate_four_of_a_kinds(self):
        four_of_a_kind_index = 11
        for four_card in reversed(ranks):
            for single_card in reversed(ranks):
                if single_card != four_card:
                    hand = Hand([Card(four_card, 's')] * 4 + [Card(single_card, 'd')])
                    self.prime_table[hand.p_value()] = four_of_a_kind_index
                    four_of_a_kind_index += 1

    def instantiate_full_houses(self):
        full_house_index = 167
        for three_card in reversed(ranks):
            for two_card in reversed(ranks):
                if two_card != three_card:
                    hand = Hand([Card(three_card, 's')] * 3 + [Card(two_card, 'd')] * 2)
                    self.prime_table[hand.p_value()] = full_house_index
                    full_house_index += 1

    def instantiate_three_of_a_kind(self):
        three_of_a_kind_index = 1610
        for three_card in reversed(ranks):
            for single_card_1, single_card_2 in combinations(reversed([c for c in ranks if c != three_card]), 2):
                hand = Hand([Card(three_card, 's')] * 3 + [Card(single_card_1, 'd'), Card(single_card_2, 'd')])
                self.prime_table[hand.p_value()] = three_of_a_kind_index
                three_of_a_kind_index += 1

    def instantiate_two_pair(self):
        two_pair_index = 2468
        for two_card_1, two_card_2 in combinations(reversed(ranks), 2):
            for single_card in reversed([c for c in ranks if c != two_card_1 and c != two_card_2]):
                hand = Hand([Card(two_card_1, 'd')] * 2 + [Card(two_card_2, 'c')] * 2 + [Card(single_card, 'c')])
                self.prime_table[hand.p_value()] = two_pair_index
                two_pair_index += 1

    def instantiate_one_pair(self):
        one_pair_index = 3326
        for two_card in reversed(ranks):
            for single_card_1, single_card_2, single_card_3 in combinations(
                    reversed([c for c in ranks if c != two_card]), 3):
                hand = Hand([Card(two_card, 's')] * 2 + [Card(single_card_1, 'd'), Card(single_card_2, 'd'),
                                                         Card(single_card_3, 'd')])
                self.prime_table[hand.p_value()] = one_pair_index
                one_pair_index += 1

    def instantiate_prime_table(self):
        self.prime_table = dict()
        self.instantiate_four_of_a_kinds()
        self.instantiate_full_houses()
        self.instantiate_three_of_a_kind()
        self.instantiate_two_pair()
        self.instantiate_one_pair()

    def get_rank(self, hand):
        q_value = hand.q_value()
        if hand.is_flush():
            return self.flush_lookup_table[q_value]
        if self.unique_5_lookup_table[q_value] is not None:
            return self.unique_5_lookup_table[q_value]
        return self.prime_table[hand.p_value()]
