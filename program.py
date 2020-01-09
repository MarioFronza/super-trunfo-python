import random
import sys

import data
from app.models.card import Card
from app.models.player import Player
from app.structs.queue import Queue

cards = data.get_all_cards()


def main():
    print_header()
    shuffle_cards()
    user_intent = get_user_intent()
    if user_intent == "yes":
        game_loop()
    else:
        sys.exit()


def print_header():
    print("****************  SUPER TRUNFO 2  ****************")
    print()
    print("Welcome to Super Trunfo 2!")
    print("Are you ready to play?")
    print()


def get_user_intent() -> str:
    print("[y] Yes")
    print("[n] No")
    print()
    choice = input("[Y]es or [N]o? ")
    if choice.lower() == "y":
        return "yes"

    return "no"


def shuffle_cards():
    random.shuffle(cards, random.random)


def show_each_card():
    for card in cards:
        print(cards.index(card) + 1, card)


def put_cards_on_queue(player_cards: [Card]) -> Queue:
    queue_cards = Queue()
    for card in player_cards:
        queue_cards.enqueue(card)

    return queue_cards


def get_deal(player_card: Queue) -> [Card]:
    deal = []
    for i in range(0, 5):
        deal.append(player_card.dequeue())

    return deal


def game_loop():
    user_cards = put_cards_on_queue(cards[0:10])
    bot_cards = put_cards_on_queue(cards[10:])

    user_deal = get_deal(user_cards)
    bot_deal = get_deal(bot_cards)

    user = Player("Mário", user_deal, user_cards)
    user.print_deal()
    print()
    user.print_cards()


if __name__ == "__main__":
    main()
