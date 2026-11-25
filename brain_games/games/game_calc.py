from random import choice, randint

import prompt

SIGN = ["+", "-", "*"]
RULE = "What is the result of the expression?"


def game_calc(name: str, min_range_value: int, max_range_value: int):

    result = 0
    sign = choice(SIGN)
    x = randint(min_range_value, max_range_value)
    y = randint(min_range_value, max_range_value)
    print(f"Question: {x} {sign} {y}")
    match sign:
        case "+":
            result = x + y
        case "-":
            result = x - y
        case "*":
            result = x * y
    answer = prompt.integer("Your answer: ")
    if answer == result:
        print("Correct!")
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'")
        print(f"Let's try again, {name}!")
        return False
