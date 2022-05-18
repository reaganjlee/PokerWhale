from cards import *
from players import player1, player2, player3, player4
#from winner_calculator import calc
from collections import Counter
from winner_calculator import *




def test_pairs():
    winner_calc = win_calculator(card_board, players)
    print(winner_calc.if_one_pair(card_board, winner_calc.player_nums(players[0])))


card_board = []
test_card = Card(14, 'Ace', 'Hearts')
test_card.showing = True
card_board.append(test_card)

test_card = Card(9, '9', 'Hearts')
test_card.showing = True
card_board.append(test_card)

test_card = Card(7, '7', 'Clubs')
test_card.showing = True
card_board.append(test_card)

test_card = Card(13, 'King', 'Hearts')
test_card.showing = True
card_board.append(test_card)

test_card = Card(2, '2', 'Spades')
test_card.showing = True
card_board.append(test_card)

players = [player1, player2];

test_pairs()