# Warmup 4: FizzBuzz
# Loop from 1 to 30 and print one word per line:

# "FizzBuzz" if the number is divisible by both 3 and 5
# "Fizz" if divisible by 3 only
# "Buzz" if divisible by 5 only
# The number itself otherwise
# Check the combined case first.

# Save as: warmup4.py

for count in range(1,31):
    ## Debug
    #print(f"count at {count}: {count % 3}:{count % 5}")
    ## Debug

    if not count % 3  and not count % 5:
        print("FizzBuzz")
    
    elif not count % 3:
        print("Fizz")
        
    elif not count % 5:
        print("Buzz")

    else:
        print(count)