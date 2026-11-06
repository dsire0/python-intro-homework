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

# Bubble sort hint: One pass through the list looks at pairs — numbers[i] and numbers[i+1] — and swaps them if the first is larger. You need to repeat this process until a full pass produces zero swaps.
# Pseudocode:

# repeat:
#     swapped = False
#     for each adjacent pair:
#         if left > right:
#             swap them
#             swapped = True
# until swapped is False
# Save as: mini_project.py

loop: bool = True
print("\n" * 20)
# primary loop in
while loop:
    # Prints again AFTER a SUCCESSFUL operation
    print("════════════ primary loop in  ════════════")
    print("\n" \
    "═════ Number Cruncher ═════\n" \
    "1. Find min\n" \
    "2. Find max\n" \
    "3. Search for number\n" \
    "4. Sort the list\n" \
    "5. Quit\n")

    # Repeats the question if choice is not valid
    choice = 0
    # second loop in
    print("══════ second loop in  ══════")
    while choice not in range(1,6):
        choice = int(input("Choose an option (1-5): ").strip())
        if choice not in range(1,6):
            print(f"\nSelection: {choice} is not valid.\n")
        else: 
            print(f"\nProceeding with selection {choice}.\n")
    print("══════ second loop out ══════")

    # primary loop out
    print("════════════ primary loop out ════════════" + "\n" * 20)
    
