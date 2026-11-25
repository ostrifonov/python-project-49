from brain_games.cli import welcome_user
from brain_games.games.game_calc import game_calc
from brain_games.games.game_logic import game_logic

RULE = "What is the result of the expression?"


def main():

    name = welcome_user()

    if game_logic(name, game_calc, RULE):
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
