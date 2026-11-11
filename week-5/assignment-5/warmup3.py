# Warmup 3: Linear Search
# Start with a hardcoded list of names. Ask the user to enter a name. 
# Loop through the list and print whether the name was:
# found and at what index — or a not-found message if it isn't in the list. 
# The examples below show the format for two different searches — your names, index, and message wording might differ:

# Enter a name to search for: Marcus
# Found "Marcus" at index 3.
# Enter a name to search for: Zara
# "Zara" was not found in the list.
# Do not use Python's .index() method or the in operator — implement the search yourself with a loop.
# Save as: warmup3.py

# hardcoded names in a list
names: list = ["bip","bop","boop"]
cap:    int = len(names)
match: bool = False

# Look again when name is not found
while not match: # Will loop as long as match == false
    search: str = input("Enter a name to search for: ") # a task is received
    miner: str = search.strip().lower() # miner accepts the task
    minecart: str = ""
    mineshaft: int = 0

    # loop through the list up to "cap"
    while mineshaft != cap:
        minecart = names[mineshaft]

        ## Debug
        # print(f"index: {mineshaft} = {names[mineshaft]}")
        # print("returned: " + minecart)
        ## Debug

        # Test for parity
        if miner == minecart :
            match = True
            print(f"Found \"{minecart}\" at index {mineshaft}")
            break

        mineshaft += 1
        
    if not match:
        print(f"Sadly, \"{miner}\" could not be found")