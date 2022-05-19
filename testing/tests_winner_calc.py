from cards import *
from players import player1, player2, player3, player4
#from winner_calculator import calc
from collections import Counter
from winner_calculator import *
import unittest

def card_in_testing(name, suit):
    standard_deck = StandardDeck()
    card = standard_deck.get_card(name, suit)
    card.showing = True
    return card

card_ace_of_hearts = Card(14, 'A', 'Hearts')
card_ace_of_hearts.showing = True
card_nine_of_hearts = Card(9, '9', 'Hearts')
card_nine_of_hearts.showing = True
# card_seven_of_clubs = Card(7, '7', 'Clubs')

card_seven_of_clubs = card_in_testing("7", "Clubs")
# card_seven_of_clubs.showing = True
card_king_of_hearts = Card(13, 'K', 'Hearts')
card_king_of_hearts.showing = True
card_deuce_of_spades = Card(2, '2', 'Spades')
card_deuce_of_spades.showing = True

player1_card1 = Card(3, '3', 'Hearts')
player1_card1.showing = True
player1_card2 = Card(7, '7', 'Hearts')
player1_card2.showing = True

player2_card1 = Card(5, '5', 'Hearts')
player2_card1.showing = True
player2_card2 = Card(6, '6', 'Hearts')
player2_card2.showing = True

