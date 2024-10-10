class Card:
    def __init__(self, val, num_val, suit):
        self.val = val
        self.num_val = num_val
        self.suit = suit

    def get_suit(self):
        return self.suit

    def get_val(self):
        return self.val

    def get_num_val(self):
        return self.num_val

    def show_card(self):
        return f"{self.val}{self.suit}"

    def convert_val(self):
        if self.val in self.values.keys():
            self.true_val = self.values[f"{self.val}"]
        return self.true_val
