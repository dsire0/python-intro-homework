# Warmup 1: Sum with a For Loop
# Use a for loop with range() to calculate the sum of all integers from 1 to 100. Print the result.
# Example output — your message wording might differ:

# The sum of 1 to 100 is 5050.
# Save as: warmup1.py

adder: int = 0
for count in range(1,101):  
    # print(count) # Used to verify count worked as intended
    adder += count
    if count == 100:
        print(f"The sum of 1 to 100 is {adder}")
        break