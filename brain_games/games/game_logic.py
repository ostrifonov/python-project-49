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
    'game_calc': 'What is the result of the expression?',
    'game_gcd': 'Find the greatest common divisor of given numbers.',
    'game_progression': 'What number is missing in the progression?',
    'game_prime': 'Answer "yes" if given number is prime. '
    'Otherwise answer "no".',
}


def game_logic(name: str, game_name: str) -> bool:

    print(GAME_RULES[game_name])
    is_win = True

    for _ in range(ROUNDS):

        match game_name:
            case "game_even":
                is_win = game_even(
                    name,
                    MIN_RANGE_VALUE,
                    MAX_RANGE_VALUE,
                )
            case "game_calc":
                is_win = game_calc(
                    name,
                    MIN_RANGE_VALUE,
                    MAX_RANGE_VALUE,
                )
            case "game_gcd":
                is_win = game_gcd(
                    name,
                    MIN_RANGE_VALUE,
                    MAX_RANGE_VALUE,
                )
            case "game_progression":
                is_win = game_progression(
                    name,
                    MIN_RANGE_VALUE,
                    MAX_RANGE_VALUE,
                )
            case "game_prime":
                is_win = game_prime(
                    name,
                    MIN_RANGE_VALUE,
                    MAX_RANGE_VALUE,
                )
        if not is_win:
            return False

    if is_win:
        return True
