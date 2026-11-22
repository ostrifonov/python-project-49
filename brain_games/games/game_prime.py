from random import randint

import prompt

from brain_games.games.is_prime import is_prime


def game_prime(name: str, min_range_value: int, max_range_value: int):

    number = randint(min_range_value, max_range_value)
    print(f"Question: {number}")
    answer = prompt.string("Your answer: ")
    correct_answer = "yes" if is_prime(number) else "no"

    if answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. " 
              f"Correct answer was '{correct_answer}'."
              )
        print(f"Let's try again, {name}!")
        return False