from brain_games.cli import welcome_user
from brain_games.games.game_gcd import game_gcd
from brain_games.games.game_logic import game_logic

RULE = "Find the greatest common divisor of given numbers."


def main():

    name = welcome_user()

    if game_logic(name, game_gcd, RULE):
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
