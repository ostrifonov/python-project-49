from random import randint


def make_progression(min_range_value: int, max_range_value: int) -> list[str]:
    
    index_range = randint(5, 10)
    start_number = randint(min_range_value, max_range_value)
    step = randint(2, 9)

    progression = [str(start_number + index * step) 
                   for index in range(0, index_range)
                   ]

    return progression