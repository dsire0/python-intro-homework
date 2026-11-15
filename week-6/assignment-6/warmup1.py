# Warmup 1: Default Parameters
# Write a function greet(name, greeting="Hello") that prints a greeting. Call it three different ways:
# With only a name argument
# With both a name and a custom greeting
# With the greeting passed as a keyword argument
# Example output — your name and custom greeting might differ:

# Hello, Alex!
# Good morning, Alex!
# Hello, Alex!
# Save as: warmup1.py


def greet(name: str, greeting: str = "Hello"):
    print(f"{greeting}, {name}!")


greet("Dave")
greet("Dave", "Good morning")
greet("Dave", greeting="I'm afraid i can't do that")
