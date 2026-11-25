MIN_RANGE_VALUE = 1
MAX_RANGE_VALUE = 100
ROUNDS = 3


def game_logic(name: str, game, rule: str) -> bool:

    print(rule)

    is_win = True

    for _ in range(ROUNDS):

        if not game(name, MIN_RANGE_VALUE, MAX_RANGE_VALUE):
            return False

    return True
