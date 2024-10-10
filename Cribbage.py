from Deck import Deck
from Card import Card
from Player import Player


class Cribbage:
    def __init__(self):
        self.deck = Deck()
        self.players = [None]
        self.current_crib = None
        self.crib = Player("crib")

    def create_players(self, num_players):
        for i in range(num_players):
            name = input(f"What is your name Player {i+1} ? ")
            self.players.append(Player(name))

    def redo_deck(self):
        self.deck.make_deck()
        self.deck.shuffle()

    def first_crib(self):
        while True:
            # player one cut
            input(f"{self.players[1].name}, press enter to cut ")
            c1 = self.deck.cut()
            print(f"{self.players[1].name}, has cut {c1.show_card()}")

            # player two cut
            input(f"{self.players[2].name}, press enter to cut ")
            c2 = self.deck.cut()
            print(f"{self.players[2].name}, has cut {c2.show_card()}")

            if c1.get_num_val() == c2.get_num_val():
                print("It was a tie! Cut again...")
                continue

            self.current_crib = (
                self.players[1]
                if c1.get_num_val() > c2.get_num_val()
                else self.players[2]
            )

            print(f"It is {self.current_crib.name}'s crib first")

            break

    def create_crib(self):
        """
        Players each place 2 cards from their hand into the crib. One player will count the points in the crib
        towards their collective score at the end of the pegging round
        """

        # player one adds to crib
        for player in self.players:
            if player is None:
                continue

            print(f"{player.name}, here is your hand: {player.get_hand()}")

            while True:
                i = input("What two cards would you like to place in the crib? ")

                if len(i) == 2 and i.isnumeric():
                    for card in player.crib_card(i):
                        self.crib.set_hand(card)
                    break

            print(f"Crib: {self.crib.get_hand()}")
            print(f"{player.name} hand: {player.get_hand()}")

    def pegging_round(self):
        # player without the crib goes first
        p1_turn = self.current_crib != self.players[1]
        p1_len = len(self.players[1].pegging_hand)
        p2_len = len(self.players[2].pegging_hand)
        count = 0

        # a player still has a card to play
        # while p1_len + p2_len >= 1:
        #     p1_lowest_card = min([card.get_num_val()  # lowest card in P1 hand to play
        #                           for card in self.players[1].pegging_hand])
        #     p2_lowest_card = min([card.get_num_val()  # lowest card in P2 hand to play
        #                           for card in self.players[2].pegging_hand])

        #     if p1_turn:  # player 1 turn
        #         if p1_len >= 1 and p1_lowest_card + count <= 31:
        #             print("Player one turn")

        #     else:  # player 2 turn
        #         if p2_len >= 1 and p2_lowest_card + count <= 31:

        #             print("Player one turn")

    def scoring(self):
        for player in self.players:
            if player is None:
                continue

            print(
                f"{player.name} scored {player.scoring(self.cut_card)} points in their hand:"
            )
            print(player.get_hand())
        print(
            f"{self.current_crib.name} also has {self.current_crib.add_score(self.crib.scoring(self.cut_card))} points in their crib:"
        )
        print(self.crib.get_hand())

    def main(self):
        self.create_players(2)
        # shuffle deck
        self.redo_deck()

        # determine who has first crib
        self.first_crib()

        # shuffle again
        self.redo_deck()

        # deal hands
        for i in range(6):
            self.players[1].set_hand(self.deck.deal_card())
            self.players[2].set_hand(self.deck.deal_card())

        # players put cards into crib
        self.create_crib()

        # cut card
        input(f"{self.current_crib.name} please cut the deck by pressing enter ")
        self.cut_card = self.deck.cut()
        print(f"The cut card is: {self.cut_card.show_card()}")

        # Pegging round
        self.pegging_round()

        # count points in hands and crib
        self.scoring()


game = Cribbage()
game.main()
