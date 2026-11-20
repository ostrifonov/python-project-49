from random import randint

import prompt

from brain_games.games.is_even import is_even


def game_even(name: str, min_range_value: int, max_range_value: int):
    number = randint(min_range_value, max_range_value)
    correct_answer = "yes" if is_even(number) else "no"
    print(f"Question: {number}")
    answer = prompt.string("Your answer: ")
    if answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"""'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.
Let's try again, {name}!""")
        return False