from app.structs.queue import Queue
from app.models.card import Card


class Player:
    def __init__(self, name: str, cards: Queue):
        self.name = name
        self.cards = cards
        self.deal = self.create_deal()

    def __str__(self):
        return "name: {0}".format(self.name)

    def create_deal(self):
        deal = []
        for i in range(0, 5):
            deal.append(self.cards.dequeue())

        return deal

    def get_first_card(self):
        if not self.is_card_empty():
            self.deal.append(self.cards.dequeue())

    def get_deal_card(self, card_number: int) -> Card:
        card = None
        if not self.is_deal_empty():
            card = self.deal[card_number]
            self.deal.remove(card)
            self.get_first_card()

        return card

    def add_new_card(self, card: Card):
        self.cards.enqueue(card)

    def is_card_empty(self):
        return self.cards.is_empty()

    def is_deal_empty(self):
        return len(self.deal) == 0

    def print_deal(self):
        for card in self.deal:
            print("[" + str(self.deal.index(card) + 1) + "] " + str(card))

    def print_cards(self):
        for card in self.cards:
            print(card)
