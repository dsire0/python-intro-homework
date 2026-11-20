from importables.spelunking import *

# Part 2: Mini-Project — Refactor the Number Cruncher
# Open your mini_project.py from Assignment 5. You're going to refactor it so that each operation lives in its own function.

# Create a new file (don't modify your Week 5 submission). Pull a copy of the numbers list from week-5/data/numbers.py into your new script.

# Define the following functions, each taking numbers (a list) as a parameter:

# find_min(numbers) — returns the minimum value (your loop-based implementation, no min())
# find_max(numbers) — returns the maximum value (your loop-based implementation, no max())
# search(numbers, target) — returns the index of target, or -1 if not found
# bubble_sort(numbers) — returns a new sorted list (do not modify the original)
# show_menu() — prints the menu options and returns the user's choice as a string
# main() — the while loop that calls show_menu() and dispatches to the right function
# Call main() at the bottom of the file.

# Requirements:

# No logic should live outside of a function (except the numbers list definition and the main() call)
# bubble_sort should return a new list, not sort in place
# Your search function should print "Found at index X" or "Not found" from inside main(), not inside search() itself — search just returns the index
# Save as: mini_project.py

# Why revisit Week 5? This is exactly how real software gets built — you write something that works, then return to make it cleaner and easier to change. Your git history now shows both versions, which is version control doing its job.


# region functions


def find_max(numbers: list[int]) -> int:
    """
    Wrapped returnmax()

    Args:
        numbers (list[int]): _A list of numbers_

    Returns:
        int: The highest value int from numbers.
    """

    return returnmax(numbers)


def find_min(numbers: list[int]) -> int:
    """Wrapped returnmin()

    Args:
        numbers (list[int]): _A list of numbers_

    Returns:
        int: The lowest value int from numbers.
    """
    return returnmin(numbers)


def search(
    numbers: list[int], target: int | None = None, printit: bool = False
) -> None | int:
    """Wrapped searchit()

    Args:
        numbers (list[int]): _description_
        target (int | None, optional): _description_. Defaults to None.

    Returns:
        None | int: Prints the result from searchit | returns the index or -1 if not found
    """
    return searchit(numbers, target, False)


def bubble_sort(numbers: list[int]) -> list[int]:
    """
    _Wrapped bubbler function passed a copy of the original numbers list_

    Args:
        numbers (list[int]): _A list of numbers_

    Returns:
        list[int]: _Returns the copy of numbers as a sorted list_
    """
    return bubbler(numbers.copy())


def router(input: int | str) -> bool:
    if input == 1:
        max: int = find_max(numbers)
        print(f"The maximum value is: {max}")
        return True
    elif input == 2:
        min: int = find_min(numbers)
        print(f"The minimum value is: {min}")
        return True
    elif input == 3:
        searchresult: None | int = search(numbers)
        if searchresult == -1:
            print("Not found")
        else:
            print(f"Found at index {searchresult}")
        return True
    elif input == 4:
        sortresult: list[int] = bubble_sort(numbers)
        print(f"{sortresult[0:]}")
        return True
    return input != 5


def show_menu() -> str:
    # Prints again AFTER a SUCCESSFUL operation
    # print("════════════ primary loop in  ════════════")
    print(
        "\n"
        "═════ Number Cruncher ═════\n"
        "1. Find max\n"
        "2. Find min\n"
        "3. Search for number\n"
        "4. Sort the list\n"
        "5. Quit\n"
    )
    # Repeats the question if choice is not valid
    choice: str | int = 0
    # print("══════ second loop in  ══════")
    # once loop exits, choice will have been validated and allow the next step of code to run
    while choice not in range(1, 6):
        try:
            choice = int(input("Choose an option (1-5): ").strip())
        except ValueError:
            print(f"\nSelection: {choice} is not valid.\n")
    return str(choice)


def main():
    loop: bool = True
    while loop:
        choice: str = show_menu()
        loop = router(int(choice))  # Returns bool


# endregion functions

numbers: list[int] = [
    42,
    17,
    83,
    5,
    61,
    29,
    74,
    8,
    55,
    93,
    31,
    66,
    14,
    47,
    78,
    3,
    59,
    22,
    86,
    40,
]

main()
