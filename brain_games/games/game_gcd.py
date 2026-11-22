from random import randint

import prompt

from brain_games.games.calculate_gcd import calculate_gcd

def game_gcd(name: str, min_range_value: int, max_range_value: int):
    
    a = randint(min_range_value, max_range_value)
    b = randint(min_range_value, max_range_value)
    result = calculate_gcd(a, b)
    
    print(f"Question: {a} {b}")
    answer = prompt.integer("Your answer: ")
    
    if answer == result:
        print("Correct!")
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'")
        print(f"Let's try again, {name}!")
        return False

