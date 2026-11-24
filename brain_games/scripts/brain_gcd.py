from brain_games.cli import welcome_user
from brain_games.games.game_logic import game_logic


def main():

    name = welcome_user()

    if game_logic(name, "game_gcd"):
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
