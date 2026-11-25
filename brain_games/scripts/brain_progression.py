from brain_games.cli import welcome_user
from brain_games.games.game_logic import game_logic
from brain_games.games.game_progression import RULE, game_progression


def main():

    name = welcome_user()

    if game_logic(name, game_progression, RULE):
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
