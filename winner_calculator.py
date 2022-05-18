#from cards import deck
#from players import player1, player2, player3, player4
from main import game
print('this loaded 1')

game.card_board = []
game.deck.shuffle()
game.deck.deal(game.card_board, 5)
print(str(game.card_board))
print('this loaded')


class win_calculator(object):
    def __init__(self, card_board, players):
        self.card_board = card_board
        self.players = players


        #calculating the winner

        def highestcombo(self, player):
            player_nums = self.player_nums(player)

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

            result = self.if_quads(player_nums)
            if result:
                # print('result of if_quads below')
                print(str(result))
                return result

            result = self.if_fullhouse(player_nums)
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

            result = self.if_set(player_nums)
            if result:
                # print('result of if_set below')
                print(str(result))
                return result

            result = self.if_two_pair(player_nums)
            if result:
                # print('result of if_two_pair below')
                print(str(result))
                return result

            result = self.if_one_pair(player_nums)
            #print('testingxd')
            if result:
                # print('result of if_one_pair below')
                print(str(result))
                return result
            print('\n\n')
            '''print(str(self.if_fullhouse))'''

            result = self.if_high_card(player_nums)
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

        def player_nums(self, player):
            lst = self.final_cards(player)

            lst_of_nums = []
            for item in lst:
                lst_of_nums.append(item.number)
            #print(lst_of_nums)

            #cnt = Counter(lst_of_nums)
            #count_list = [k for k, v in cnt.iteritems() if v > 1]
            #[num for num in lst_of_nums if lst_of_nums.count(num)>1]

            placeholder = []
            for num in lst_of_nums:
                #if lst_of_nums.count(num) > 1:
                placeholder.append([num, lst_of_nums.count(num)])

            count_lst = []
            for num in placeholder:
                if num not in count_lst:
                    count_lst.append(num)
            '''count_lst = []
        for num in lst_of_nums:
          if lst_of_nums.count(num) > 1:
            count_lst.append([num, lst_of_nums.count(num)])'''
            #print('count_lst before: '+str(count_lst))
            count_lst.sort(key=lambda item: item[0], reverse=True)
            #print('count_lst sorted by highest #: '+str(count_lst))
            count_lst.sort(key=lambda item: item[1], reverse=True)
            #actually don't think the sorting here matters as much as intiially thought, will keep here anyway
            #print('count_lst sorted by highest occurances: '+str(count_lst))

            #print(str(count_lst))
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
            result = self.if_straight_flush(player)
            if result:
                if result[0]:
                    if result[0][0].number == 14:
                        return result[0]
            return None

        def final_cards(self, player):
            lst = self.card_board.copy()
            for card in player.cards:
                lst.append(card)
            #print(str(lst))
            #print(lst[0].suit)
            return lst

        def get_pairs(self, player_nums):
            #player_nums = self.player_nums(player)
            lst_of_pairs = [item for item in player_nums if item[1] == 2]
            #print('\nlst_of_pairs I think works!\n')
            if lst_of_pairs:
                #print('before sorting')
                #print(str(result))
                #print('\nafter sorting:')
                lst_of_pairs.sort(key=lambda item: item[0], reverse=True)

                #print(str(lst_of_pairs))
                return lst_of_pairs

        def if_one_pair(self, player_nums):
            result = self.get_pairs(
                player_nums
            )  #if I want to optimize, instead of using player_nums as argument, just use result of the .get_pairs instead
            if result:
                lst_of_leftovers = [
                    item for item in player_nums if item != result[0]
                ]
                lst_of_leftovers.sort(key=lambda item: item[0], reverse=True)
                result.extend(lst_of_leftovers[:3])
                return result
            return None

        def if_high_card(self, player_nums):
            #player_nums already comes sorted
            result = player_nums[:5]
            return result

        def if_two_pair(self, player_nums):
            result = self.get_pairs(player_nums)

            if result:
                if len(result) >= 2:

                    lst_of_leftovers = [
                        item for item in player_nums
                        if (item != result[0]) and (item != result[1])
                    ]
                    lst_of_leftovers.sort(key=lambda item: item[0], reverse=True)

                    if lst_of_leftovers[0][
                        1] == 2:  #when there are 3 pairs on the board
                        lst_of_leftovers[0][1] = 1
                        result.append(lst_of_leftovers[0])
                    else:  #when it is just two pair and all single cards
                        result.append(lst_of_leftovers[0])
                    #print('result is: '+str(result))
                    return result
            return None

        def get_sets(self, player_nums):
            lst_of_sets = [item for item in player_nums if item[1] == 3]
            #print('\n think this works for the get_sets function!\n')
            if lst_of_sets:
                lst_of_sets.sort(
                    key=lambda item: item[0], reverse=True
                )  #Pretty sure that there are no two sets possible so this line isn't needed but idk fs and I don't want this to break xd

                #print(str(lst_of_sets))
                return lst_of_sets

        def if_set(self, player_nums):
            result = self.get_sets(player_nums)
            #There will be no pairs (and 2nd sets from the 7 cards) along with the first set, as this will be covered if if_fullhouse

            if result:
                lst_of_leftovers = [
                    item for item in player_nums if item != result[0]
                ]
                lst_of_leftovers.sort(key=lambda item: item[0], reverse=True)
                output = result.copy()
                if lst_of_leftovers[0][1] == 2:
                    result.append(lst_of_leftovers[0])
                else:
                    result.append(lst_of_leftovers[0])
                    result.append(lst_of_leftovers[1])
                #print('result is: '+str(result))
                return result
            return None

        def if_fullhouse(self, player_nums):
            result = self.get_sets(player_nums)
            if result:
                top_set = result.pop(0)

                get_pairs_result = self.get_pairs(player_nums)
                if get_pairs_result:
                    lst_of_leftovers = result + get_pairs_result

                    lst_of_leftovers.sort(key=lambda item: item[0], reverse=True)

                    result = [top_set.copy()]
                    result.append(lst_of_leftovers[0])
                    print('result is: ' + str(result))
                    return result
            return None

        def if_quads(self, player_nums):
            lst_of_quads = [item for item in player_nums if item[1] == 4]
            lst_of_leftovers = [item for item in player_nums if item[1] != 4]
            #print('\n think this works for the if_quads function!\n')
            if lst_of_quads:
                lst_of_quads.sort(
                    key=lambda item: item[0], reverse=True
                )  #Pretty sure that there are no two sets possible so this line isn't needed but idk fs and I don't want this to break xd
                #print('player_nums: ' + str(player_nums))

                #print('lst_of_quads: '+str(lst_of_quads))
                #print('lst_of_leftovers: '+str(lst_of_leftovers))

                lst_of_quads.append(lst_of_leftovers[0])
                return lst_of_quads

        def if_flush(
                self, player
        ):  #sort by nums, then keep the ones that are in the same suit?

            #then when comparing flushes just use the first 5, need the extra when seeing if straight flush possible
            lst = self.final_cards(player)
            #  self.card_board.copy()
            #for card in player.cards:
            #  lst.append(card)
            #print(str(lst))
            #print(lst[0].suit)

            lst_of_suits = []
            for itm in lst:
                lst_of_suits.append(itm.suit)
            #print('lst_of_suits: '+str(lst_of_suits))

            suit_list = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
            flush_cards = []
            for suit in suit_list:
                if lst_of_suits.count(suit) >= 5:
                    #print(str(suit))
                    #print('We have a flush!')
                    for card in lst:
                        if card.suit == suit:
                            flush_cards.append(card)

                    flush_cards.sort(key=lambda card: card.number, reverse=True)
                    flush_cards = flush_cards[:5]
                    print('the flush_cards are: ' + str(flush_cards))
                    return flush_cards
            #print('no flush!')
            return None

        def if_straight(self, player):
            result = self.get_straights(player)
            if result:
                return result[0]
            return None

        def get_straights(self, player):
            lst = self.final_cards(player)

            lst_of_nums = []
            for itm in lst:
                lst_of_nums.append(itm.number)
            #print(lst_of_nums)

            lst_of_nums.sort(reverse=True)
            #print('lst_of_nums after being sorted: '+str(lst_of_nums))

            list_of_nums_unique = []
            for num in lst_of_nums:
                if num not in list_of_nums_unique:
                    list_of_nums_unique.append(num)

            highest_straight_nums = []

            for index in range(len(list_of_nums_unique) - 4):
                '''i=index
          count = 0
          while (i < len(list_of_nums_unique)-1) and (list_of_nums_unique[i] == list_of_nums_unique[i+1] + 1):
            count +=1
            i+=1
          if count >=5:
            highest_straight_nums.extend(list_of_nums_unique[index:index+count])'''
                if list_of_nums_unique[index] - list_of_nums_unique[index +
                                                                    1] == 1:
                    if list_of_nums_unique[index +
                                           1] - list_of_nums_unique[index +
                                                                    2] == 1:
                        if list_of_nums_unique[index +
                                               2] - list_of_nums_unique[index +
                                                                        3] == 1:
                            if list_of_nums_unique[
                                index + 3] - list_of_nums_unique[index +
                                                                 4] == 1:
                                highest_straight_nums.extend(
                                    [list_of_nums_unique[index:index + 5]])

            #print('highest_straight_nums: '+str(highest_straight_nums))

            highest_straight = [[] for _ in highest_straight_nums]
            #[[]]* len(highest_straight_nums)
            #print(str(len(highest_straight_nums)))

            for i in range(len(highest_straight_nums)):
                #print('\ni: '+str(i))
                #print(str(highest_straight))
                nums_alr_in = []

                for card in lst:
                    #print(card)
                    #print(highest_straight_nums[i])
                    if (card.number in highest_straight_nums[i]) and (
                            card.number not in nums_alr_in):  #highest_straight[i]
                        nums_alr_in.append(card.number)
                        #print('nums_alr_in: '+ str(nums_alr_in))

                        #print(str(highest_straight[i]))
                        highest_straight[i].append(card)
                        #print('highest_straight2: '+ str(highest_straight))

                highest_straight[i].sort(key=lambda card: card.number,
                                         reverse=True)

            #print('\nhighest_straight: '+str(highest_straight))
            if highest_straight:
                return highest_straight
            return None



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
