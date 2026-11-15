# Warmup 4: Validation Function
# Write a function is_valid_score(score) that returns True if score is an integer between 0 and 100 (inclusive), and False otherwise.
# Then use input() to ask the user for a score and convert it to an integer with int() before you check it.
# Call your function inside an if statement and print either "Valid score." or "Invalid score — must be between 0 and 100.".
# Save as: warmup4.py


def is_valid_int(ghosttext: str = "Enter an integer: ") -> int:
    """_summary_ Loops asking for input - checks if valid - returns the int if it passes.
        Two steps condensed into one try:except block
    Args:
        ghosttext (str, optional): Allows the greeting to be customized. Defaults to "Enter an integer".

    Returns:
        int: a valid int unmodified
    """
    while True:
        intput: str = input(f"{ghosttext}")
        try:
            num = int(intput)
            return num
        except ValueError:
            print(f"{intput} is not an integer. Try again.")


def is_valid_score(score: int = 0):
    return score in range(101)


if __name__ == "__main__":
    score: int = is_valid_int("What's your score?")
    if is_valid_score(score):
        print("Valid Score")
    else:
        print("Invalid score — must be between 0 and 100.")
