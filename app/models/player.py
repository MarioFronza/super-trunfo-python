from app.structs.queue import Queue


class Player:
    def __init__(self, name: str, cards: Queue):
        self.name = name
        self.cards = cards
        self.deal = self.create_deal()

    def __str__(self):
        return "name: {0}".format(self.name)

    def print_deal(self):
        for card in self.deal:
            print(card)

    def create_deal(self):
        deal = []
        for i in range(0, 5):
            deal.append(self.cards.dequeue())

        return deal

    def print_cards(self):
        for card in self.cards:
            print(card)
