from cards import *
from players import *
from winner_calculator import *
from pot import *
from collections import Counter


class Game(object):
    def __init__(self, cards, players, small_blind_amt=.10, big_blind_amt=.20):
        self.cards = cards
        # self.pot = 0
        self.current_pot = Pot(0)

        # The current main bet on the table
        self.table_stake = self.current_pot.table_stake
        # Difference between players' current bet and table stake
        # self.stake_gap = self.current_pot.stake_gap
        # Min re-raise amount is the difference between previous raise and what was previously at the table
        self.req_min_raise_diff = big_blind_amt
        self.card_board = []
        self.players = None   # Just the list of players
        self.small_blind_amt = small_blind_amt
        self.big_blind_amt = big_blind_amt
        # self.current_pot.add_lst_participants(players)
        self.pots = [self.current_pot]

        self.current_bet = 0
        self.street = 'Pre-flop'
        self.turn = 0

        # self.players_in_action = players.copy()
        #There can also be vars for SB/BB/Dealer name but don't think it's needed
        # self.current_player = None

        self.last_hand_BB_bust = False

        self.last_aggro_player = None  #only needed on rivers

    def __repr__(self):
        return 'We have a game!' + '\nBlinds are ' + str(
            self.small_blind_amt) + '/' + str(
            self.big_blind_amt) + '\nWith a ' + str(
            self.cards) + '\nand ' + str(len(
            self.players)) + ' players'
        #+ str(self.players)

    def set_players(self):
        players = []
        while True:
        #     try:
            num_players = input('How many players would you like to have? ')
            if (num_players == ""):
                print('\nCannot be an empty number of players ')
                continue
            num_players = int(num_players)
            if (num_players < 2):
                print('\nYou need to have 2 players or more to play ')
                continue
            else:
                # print('\nYour options are fold, check, call, raise')
                counter = 0
                while counter < num_players:
                    prompt = "What is the name of player " + str(counter) + "? "
                    player_name = input(prompt)
                    player_stack = input ("What is this player's stack size? ")
                    player_stack = float(player_stack)
                    if player_stack < 0:
                        print("Player stack has to be greater than 0")
                        continue
                    player = Player(player_name, player_stack)
                    players.append(player)
                    counter += 1
                break
            # except:
            #     continue
        print("It gets to here")
        self.players = players
        self.current_pot.add_lst_participants(players)
        self.positioned = players.copy()  #list of players in order of position

        self.players_not_out = self.positioned.copy()
    def start(self):
        # print('game restarting')
        # while True:
        #     players_input = input('How many players would you like to have?')
        #     players_input = int(players_input)
        #     if players_input < 2
        self.set_players()

        #clear cards/roles from all players
        for player in self.players:
            player.clear_cards()
            player.special_role = None
        # print('players cards/roles removed')

        self.cards.__init__()
        # print('cards reset')

        self.cards.shuffle()
        self.deal_cards_all_players()
        self.current_pot = Pot(0)
        self.current_pot.add_lst_participants(self.players_not_out)
        self.pots = [self.current_pot]
        self.blinds_in_roles_set()
        print('The blinds have been put in, UTG starts')
        # self.turn = 1
        self.next_turn()

        #current_street()
        '''for player in self.positioned: 
      print(player.cards)
    print('just for some testing/debugging^')'''


    def next_turn(self, folded=False):
        if len(self.players_not_out) == 1:
            self.game_end()

        if folded == False:
            self.turn += 1

        if_all_evened_out = True
        for player in self.players_not_out:
            if player.current_stake != self.table_stake:
                if_all_evened_out = False
        if self.street != 'Pre-flop' and self.table_stake != 0 and self.turn != 0 and if_all_evened_out:
            self.next_street()
        # if self.street != 'Pre-flop' and if_all_evened_out

        if (self.turn == len(self.players_not_out)):
            if (self.street == 'Pre-flop') or if_all_evened_out == False: # self.players_not_out[0].current_stake != self.table_stake:
                # If it is preflop and the turn counter for players reaches max, it goes
                # back to the SB and BB
                # Or if there is a raiser
                self.turn = 0
            else:
                self.next_street()
        # if (self.street == 'Pre-flop') and \
        #         (self.turn == len(self.players_not_out)):
        #     self.turn = 0
        # if (self.street != 'Pre-flop') and \
        #         (self.turn == len(self.players_not_out)):
        #     self.next_street()
        if (self.street != 'Done'):
            print('\nThe current turn number is: ' + str(self.turn) + '\n')

            print('\ncurrent players turn: ' +
                  self.players_not_out[self.turn].name)

            print('stack size: ' +
                  str(round(self.players_not_out[self.turn].current_stack, 2)))
            print('cards: ' + str(self.players_not_out[self.turn].cards))
            print("player's current stake: " +
                  str(round(self.players_not_out[self.turn].current_stake, 2)))
            print("game's stake: " + str(self.table_stake))
            print("game's current pot size: " + self.display_pot_amt())
            print('special_role: ' +
                  str(self.players_not_out[self.turn].special_role))

            players_input = self.get_input_and_redirect();

            # print('we have some input!')

            if (self.street == 'Pre-flop') and (self.turn == 1):
                # Can't put this up front because BB has to go during pre-flop
                self.next_street()
            else:
                if players_input == 'fold':
                    self.next_turn(True)
                else:
                    self.next_turn()

    def get_input_and_redirect(self):
        while True:
            try:
                players_input = input('what would you like to do? ')
                if (players_input == 'check'):
                    if (self.players_not_out[self.turn].current_stake == self.table_stake):
                        break
                    else:
                        print('\nYour options are fold, call, raise')

                elif (self.current_player().current_stake == self.table_stake) \
                        and (players_input == 'call'):  #When its BB
                    print('\nYour options are fold, check, raise')

                elif players_input == 'fold' or players_input == 'call' or players_input == 'raise':
                    break
                else:
                    print('\nYour options are fold, check, call, raise')
            except:
                continue

        if players_input == 'fold':
            self.fold()
        if players_input == 'check':
            self.check()
        if players_input == 'call':
            self.call()
        if players_input == 'raise':
            raise_amt = input('What would you like to raise it to? ')
            self.raise_by(raise_amt)
        return players_input


    def next_street(self):
        print('\n\n we got it!\n\n')

        if self.street == 'River':
            self.game_end()
        else:
            if self.street == 'Turn':
                self.street = 'River'
                self.cards.deal(self.card_board)
            if self.street == 'Flop':
                self.street = 'Turn'
                self.cards.deal(self.card_board)
            if self.street == 'Pre-flop':
                self.street = 'Flop'
                self.cards.deal(self.card_board, 3)

            print('The current street is: ' + str(self.street))
            print(self.card_board)

            self.turn = -1
            self.current_pot.table_stake = 0
            self.table_stake = 0
            # self.current_pot.stake_gap = 0
            self.current_bet = 0

            for player in self.positioned:
                player.current_stake = 0

        self.next_turn()

    def game_end(
            self
    ):  #calculates the winner and gives the pot to the correct player, also uses a smaller function to calculate side-pots

        #so ways to get to this function, you get to the river, or everyone folds i.e. only one player left in players_not_out
        print('\n\n Game ends!\n\n')
        if len(self.players_not_out) == 1:
            print('When folding down, the winner is: ' +
                  str(self.players_not_out[0]))
            return

        self.street = 'Done'
        # best_player = 'none'
        # highest_hand = None
        players_in_game = []
        for pot in self.pots:
            [players_in_game.append(x) for x in pot.participants if x not in players_in_game]

        winner_calc = win_calculator(self.card_board, self.positioned)
        result = winner_calc.checker(players_in_game)
        # for player in self.positioned:
        #     print("blah")
        print(result)
        return result

    def change_pos_order(self, busted_special_role=None):

        self.positioned[0].special_role = None
        self.positioned[1].special_role = None
        self.positioned[-1:][0].special_role = None

        self.positioned = self.positioned[-1:] + self.positioned[:1]

        if busted_special_role != None:
            if busted_special_role == 'BB':  #Special case of if BB busts
                self.positioned[0].special_role = 'BB'
                self.positioned[-1:][0].special_role = 'Btn'
                self.last_hand_BB_bust = True
            if busted_special_role == 'SB':
                self.positioned[0].special_role = 'SB'
                self.positioned[1].special_role = 'BB'
        elif self.last_hand_BB_bust:
            self.positioned[0].special_role = 'SB'
            self.positioned[1].special_role = 'BB'
            self.last_hand_BB_bust = False

        else:
            self.positioned[-1:][0].special_role = 'Btn'
            self.positioned[0].special_role = 'SB'
            self.positioned[1].special_role = 'BB'

    def deal_cards_all_players(self):
        for player in self.positioned:
            self.cards.deal(player.cards, 2)

    def update_table_stakes(self, amt):
        self.table_stake = amt
        self.current_pot.table_stake = amt

    def blinds_in_roles_set(self):
        self.players_not_out[-1:][0].special_role = 'Btn'

        self.put_money_in_pot(self.small_blind_amt)
        self.update_table_stakes(self.small_blind_amt)
        # self.current_pot.table_stake = self.small_blind_amt
        self.players_not_out[self.turn].special_role = 'SB'
        print('\ncurrent game stake is: ' + str(self.table_stake))
        print('small blinds stake is: ' +
              str(self.players_not_out[self.turn].current_stake))

        print('\n going on to player 2')
        self.turn += 1

        #self.positioned[0].current_stack -= self.small_blind_amt
        #self.pot += self.small_blind_amt

        self.put_money_in_pot(self.big_blind_amt)
        self.update_table_stakes(self.big_blind_amt)
        # self.current_pot.table_stake = self.big_blind_amt
        self.players_not_out[self.turn].special_role = 'BB'
        print('\ncurrent game stake is: ' + str(self.table_stake))
        print('big blinds stake is: ' +
              str(self.players_not_out[self.turn].current_stake))

    def put_money_in_pot(self, amount):
        # self.pot += amount
        self.current_pot.add_amt(amount)
        self.current_player().current_stack -= amount
        self.current_player().current_stake += amount
        # self.current_pot.table_stake = amount
        # self.table_stake = self.current_pot.table_stake


    # Players' actions

    def fold(self):
        for pot in self.pots:
            pot.participants.remove(self.current_player())
        print(str(self.players_not_out.pop(self.turn).name) + ' folds')
        print(self.players_not_out)
        '''print('\npositioned should have all the players still ')
    print(self.positioned)'''

    def check(self):
        print(str(self.players_not_out[self.turn]) + ' checks')

    def call(self):
        call_amt = self.table_stake - self.current_player().current_stake
        if call_amt > self.current_player().current_stack:
            self.all_in()
        else:
            self.put_money_in_pot(call_amt)
            # self.update_table_stakes(call_amt)

    def raise_by(self, raise_amount):
        raise_amount = float(raise_amount)
        # if (raise_amount - self.stake_gap) < self.table_stake:
        #     raise Exception("")
        if (raise_amount - self.req_min_raise_diff) < self.table_stake:
            # raise Exception('the raise is not large enough')
            print("the raise is not large enough")
            self.get_input_and_redirect()
            return

        if (raise_amount > self.current_player().current_stack):
            # raise Exception('This is a larger amount than you currently have')
            print("This is a larger amount than you currently have")
            self.get_input_and_redirect()
            return


        if raise_amount == self.current_player().current_stack:
            self.all_in()
        else:
            print(str(self.current_player()) + ' raises to' + str(raise_amount))
            self.put_money_in_pot(raise_amount)
            self.update_table_stakes(raise_amount)
            # Min re-raise amount is the difference between previous raise and what was previously at the table
            self.req_min_raise_diff = raise_amount - self.table_stake
            # self.current_pot.table_stake = raise_amount
    def max_table_stake(self):
        max = 0
        for pot in self.pots:
            if pot.table_stake > max:
                max = pot.table_stake
        return max
    def all_in(self):
        # all_in_info = [self.current_player(), [], self.current_player().current_stack]
        # self.all_in_pots.append(all_in_info)
        current_player_stack = self.current_player().current_stack
        if current_player_stack > self.max_table_stake():
            self.update_table_stakes(current_player_stack)
        # else:
            # deduct the difference of table stake and all_in amount and add
            # that into a new pot of the players that already put money in

        # if current_player_stack < self.cu

        self.put_money_in_pot(current_player_stack)

        # self.current_pot.table_stake = self.current_player().current_stack
        # self.players_not_out.remove(self.current_player())
        new_pot = Pot(0)
        new_pot.add_lst_participants(self.players_not_out)
        self.pots.append(new_pot)
        self.current_pot = new_pot

    def display_pot_amt(self):
        total = 0
        for pot in self.pots:
            total += pot.pot_amt
        return str(round(total, 2))

    def current_player(self):
        return self.players_not_out[self.turn]

game = Game(deck, [player1, player2, player3, player4])
game.start()