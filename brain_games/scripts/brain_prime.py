from brain_games.cli import welcome_user
from brain_games.games.game_prime import game_prime
from brain_games.games.game_logic import game_logic

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():

    name = welcome_user()

    if game_logic(name, game_prime, RULE):
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
