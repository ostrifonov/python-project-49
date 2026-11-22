import prompt

from random import randint

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
        print(f"""'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.
Let's try again, {name}!""")
        return False