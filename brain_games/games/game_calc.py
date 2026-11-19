from random import choice, randint

import prompt

MIN_RANGE_VALUE = 1
MAX_RANGE_VALUE = 100
ROUNDS = 3
SIGN = ["+", "-", "*"]

def game_calc(name):
    
    print("What is the result of the expression?")

    for _ in range(ROUNDS):
        result = 0
        sign = choice(SIGN)
        x = randint(MIN_RANGE_VALUE, MAX_RANGE_VALUE)
        y = randint(MIN_RANGE_VALUE, MAX_RANGE_VALUE)
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
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")