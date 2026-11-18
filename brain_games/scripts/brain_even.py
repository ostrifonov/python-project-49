
from brain_games.cli import welcome_user
from brain_games.game_even import game


def main():
    name = welcome_user()
    game(name)


if __name__ == "__main__":
    main()