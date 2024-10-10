from Card import Card
from itertools import combinations


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.values = {"A": 1, "J": 10, "Q": 10, "K": 10}
        self.score = 0
        self.suits = "♠♥♦♣"
        self.pegging_hand = []

    def set_hand(self, card):
        self.hand.append(card)
        self.pegging_hand.append(card)

    def get_hand(self):
        hand = ""
        for card in self.hand:
            hand += f"{card.show_card()} "

        return hand

    def add_score(self, s):
        self.score += s
        return s

    def crib_card(self, indexs):
        crib = []
        for c in indexs:
            crib.append(self.hand[int(c) - 1])
        for card in crib:
            self.hand.remove(card)

        return crib

    def find_15s(self):
        target = 15
        total = 0
        arr = []
        p = []

        hand_vals = []
        for card in self.hand:
            cval = card.get_val()
            if cval in self.values.keys():
                cval = self.values[cval]
            hand_vals.append(int(cval))

        if len(hand_vals) > 0:
            for r in range(0, len(hand_vals) + 1):
                arr += list(combinations(hand_vals, r))
            for item in arr:
                if sum(item) == target:
                    p.append(item)

        total = len(p) * 2
        self.score += total

        return total

    def find_pairs(self, hand_vals):
        total = 0
        for i in range(1, 14):
            if hand_vals.count(i) == 2:
                total += 2
            elif hand_vals.count(i) == 3:
                total += 6
            elif hand_vals.count(i) == 4:
                total += 12

        self.score += total

        return total

    def find_straights(self, hand_vals):
        straight_checker = "1 2 3 4 5 6 7 8 9 10 11 12 13"
        arr = []
        p = []
        total = 0

        if len(hand_vals) > 0:
            for r in range(0, len(hand_vals) + 1):
                arr += list(combinations(hand_vals, r))
            for item in arr:
                # these tuples are straight potentials (at least three cards long)
                if len(item) >= 3:
                    p.append(item)

        straight_len = 0

        for item in reversed(p):
            i = " ".join(map(str, item))

            if i in straight_checker and len(item) >= straight_len:
                straight_len = len(item)
                total += len(item)

        self.score += total
        return total

    def find_flush(self):
        suits = []
        total = 0
        for card in self.hand:
            suits.append(card.get_suit())
        pass

        for suit in self.suits:
            suit_count = suits.count(suit)  # number of cards with each suit

            if (
                suit_count >= 4
            ):  # if it meets flush requirement add to score the amount of cards with that suit
                total += suit_count

        return total

    def scoring(self, cut_card):
        self.hand.append(cut_card)

        hand_vals = []

        for card in self.hand:
            cval = card.get_num_val()
            hand_vals.append(cval)

        hand_vals.sort()

        # calculate 15s
        print(f"15s: {self.find_15s()}")

        # calculate pairs
        print(f"Pairs: {self.find_pairs(hand_vals)}")

        # calculate straights
        print(f"Straights: {self.find_straights(hand_vals)}")

        # calculate flush
        print(f"Flush: {self.find_flush()}")
        return self.score
