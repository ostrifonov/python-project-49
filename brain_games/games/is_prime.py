from math import sqrt


def is_prime(a: int) -> bool:

    if a < 2:
        return None

    is_prime = True

    for num in range(2, int(sqrt(a)) + 1):
        if a % num == 0:
            is_prime = False

    return is_prime
