#region assignment
# Part 2: Mini-Project — Number Cruncher
# A data file is provided in week-5/data/numbers.py. Copy the numbers list from that file into your script.
# Build a menu-driven program using a while loop. Each time the menu displays, the user picks an option. The menu below shows the format — your wording and layout might differ, but all five options must be present:
# === Number Cruncher ===
# 1. Find minimum
# 2. Find maximum
# 3. Search for a number
# 4. Sort the list
# 5. Quit
# Choose an option (1-5):
# Requirements for each option:
# Find minimum — loop through the list and track the smallest value. Do not use Python's built-in min().
# Find maximum — same approach, tracking the largest value. Do not use max().
# Search — ask the user for a number, then implement a linear search loop. Print the index if found, or a "not found" message.
# Sort — implement bubble sort: repeatedly loop through adjacent pairs, swap if out of order, and repeat until no swaps occur. Print the sorted list. Do not use sorted() or .sort().
# Quit — print a goodbye message and exit the loop.
# The menu should redisplay after each operation until the user chooses Quit.

# Bubble sort hint: One pass through the list looks at pairs — numbers[i] and numbers[i+1] 
# — and swaps them if the first is larger. 
# You need to repeat this process until a full pass produces zero swaps.

# Pseudocode:

# repeat:
#     swapped = False
#     for each adjacent pair:
#         if left > right:
#             swap them
#             swapped = True
# until swapped is False
# Save as: mini_project.py
#endregion assignment
#region imports
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from importables import spelunking as sp

#endregion imports


#region functions
def router(input:int):
    if   input == 1:
        return findmin()
    elif input == 2:
        return findmax()
    elif input == 3:
        return search()
    elif input == 4:
        return bubblesort()
    elif input == 5:
        return quit()
    else:
        return True

# Working in order - findmin, findmax, search, bubblesort.
# Compare list values against eachother, assignment only occurs if trialvalue < currentvalue
def findmin()     -> bool: # 1
    currentvalue: int = numbers[0]
    trialvalue: int = 0
    for trialvalue in numbers:
        # comparison
        print(f"trialva1lue < currentvalue : {trialvalue} < {currentvalue} : {trialvalue < currentvalue}")
        currentvalue = trialvalue if trialvalue < currentvalue else currentvalue

    print(f"The minimum value is {currentvalue}")
    return True


def findmax()    -> bool: # 2
    currentvalue: int = numbers[0]
    trialvalue: int = 0
    for trialvalue in numbers:
        # comparison
        print(f"trialva1lue > currentvalue : {trialvalue} > {currentvalue} : {trialvalue > currentvalue}")
        currentvalue = trialvalue if trialvalue > currentvalue else currentvalue

    print(f"The maximum value is {currentvalue}")
    return True

def search()     -> bool: # 3
    searchterm: int = sp.intput()
    sp.int_miner(searchterm, numbers[0:])
    return True


def bubblesort() -> bool: # 4
    print(sp.bubbler(numbers))
    return True


def quit()       -> bool: # 5
    print("Goodbye")
    return False
#endregion functions

#region global variables
# List of ints
numbers: list[int] = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]
# primary loop condition
loop: bool = True
#endregion global variables

print("\n" * 5)
#region primary loop
while loop:
    # Prints again AFTER a SUCCESSFUL operation
    # print("════════════ primary loop in  ════════════")
    print("\n" \
    "═════ Number Cruncher ═════\n" \
    "1. Find min\n" \
    "2. Find max\n" \
    "3. Search for number\n" \
    "4. Sort the list\n" \
    "5. Quit\n")

    # Repeats the question if choice is not valid
    choice = 0

    #region second loop
    # print("══════ second loop in  ══════")
    # once loop exits, choice will have been validated and allow the next step of code to run
    while choice not in range(1,6):
        try:
            choice = int(input("Choose an option (1-5): ").strip())
        except TypeError:
            print(f"\nSelection: {choice} is not valid.\n")
        # else: 
            # print(f"\nProceeding with selection {choice}.\n")

    # Decides if the loop will continue
    loop = router(choice) # Returns bool

    #endregion second loop
    # print("══════ second loop out ══════")

    #endregion primary loop
    # print("════════════ primary loop out ════════════" + "\n" * 20)
    
