import sys

from brain_games.cli import welcome_user
from brain_games.games.game_calc import game_calc
from brain_games.games.game_even import game_even
from brain_games.games.game_gcd import game_gcd
from brain_games.games.game_prime import game_prime
from brain_games.games.game_progression import game_progression

MIN_RANGE_VALUE = 1
MAX_RANGE_VALUE = 100
ROUNDS = 3
GAME_RULES = {
    'game_even': 'Answer "yes" if the number is even, otherwise answer "no".',
    'game_calc': "What is the result of the expression?",
    'game_gcd': "Find the greatest common divisor of given numbers.",
    'game_progression': "What number is missing in the progression?",
    'game_prime': 'Answer "yes" if given number is prime. ' 
    'Otherwise answer "no".',
}


def end_game(end_flag: bool):
    if not end_flag:
        sys.exit()


def game_logic(game_name: str):
    name = welcome_user()

    for _ in range(ROUNDS):

        match game_name:

            case "game_even":
                print(GAME_RULES["game_even"])
                end_flag = game_even(
                    name,
                    MIN_RANGE_VALUE,
                    MAX_RANGE_VALUE,
                )
                end_game(end_flag)

            case "game_calc":
                print(GAME_RULES["game_calc"])
                end_flag = game_calc(
                    name,
                    MIN_RANGE_VALUE,
                    MAX_RANGE_VALUE,
                )
                end_game(end_flag)

            case "game_gcd":
                print(GAME_RULES["game_gcd"])
                end_flag = game_gcd(
                    name,
                    MIN_RANGE_VALUE,
                    MAX_RANGE_VALUE,
                )
                end_game(end_flag)

            case "game_progression":
                print(GAME_RULES["game_progression"])
                end_flag = game_progression(
                    name,
                    MIN_RANGE_VALUE,
                    MAX_RANGE_VALUE,
                )
                end_game(end_flag)

            case "game_prime":
                print(GAME_RULES["game_prime"])
                end_flag = game_prime(
                    name,
                    MIN_RANGE_VALUE + 1,
                    MAX_RANGE_VALUE,
                )
                end_game(end_flag)

    print(f"Congratulations, {name}!")
