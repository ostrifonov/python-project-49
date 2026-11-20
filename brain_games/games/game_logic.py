from brain_games.cli import welcome_user
from brain_games.games.game_calc import game_calc
from brain_games.games.game_even import game_even

MIN_RANGE_VALUE = 1
MAX_RANGE_VALUE = 100
ROUNDS = 3
RULES = {"game_even": "Answer \"yes\" if the number is even, otherwise answer \"no\".",
         "game_calc": "What is the result of the expression?"}


def game_logic(game_name: str):
    name = welcome_user()
    for _ in range(ROUNDS):
        match game_name:
            case "game_even":
                print(RULES["game_even"])
                end_flag = game_even(name, MIN_RANGE_VALUE, MAX_RANGE_VALUE)
                if not end_flag:
                    return
            case "game_calc":
                print(RULES["game_calc"])
                end_flag = game_calc(name, MIN_RANGE_VALUE, MAX_RANGE_VALUE)
                if not end_flag:
                    return
            case _:
                print("This game doesn't exist")
                return
    print(f"Congratulations, {name}!")
                
