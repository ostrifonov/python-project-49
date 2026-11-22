def calculate_gcd(a: int, b: int) -> int | None:
    if a == 0 and b == 0:
        return None
      
    a, b = abs(a), abs(b)
      
    while b != 0:
        a, b = b, a % b
      
    return a