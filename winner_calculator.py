#from cards import deck
#from players import player1, player2, player3, player4
# from main import game
# print('this loaded 1')

# game.card_board = []
# game.deck.shuffle()
# game.deck.deal(game.card_board, 5)
# print(str(game.card_board))
# print('this loaded')


class win_calculator(object):
    def __init__(self, card_board, players):
        self.card_board = card_board
        self.players = players


        #calculating the winner

    def highestcombo(self, player):
        player_nums_with_board = self.player_nums_with_board(player)

        result = self.if_royal_flush(player)
        if result:
            # print('result of if_royal_flush below')
            print(str(result))
            return result

        result = self.if_straight_flush(player)
        if result:
            # print('result of if_straight_flush below')
            print(str(result))
            return result

        result = self.if_quads(player_nums_with_board)
        if result:
            # print('result of if_quads below')
            print(str(result))
            return result

        result = self.if_fullhouse(player_nums_with_board)
        if result:
            # print('result of if_fullhouse below')
            print(str(result))
            return result

        result = self.if_flush(player)
        if result:
            # print('result of if_flush below')
            print(str(result))
            return result

        result = self.if_straight(player)
        if result:
            # print('result of if_straight below')
            print(str(result))
            return result

        result = self.if_three_of_kind(player_nums_with_board)
        if result:
            # print('result of if_set below')
            print(str(result))
            return result

        result = self.if_two_pair(player_nums_with_board)
        if result:
            # print('result of if_two_pair below')
            print(str(result))
            return result

        result = self.if_one_pair(player_nums_with_board)
        #print('testingxd')
        if result:
            # print('result of if_one_pair below')
            print(str(result))
            return result
        print('\n\n')
        '''print(str(self.if_fullhouse))'''

        result = self.if_high_card(player_nums_with_board)
        #print('testingxd')
        if result:
            # print('result of if_high_card below')
            print(str(result))
            return result
        print('\n\n')
        '''if_pair = self.if_pair(player_nums)
    print(str(if_pair))

    #print('\nseparator flush below\n')
    if_flush = self.if_flush(player)
    print(str(if_flush))

    #print('\nseparator set below\n')
    

    

    print('\nif_straight output below:\n')
    if_straight = self.if_straight(player)
    print(str(if_straight))

    print('result of final_cards below')
    self.final_cards(player)'''
        #if if_quads:
        #  highest_combo = if_quads.append[]

    def checker(self):
        players_and_combos = []
        for player in self.players:
            result = [[str(player)]] + [self.highestcombo(player)]
            players_and_combos.append(result)
        print(players_and_combos)
        current_best = []
        for player in players_and_combos:
            pass
            #if player[1][0]

    def get_card_nums(self, final_cards):
        lst_of_nums = []
        for item in final_cards:
            lst_of_nums.append(item.number)
        return lst_of_nums

    def get_card_nums_counts(self, final_cards):
        lst_of_nums = self.get_card_nums(final_cards)
        nums_and_counts = []
        nums_alr_there = []
        for num in lst_of_nums:
            #if lst_of_nums.count(num) > 1:
            if num not in nums_alr_there:
                nums_and_counts.append([num, lst_of_nums.count(num)])
                nums_alr_there.append(num)
        return nums_and_counts

    def player_nums_with_board(self, player):
        # Returns the numbers of a player's cards

        final_cards = self.final_cards(player)
        nums_and_counts = self.get_card_nums_counts(final_cards)

        count_lst = []
        for num in nums_and_counts:
            if num not in count_lst:
                count_lst.append(num)
        '''count_lst = []
    for num in lst_of_nums:
      if lst_of_nums.count(num) > 1:
        count_lst.append([num, lst_of_nums.count(num)])'''
        count_lst.sort(key=lambda item: item[0], reverse=True)
        #print('count_lst sorted by highest #: '+str(count_lst))
        count_lst.sort(key=lambda item: item[1], reverse=True)
        #actually don't think the sorting here matters as much as intiially thought, will keep here anyway
        #print('count_lst sorted by highest occurances: '+str(count_lst))

        return count_lst

    def if_straight_flush(self, player):
        lst_of_straights = self.get_straights(player)

        straight_flush = []

        if lst_of_straights:
            for straight in lst_of_straights:  #the list of cards forming staight

                lst_of_suits = []
                for itm in straight:
                    lst_of_suits.append(itm.suit)

                suit_list = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
                flush_cards = []
                for suit in suit_list:
                    if lst_of_suits.count(suit) >= 5:
                        for card in straight:
                            if card.suit == suit:
                                flush_cards.append(card)

                        flush_cards.sort(key=lambda card: card.number,
                                         reverse=True)

                straight_flush.append(flush_cards)
            #print('\n\nstraight_flush:\n\n' + str(straight_flush))
            if straight_flush:
                if straight_flush[0]:
                    return straight_flush
        return None

    def if_royal_flush(self, player):
        result = self.get_straight_flush(player)
        if result:
            if result[0].number == 14:
                return True
        return False

    def final_cards(self, player):
        # Returns a list that includes both the cards on the board and the player's cards
        lst = self.card_board.copy()
        for card in player.cards:
            lst.append(card)
        #print(str(lst))
        #print(lst[0].suit)
        return lst

    def get_pairs(self, player):
        player_nums = self.player_nums_with_board(player)
        #player_nums = self.player_nums(player)
        lst_of_pairs = [item for item in player_nums if item[1] == 2]
        #print('\nlst_of_pairs I think works!\n')
        if lst_of_pairs:
            #print('before sorting')
            #print(str(result))
            #print('\nafter sorting:')
            lst_of_pairs.sort(key=lambda item: item[0], reverse=True)
            final_cards = self.final_cards(player)
            pairs_as_card_objs = [self.cards_from_num(final_cards, pair[0]) for pair in lst_of_pairs]

            #print(str(lst_of_pairs))
            return pairs_as_card_objs

    def cards_from_num(self, final_cards, num):
        cards_w_num = []
        for card in final_cards:
            if card.number == num:
                cards_w_num.append(card)
        return cards_w_num

    def if_one_pair(self, player_nums):
        result = self.get_pairs(
            player_nums
        )  #if I want to optimize, instead of using player_nums as argument, just use result of the .get_pairs instead

        # Code below appends three highest cards to visualize the highest 5 cards possible.
        # I cut it out to simplify code, but can use the logic in GUI or generalize later
        if result:
            # lst_of_leftovers = [
            #     item for item in player_nums if item != result[0]
            # ]
            # lst_of_leftovers.sort(key=lambda item: item[0], reverse=True)
            # result.extend(lst_of_leftovers[:3])
            return True
        return False

    def if_high_card(self, player_nums):
        #player_nums already comes sorted
        result = player_nums[:5]
        return result

    # def get_two_pair(self, player):
    #     player_nums = self.player_nums_with_board(player)
    #     result = self.get_pairs(player_nums)
    #     if result:
    #         if len(result) >= 2:
    #             return
    def if_two_pair(self, player):
        # There is not get_two_pair method, use get_pairs for everything
        # player_nums = self.player_nums_with_board(player)
        result = self.get_pairs(player)

        if result:
            if len(result) >= 2:

                # lst_of_leftovers = [
                #     item for item in player_nums
                #     if (item != result[0]) and (item != result[1])
                # ]
                # lst_of_leftovers.sort(key=lambda item: item[0], reverse=True)
                #
                # if lst_of_leftovers[0][
                #     1] == 2:  #when there are 3 pairs on the board
                #     lst_of_leftovers[0][1] = 1
                #     result.append(lst_of_leftovers[0])
                # else:  #when it is just two pair and all single cards
                #     result.append(lst_of_leftovers[0])
                # #print('result is: '+str(result))
                # return result
                return True
        return False

    def get_three_of_kind(self, player):
        player_nums = self.player_nums_with_board(player)
        lst_of_trips = [item for item in player_nums if item[1] == 3]
        if lst_of_trips:
            lst_of_trips.sort(
                key=lambda item: item[0], reverse=True
            )  #Pretty sure that there are no two sets possible so this line isn't needed but idk fs and I don't want this to break xd

            final_cards = self.final_cards(player)
            trips_as_card_objs = [self.cards_from_num(final_cards, trip[0]) for trip in lst_of_trips]

            return trips_as_card_objs

    def if_three_of_kind(self, player_nums):
        result = self.get_three_of_kind(player_nums)
        #There will be no pairs (and 2nd trip-s from the 7 cards) along with the first set, as this will be covered if if_fullhouse

        if result:
            # lst_of_leftovers = [
            #     item for item in player_nums if item != result[0]
            # ]
            # lst_of_leftovers.sort(key=lambda item: item[0], reverse=True)
            # output = result.copy()
            # if lst_of_leftovers[0][1] == 2:
            #     result.append(lst_of_leftovers[0])
            # else:
            #     result.append(lst_of_leftovers[0])
            #     result.append(lst_of_leftovers[1])
            # #print('result is: '+str(result))
            # return result
            return True
        return False

    def get_fullhouse(self, player):
        trips = self.get_three_of_kind(player)
        pair = self.get_pairs(player)
        if trips == None or pair == None:
            return None
        fullhouse = trips[0] + pair[0]
        return fullhouse

    def if_fullhouse(self, player):
        fullhouse = self.get_fullhouse(player)
        if fullhouse:
            return True
        return False
    def get_quads(self, player):
        player_nums = self.player_nums_with_board(player)
        lst_of_quads = [item for item in player_nums if item[1] == 4]
        if lst_of_quads:
            lst_of_quads.sort(
                key=lambda item: item[0], reverse=True
            )  #Pretty sure that there are no two sets possible so this line isn't needed but idk fs and I don't want this to break xd

            final_cards = self.final_cards(player)
            quads_as_card_objs = [self.cards_from_num(final_cards, trip[0]) for trip in lst_of_quads]

            return quads_as_card_objs
    def if_quads(self, player):
        quads = self.get_quads(player)
        if quads:
            return True
        return False

    def get_flushes(self, player):
        final_cards = self.final_cards(player)
        lst_of_cards_sorted = sorted(final_cards, key=lambda card: card.number,
                                     reverse=True)
        lst_of_suits = []
        for itm in final_cards:
            lst_of_suits.append(itm.suit)
        #print('lst_of_suits: '+str(lst_of_suits))

        suit_list = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
        flush_cards = []
        flush_suit = ""
        for suit in suit_list:
            suit_count = 0
            for card in lst_of_cards_sorted:
                if card.suit == suit:
                    suit_count += 1
            if suit_count >= 5:
                flush_suit = suit

        for card in lst_of_cards_sorted:
            if card.suit == flush_suit:
                flush_cards.append(card)
        return flush_cards
    def if_flush(self, player):
        flushes = self.get_flushes(player)
        if flushes:
            return True
        return False


    def if_straight(self, player):
        result = self.get_straights(player)
        if result:
            return True
        return False

    def get_straights(self, player):
        final_cards = self.final_cards(player)

        # lst_of_nums = self.get_card_nums(final_cards)
        #print(lst_of_nums)

        # lst_of_nums.sort(reverse=True)
        lst_of_cards_sorted = sorted(final_cards, key=lambda card: card.number,
                                 reverse=True)
        #print('lst_of_nums after being sorted: '+str(lst_of_nums))

        # In the case the highest card has two, then it would not match the next check below

        # get the cards with unique numbers
        list_of_cards_w_nums_unique = []
        lst_of_nums = []
        for card in lst_of_cards_sorted:
            if card.number not in lst_of_nums:
                list_of_cards_w_nums_unique.append(card)
                lst_of_nums.append(card.number)

        highest_straight_cards = []

        # get all the possible cards that can make straights
        number_of_cards_w_nums_unique = len(list_of_cards_w_nums_unique)
        for i in range(number_of_cards_w_nums_unique - 1):
            j = i
            counter = 1
            while (j < number_of_cards_w_nums_unique - 1) and \
                    (list_of_cards_w_nums_unique[j].number - list_of_cards_w_nums_unique[j+1].number == 1):
                j += 1
                counter += 1
            if counter >= 5:
                highest_straight_cards.append(list_of_cards_w_nums_unique[i:i+5])
                continue
        return highest_straight_cards

    def get_highest_straight(self, player):
        straights = self.get_straights(player)
        if straights:
            return straights[0]
        return None

    def get_straight_flush(self, player):
        straights = self.get_straights(player)
        if straights:
            for straight in straights:
                straight_is_also_flush = True
                suit = straight[0].suit
                for card in straight:
                    if card.suit != suit:
                        straight_is_also_flush = False
                if straight_is_also_flush:
                    return straight
        return None

    def if_straight_flush(self, player):
        straight_flush = self.get_straight_flush(player)
        if straight_flush:
            return True
        return False

