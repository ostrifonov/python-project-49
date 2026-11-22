import prompt


def welcome_user() -> str:
    name = prompt.string("""Welcome to the Brain Games!
May I have your name? """)
    print(f"Hello, {name}!")

    return name
