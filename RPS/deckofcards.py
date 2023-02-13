import random


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def count(self):
        return len(self.cards)

    def __repr__(self):
        return "Deck of " + str(self.count()) + " cards"

    def _deal(self, amt):
        if self.count() == 0:
            raise ValueError("All cards have been dealt")

        if self.count() < amt:
            amt = self.count()

        cards = []
        for num in range(amt):
            cards.append(self.cards.pop())
        return cards

    def shuffle(self):
        if self.count() != 52:
            raise ValueError("Only full decks can be shuffled")

        random.shuffle(self.cards)

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, num):
        return self._deal(num)


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return self.value + " of " + self.suit
