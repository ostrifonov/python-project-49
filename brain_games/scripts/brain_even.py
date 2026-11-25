from brain_games.cli import welcome_user
from brain_games.games.game_even import game_even
from brain_games.games.game_logic import game_logic

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():

    name = welcome_user()

    if game_logic(name, game_even, RULE):
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
