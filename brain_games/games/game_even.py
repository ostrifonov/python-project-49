from random import randint

import prompt

from brain_games.is_even import is_even

MIN_RANGE_VALUE = 1
MAX_RANGE_VALUE = 100
ROUNDS = 3


def game_even(name):

    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(ROUNDS):
        number = randint(MIN_RANGE_VALUE, MAX_RANGE_VALUE)
        correct_answer = "yes" if is_even(number) else "no"
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")
        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"""'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.
Let's try again, {name}!""")
            return
    print(f"Congratulations, {name}!")