#game.cards.shuffle()
#game.cards.deal(game.card_board, 5)
'''test_card = Card(14, 'Ace', 'Hearts')
test_card.showing = True
game.card_board.append(test_card)

test_card = Card(9, '9', 'Hearts')
test_card.showing = True
game.card_board.append(test_card)

test_card = Card(7, '7', 'Clubs')
test_card.showing = True
game.card_board.append(test_card)

test_card = Card(13, 'King', 'Hearts')
test_card.showing = True
game.card_board.append(test_card)

test_card = Card(2, '2', 'Spades')
test_card.showing = True
game.card_board.append(test_card)'''

#print(str(game.card_board))

#print('\nThe players cards are: ')
#game.deal_cards_all_players()
#for player in game.positioned:
#  print(str(player.cards))
'''test_card = Card(5, '5', 'Spades')
test_card.showing = True
player1.cards.append(test_card)

test_card = Card(4, '4', 'Clubs')
test_card.showing = True
player.cards.append(test_card)'''

print('\n')
#game.player_nums(player1)
'''print('highest combo for player1: ')
game.highestcombo(player1)

print('\n\n')

print('highest combo for player2: ')
game.highestcombo(player2)

print('\n\n')

print('highest combo for player3: ')
game.highestcombo(player3)

print('\n\n')

print('highest combo for player4: ')
game.highestcombo(player4)'''
#game.checker()
#need to have it by the cards, not just the numbers
