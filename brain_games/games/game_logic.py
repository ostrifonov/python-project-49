from brain_games.cli import welcome_user
from brain_games.games.game_calc import game_calc
from brain_games.games.game_even import game_even
from brain_games.games.game_gcd import game_gcd
from brain_games.games.game_progression import game_progression


MIN_RANGE_VALUE = 1
MAX_RANGE_VALUE = 100
ROUNDS = 3
GAME_RULES = {"game_even": "Answer \"yes\" if the number is even, otherwise answer \"no\".",
         "game_calc": "What is the result of the expression?",
         "game_gcd": "Find the greatest common divisor of given numbers",
         "game_progression": "What number is missing in the progression?"}


def game_logic(game_name: str):
    name = welcome_user()
    
    for _ in range(ROUNDS):
        match game_name:
            
            case "game_even":
                print(GAME_RULES["game_even"])
                end_flag = game_even(name, MIN_RANGE_VALUE, MAX_RANGE_VALUE)
                if not end_flag:
                    return
            
            case "game_calc":
                print(GAME_RULES["game_calc"])
                end_flag = game_calc(name, MIN_RANGE_VALUE, MAX_RANGE_VALUE)
                if not end_flag:
                    return
            
            case "game_gcd":
                print(GAME_RULES["game_gcd"])
                end_flag = game_gcd(name, MIN_RANGE_VALUE, MAX_RANGE_VALUE)
                if not end_flag:
                    return

            case "game_progression":
                print(GAME_RULES["game_progression"])
                end_flag = game_progression(name, MIN_RANGE_VALUE, MAX_RANGE_VALUE)
                if not end_flag:
                    return
            
            case _:
                print("This game doesn't exist")
                return
    
    print(f"Congratulations, {name}!")