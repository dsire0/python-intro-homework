
def int_miner(spelunking:int, cavelist:list) -> None:
    """Search through a list and return an int.

    Args:
        spelunking (int): The integer to search for.
        cavelist (list): The list to search through
    """
    cap:    int = len(cavelist)-1
    match: bool = False
    mineshaft: int = 0
    minecart: int = 0

    # Look again when name is not found
    while not match: # Will loop as long as match == false
        miner: int = spelunking # miner accepts the task

        # loop through the list up to "cap"
        while mineshaft <= cap:
            minecart = cavelist[mineshaft]

            #region Debug
            # print(f"index: {mineshaft} = {numbers[mineshaft]}")
            # print("returned: " + minecart)
            #endregion Debug

            # Test for parity
            if miner == minecart :
                match = True
                print(f"Found \"{minecart}\" at index {mineshaft}")
                return

            mineshaft += 1
            
        if not match:
            print(f"Sadly, \"{miner}\" could not be found")
            match = True # Ehhh
            return



def intput() -> int:
    """ Loops asking for input - checks if valid - returns the int if it passes.

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