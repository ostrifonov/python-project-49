import prompt

from random import randint

from brain_games.games.make_progression import make_progression

def game_progression(name: str, min_range_value: int, max_range_value: int):
    
    progression = make_progression(min_range_value, max_range_value)
    
    invisible_num_index = randint(1, len(progression)-1)
    invisible_number = int(progression[invisible_num_index])
    progression[invisible_num_index] = ".."
        
    print(f"Question: {" ".join(progression)}")

    answer = prompt.integer("Your answer: ")
        
    if answer == invisible_number:
        print("Correct!")
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{invisible_number}'")
        print(f"Let's try again, {name}!")
        return False