from Card import Card
import random


class Deck:
    def __init__(self):
        self.suits = '♠♥♦♣'

    def make_deck(self):
        self.deck = []

        for suit in self.suits:
            for i in range(1, 14):
                l = ''
                if i == 1:
                    l = 'A'
                elif i == 11:
                    l = 'J'
                elif i == 12:
                    l = 'Q'
                elif i == 13:
                    l = 'K'
                else:
                    l = str(i)
                self.deck.append((Card(l, i, suit)))

    def print_deck(self):
        for card in self.deck:
            print(f"{card.get_val()} {card.get_suit()}")

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop(0)

    def cut(self):
        return self.deck.pop(random.randrange(0, len(self.deck)))


d = Deck()
