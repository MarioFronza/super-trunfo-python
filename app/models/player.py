from app.structs.queue import Queue


class Player:
    def __init__(self, name: str, deal, cards: Queue):
        self.name = name
        self.deal = deal
        self.cards = cards

    def __str__(self):
        return "name: {0}".format(self.name)

    def print_deal(self):
        for card in self.deal:
            print(card)

    def print_cards(self):
        for card in self.cards:
            print(card)