class testPairs(unittest.TestCase):
    # card_board = []
    def test_one_pair(self):
        card_board = []

        card_board.append(card_ace_of_hearts)
        card_board.append(card_nine_of_hearts)
        card_board.append(card_seven_of_clubs)
        card_board.append(card_king_of_hearts)
        card_board.append(card_deuce_of_spades)

        players = [player1, player2]
        player1.cards = [player1_card1, player1_card2]
        player2.cards = [player2_card1, player2_card2]

        winner_calc = win_calculator(card_board, players)
        pairs = winner_calc.get_pairs(players[0])
        if_statement = winner_calc.if_one_pair(players[0])
        print(winner_calc.final_cards(players[0]))
        print(pairs)
        print(if_statement)
        self.assertTrue(if_statement, "should be true")



    def test_two_pair(self):
        card_board = []

        card_board.append(card_in_testing("A", "Hearts"))
        card_board.append(card_in_testing("5", "Clubs"))
        card_board.append(card_seven_of_clubs)
        card_board.append(card_king_of_hearts)
        card_board.append(card_deuce_of_spades)

        players = [player1, player2]
        player1_card1 = card_in_testing("K", "Spades")
        player1_card2 = card_in_testing("A", "Diamonds")
        player1.cards = [player1_card1, player1_card2]
        player2.cards = [player2_card1, player2_card2]

        winner_calc = win_calculator(card_board, players)
        pairs = winner_calc.get_pairs(players[0])
        if_statement = winner_calc.if_two_pair(players[0])
        print(winner_calc.final_cards(players[0]))
        print(pairs)
        print(if_statement)
        self.assertTrue(if_statement, "should be true")

    def test_three_of_kind(self):
        card_board = []

        card_board.append(card_in_testing("A", "Hearts"))
        card_board.append(card_in_testing("A", "Clubs"))
        card_board.append(card_seven_of_clubs)
        card_board.append(card_king_of_hearts)
        card_board.append(card_deuce_of_spades)

        players = [player1, player2]
        player1_card1 = card_in_testing("K", "Spades")
        player1_card2 = card_in_testing("A", "Diamonds")
        player1.cards = [player1_card1, player1_card2]
        player2.cards = [player2_card1, player2_card2]

        winner_calc = win_calculator(card_board, players)
        three_of_kind = winner_calc.get_three_of_kind(players[0])
        if_statement = winner_calc.if_three_of_kind(players[0])
        print(winner_calc.final_cards(players[0]))
        print(three_of_kind)
        print(if_statement)
        self.assertTrue(if_statement, "should be true")

    def test_fullhouse(self):
        card_board = []

        card_board.append(card_in_testing("A", "Hearts"))
        card_board.append(card_in_testing("A", "Clubs"))
        card_board.append(card_seven_of_clubs)
        card_board.append(card_king_of_hearts)
        card_board.append(card_in_testing("7", "Diamonds"))

        players = [player1, player2]
        player1_card1 = card_in_testing("K", "Spades")
        player1_card2 = card_in_testing("A", "Diamonds")
        player1.cards = [player1_card1, player1_card2]
        player2.cards = [player2_card1, player2_card2]

        winner_calc = win_calculator(card_board, players)
        fullhouse = winner_calc.get_fullhouse(players[0])
        if_statement = winner_calc.if_fullhouse(players[0])
        print(winner_calc.final_cards(players[0]))
        print(fullhouse)
        print(if_statement)
        self.assertTrue(if_statement, "should be true")

    def test_quads(self):
        card_board = []

        card_board.append(card_in_testing("A", "Hearts"))
        card_board.append(card_in_testing("A", "Clubs"))
        card_board.append(card_seven_of_clubs)
        card_board.append(card_king_of_hearts)
        card_board.append(card_in_testing("7", "Diamonds"))

        players = [player1, player2]
        player1_card1 = card_in_testing("A", "Spades")
        player1_card2 = card_in_testing("A", "Diamonds")
        player1.cards = [player1_card1, player1_card2]
        player2.cards = [player2_card1, player2_card2]

        winner_calc = win_calculator(card_board, players)
        quads = winner_calc.get_quads(players[0])
        if_statement = winner_calc.if_quads(players[0])
        print(winner_calc.final_cards(players[0]))
        print(quads)
        print(if_statement)
        self.assertTrue(if_statement, "should be true")

    def test_get_straights(self):
        card_board = []

        card_board.append(card_in_testing("A", "Hearts"))
        card_board.append(card_in_testing("K", "Clubs"))
        card_board.append(card_in_testing("Q", "Spades"))
        card_board.append(card_king_of_hearts)
        card_board.append(card_in_testing("9", "Diamonds"))

        players = [player1, player2]
        player1_card1 = card_in_testing("J", "Spades")
        player1_card2 = card_in_testing("10", "Diamonds")
        player1.cards = [player1_card1, player1_card2]
        player2.cards = [player2_card1, player2_card2]

        winner_calc = win_calculator(card_board, players)
        straights = winner_calc.get_straights(players[0])
        if_statement = winner_calc.if_straight(players[0])
        print(winner_calc.final_cards(players[0]))
        print(straights)
        print(if_statement)
        self.assertTrue(if_statement, "should be true")

    def test_get_flush(self):
        card_board = []

        card_board.append(card_in_testing("A", "Hearts"))
        card_board.append(card_in_testing("3", "Hearts"))
        card_board.append(card_seven_of_clubs)
        card_board.append(card_king_of_hearts)
        card_board.append(card_in_testing("2", "Hearts"))

        players = [player1, player2]
        player1_card1 = card_in_testing("Q", "Hearts")
        player1_card2 = card_in_testing("6", "Hearts")
        player1.cards = [player1_card1, player1_card2]
        player2.cards = [player2_card1, player2_card2]

        winner_calc = win_calculator(card_board, players)
        flushes = winner_calc.get_flushes(players[0])
        if_statement = winner_calc.if_flush(players[0])
        print(winner_calc.final_cards(players[0]))
        print(flushes)
        print(if_statement)
        self.assertTrue(if_statement, "should be true")

    def test_get_straight_flush(self):
        card_board = []

        card_board.append(card_in_testing("A", "Clubs"))
        card_board.append(card_in_testing("K", "Clubs"))
        card_board.append(card_in_testing("Q", "Clubs"))
        card_board.append(card_king_of_hearts)
        card_board.append(card_in_testing("9", "Clubs"))

        players = [player1, player2]
        player1_card1 = card_in_testing("J", "Clubs")
        player1_card2 = card_in_testing("10", "Clubs")
        player1.cards = [player1_card1, player1_card2]
        player2.cards = [player2_card1, player2_card2]

        winner_calc = win_calculator(card_board, players)
        straights = winner_calc.get_straights(players[0])
        straight_flush = winner_calc.get_straight_flush(players[0])
        if_statement = winner_calc.if_straight_flush(players[0])
        print(winner_calc.final_cards(players[0]))
        print(straights)
        print(straight_flush)
        print(if_statement)
        self.assertTrue(if_statement, "should be true")

    def test_get_royal_flush(self):
        card_board = []

        card_board.append(card_in_testing("A", "Clubs"))
        card_board.append(card_in_testing("K", "Clubs"))
        card_board.append(card_in_testing("Q", "Clubs"))
        card_board.append(card_king_of_hearts)
        card_board.append(card_in_testing("9", "Diamonds"))

        players = [player1, player2]
        player1_card1 = card_in_testing("J", "Clubs")
        player1_card2 = card_in_testing("10", "Clubs")
        player1.cards = [player1_card1, player1_card2]
        player2.cards = [player2_card1, player2_card2]

        winner_calc = win_calculator(card_board, players)
        straights = winner_calc.get_straights(players[0])
        royal_straight_flush = winner_calc.get_straight_flush(players[0])
        if_statement = winner_calc.if_royal_flush(players[0])
        print(winner_calc.final_cards(players[0]))
        print(straights)
        print(royal_straight_flush)
        print(if_statement)
        self.assertTrue(if_statement, "should be true")

    def test_get_card(self):
        standard_deck = StandardDeck()
        card = standard_deck.get_card("K", "Hearts")
        self.assertEqual(card.name, "K", "card name should be same")
        self.assertEqual(card.suit, "Hearts", "card suit should be same")





    # test_pairs(card_board, players)
if __name__ == '__main__':
    unittest.main()