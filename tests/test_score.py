import unittest

from yatzee.yatzee.score import calculate_possible_scores, SCORE_SHEET_TEMPLATE


class TestScore(unittest.TestCase):
    SCORE_SHEET_TEMPLATE = {
        # Upper section
        'Ones': None, 'Twos': None, 'Threes': None,
        'Fours': None, 'Fives': None, 'Sixes': None,
        # Lower section
        'One Pair': None, 'Two Pairs': None, 'Three Pairs': None, 'Three of a Kind': None,
        'Villa': None, 'Four of a Kind': None, 'Five of a Kind': None, 'Small Straight': None, 'Large Straight': None,
        'Full Straight': None, 'Full House': None, 'Chance': None, 'Yatzy': None
    }

    def test_score(self):
        res = calculate_possible_scores([5,5,5,6,6,6], SCORE_SHEET_TEMPLATE)
        self.assertEqual(33, res.get('Villa'))
        print(res)

    def test_score_1(self):
        res = calculate_possible_scores([5,5,5,6,6,6], SCORE_SHEET_TEMPLATE)
        self.assertEqual(28, res.get('Full House'))
        print(res)

    def test_score_2(self):
        res = calculate_possible_scores([1,5,5,6,6,6], SCORE_SHEET_TEMPLATE)
        self.assertEqual(28, res.get('Full House'))
        print(res)

    def test_score_3(self):
        res = calculate_possible_scores([5,1,5,6,6,6], SCORE_SHEET_TEMPLATE)
        self.assertEqual(28, res.get('Full House'))
        print(res)

