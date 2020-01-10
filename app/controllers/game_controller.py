import random

from app.models.card import Card
from app.models.player import Player
from app.structs.queue import Queue

from app.observer.observed import Observed
from app.observer.observer import Observer
from typing import List


class GameController(Observed):

    turn = random.randint(0, 1)
    current_round = 1
    _observers: List[Observer] = []

    def __init__(self, user_name: str, cards: [Card]):
        self.cards = cards
        self.shuffle_cards()
        self.user = Player(user_name, self.prepare_cards(self.cards[0:10]))
        self.bot = Player("Bot", self.prepare_cards(self.cards[10:]))

    def prepare_cards(self, player_cards: [Card]) -> Queue:
        queue_cards = Queue()
        for card in player_cards:
            queue_cards.enqueue(card)
        return queue_cards

    def shuffle_cards(self):
        random.shuffle(self.cards, random.random)

    def verify_winner(self):
        if self.user.is_deal_empty():
            self.notify_winner(self.user)
        elif self.bot.is_deal_empty():
            self.notify_winner(self.bot)

    def play(self):
        if self.turn == 0:
            self.user_turn()
        else:
            self.bot_turn()

        self.verify_winner()
        self.switch_turn()

    def user_turn(self):
        print("Please, choose a card")
        print()
        self.user.print_deal()
        card_choice = -1
        while card_choice <= 0 or card_choice > len(self.user.deal):
            card_choice = int(input("Card number: "))

        user_card = self.user.get_deal_card(card_choice - 1)
        print(user_card)
        print("Now, choose an attribute")
        print("[1] Age " + str(user_card.age))
        print("[2] Size " + str(user_card.size))
        print("[3] Height " + str(user_card.height))
        print("[4] Weight " + str(user_card.weight))
        attr_choice = -1
        while attr_choice <= 0 or attr_choice >= 5:
            attr_choice = int(input("Attribute number: "))

        user_card_attribute = user_card.get_attr_by_number(attr_choice)
        bot_card = self.bot.get_deal_card(random.randint(0, len(self.bot.deal) - 1))
        bot_card_attribute = bot_card.get_attr_by_number(attr_choice)
        print(user_card.name + " X " + bot_card.name)
        if user_card_attribute > bot_card_attribute:
            print("You Win!")
        else:
            print("You loose :(")

    def bot_turn(self):
        bot_card = self.bot.get_deal_card(random.randint(0, len(self.bot.deal) - 1))
        attr_number = random.randint(1, 4)
        bot_card_attribute = bot_card.get_attr_by_number(attr_number)
        print("Please, choose a card")
        self.user.print_deal()
        card_choice = -1
        while card_choice <= 0 or card_choice > len(self.user.deal):
            card_choice = int(input("Card number: "))

        user_card = self.user.get_deal_card(card_choice - 1)
        print(user_card)

        user_card_attribute = user_card.get_attr_by_number(attr_number)
        print(user_card.name + " X " + bot_card.name)
        if user_card_attribute > bot_card_attribute:
            print("You Win!")
        else:
            print("You loose :(")

    def switch_turn(self):
        if self.turn == 0:
            self.turn = 1
        else:
            self.turn = 0
        self.current_round += 1

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def notify_winner(self, player: Player) -> None:
        for observer in self._observers:
            observer.winner(player)
