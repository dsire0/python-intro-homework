def int_miner(cavelist: list, spelunking: int, printit: bool = True) -> None | int:
    """Search through a list and return an int.

    Args:
        cavelist (list): The list to search through
        spelunking (int): The integer to search for.
    """
    cap: int = len(cavelist) - 1
    match: bool = False
    mineshaft: int = 0
    minecart: int = 0

    # Look again when number is not found
    while not match:  # Will loop as long as match == false
        miner: int = spelunking  # miner accepts the task

        # loop through the list up to "cap"
        while mineshaft <= cap:
            minecart = cavelist[mineshaft]

            # region Debug
            # print(f"index: {mineshaft} = {numbers[mineshaft]}")
            # print("returned: " + minecart)
            # endregion Debug

            # Test for parity
            if miner == minecart and printit:
                match = True
                print(f'Found "{minecart}" at index {mineshaft}')
                return
            elif miner == minecart and not printit:
                match = True
                return mineshaft

            mineshaft += 1

        if not match and printit:
            print(f'Sadly, "{miner}" could not be found')
            match = True  # Ehhh
            return
        elif not match and not printit:
            return -1


def searchit(
    numbers: list[int], target: int | None = None, printit: bool = True
) -> None | int:
    searchterm: int = intput() if target is None else target
    searchresult: None | int = int_miner(numbers[0:], searchterm, printit)
    return searchresult


def intput() -> int:
    """Loops asking for input - checks if valid - returns the int if it passes.

    Two steps condensed into one try:except block

    Returns:
        int: a valid int unmodified
    """
    while True:
        intput: str = input("Enter an integer: ")
        try:
            num = int(intput)
            return num
        except ValueError:
            print(f"{intput} is not an integer. Try again.")


def is_valid_int(ghosttext: str = "Enter an integer: ") -> int:
    """Variant of intput: Loops asking for input - checks if valid - returns the int if it passes.

        Two steps condensed into one try:except block with optional customized greeting.
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


# Integers only
def bubbler(bubbles: list[int]) -> list[int]:
    swapplepop: bool = True
    while swapplepop:
        swapplepop: bool = False
        for i in range(len(bubbles) - 1):
            left: int = bubbles[i]
            right: int = bubbles[i + 1]
            if left > right:
                bubbles[i] = right
                bubbles[i + 1] = left
                swapplepop = True
    return bubbles


# Compare list values against eachother, assignment only occurs if trialvalue < currentvalue
def findmin(numbers: list[int]) -> bool:
    """_summary_

    Args:
        numbers (list[int]): _description_

    Returns:
        bool: _description_
    """
    currentvalue: int = numbers[0]
    trialvalue: int = 0
    for trialvalue in numbers:
        # comparison
        print(
            f"trialva1lue < currentvalue : {trialvalue} < {currentvalue} : {trialvalue < currentvalue}"
        )
        currentvalue = trialvalue if trialvalue < currentvalue else currentvalue

    print(f"The minimum value is {currentvalue}")
    return True


def findmax(numbers: list[int]) -> bool:
    currentvalue: int = numbers[0]
    trialvalue: int = 0
    for trialvalue in numbers:
        # comparison
        print(
            f"trialva1lue > currentvalue : {trialvalue} > {currentvalue} : {trialvalue > currentvalue}"
        )
        currentvalue = trialvalue if trialvalue > currentvalue else currentvalue

    print(f"The maximum value is {currentvalue}")
    return True


def returnmin(numbers: list[int]) -> int:
    currentvalue: int = numbers[0]
    trialvalue: int = 0
    for trialvalue in numbers:
        # comparison
        # print(
        #     f"trialva1lue < currentvalue : {trialvalue} < {currentvalue} : {trialvalue < currentvalue}"
        # )
        currentvalue = trialvalue if trialvalue < currentvalue else currentvalue

    # print(f"The minimum value is {currentvalue}")
    return currentvalue


def returnmax(numbers: list[int]) -> int:
    currentvalue: int = numbers[0]
    trialvalue: int = 0
    for trialvalue in numbers:
        # comparison
        # print(
        #     f"trialva1lue > currentvalue : {trialvalue} > {currentvalue} : {trialvalue > currentvalue}"
        # )
        currentvalue = trialvalue if trialvalue > currentvalue else currentvalue

    # print(f"The maximum value is {currentvalue}")
    return currentvalue
