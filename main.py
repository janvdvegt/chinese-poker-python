from evaluator import HandEvaluator
from card import Card, Hand


hand_evaluator = HandEvaluator()

cards = [Card('7', 's'),
         Card('5', 's'),
         Card('4', 's'),
         Card('3', 's'),
         Card('2', 's')]

hand_1 = Hand(cards, hand_evaluator)

cards = [Card('8', 'd'),
         Card('8', 's'),
         Card('8', 'c'),
         Card('3', 's'),
         Card('3', 'c')]

hand_2 = Hand(cards, hand_evaluator)

print(hand_2 > hand_1)

cards = [Card('6', 's'),
         Card('5', 's'),
         Card('4', 's'),
         Card('3', 's'),
         Card('2', 's')]

hand_1 = Hand(cards, hand_evaluator)

cards = [Card('8', 'd'),
         Card('5', 'd'),
         Card('4', 'd'),
         Card('7', 'd'),
         Card('6', 'd')]

hand_2 = Hand(cards, hand_evaluator)

print(hand_2 > hand_1)

