import sys


def main():
    print_header()
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


def game_loop():
    print("Olá")


if __name__ == "__main__":
    main()
