# Warmup 4: Sign and Parity
# Ask the user for a number. 
# Using two separate if/elif/else blocks — one for sign, one for parity. 
# print two lines of output. 
# The examples below show the format for two different inputs — your number will differ:
# Enter a number: -7
# -7 is negative.
# -7 is odd.
# Enter a number: 0
# 0 is zero.
# 0 is even.

# Convert's user input to an int
num: int  = int(input("provide a number: "))

# Determine the Sign
if num > 0:
    print(f"{num} is positive.")
elif num < 0:
    print(f"{num} is negative.")
else:
    print(f"{num} is zero.")

# Determine the Parity
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")