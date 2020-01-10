import random
import sys

import data
from app.controllers.game_controller import GameController
from app.observer.observer import Observer


class Program(Observer):
    def __init__(self):
        pass

    def init(self):
        self.print_header()
        user_intent = self.get_user_intent()
        if user_intent == "yes":
            name = input("Enter yout name: ")
            self.game_loop(name)
        else:
            sys.exit()

    def print_header(self):
        print("****************  SUPER TRUNFO 2  ****************")
        print()
        print("Welcome to Super Trunfo 2!")
        print("Are you ready to play?")
        print()

    def get_user_intent(self) -> str:
        print("[y] Yes")
        print("[n] No")
        print()
        choice = input("[Y]es or [N]o? ")
        if choice.lower() == "y":
            return "yes"

        return "no"

    def game_loop(self, name: str):
        game_controller = GameController(name, data.get_all_cards())
        game_controller.attach(self)
        while True:
            game_controller.play()

    def winner(self, player):
        print(player.name + " won the game!")
        sys.exit()


if __name__ == "__main__":
    program = Program()
    program.init()

