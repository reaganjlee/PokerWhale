

class Pot(object):
    def __init__(self, pot_amt):
        self.participants = []
        self.pot_amt = pot_amt
        self.table_stake = 0
        # self.stake_gap = 0
        # self.req_min_raise_diff = big_blind_amt

    def add_participant(self, participant):
        self.participants.append(participant)

    def add_lst_participants(self, participants):
        for participant in participants:
            self.participants.append(participant)

    def add_amt(self, amt):
        self.pot_amt += amt

    def __repr__(self):
        # return float(self.pot_amt)
        return "Participants: " + self.participants \
            + "\nPot amount: " + self.pot_amt