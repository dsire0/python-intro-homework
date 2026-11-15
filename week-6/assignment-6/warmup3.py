# Warmup 3: Scope in Action
# Demonstrate variable scope with two short examples in one file:

# Define a variable inside a function. Try to access it outside the function and show the NameError — paste the error in a comment, then remove or comment out the line that causes it.
# Show how return solves the problem: return the value from the function and assign it to a variable in the outer scope. Print it to confirm it worked.
# Save as: warmup3.py


def lost() -> None:
    animal: str = "dog"
    # Warning: Local variable `animal` is assigned to but never used <- builtin
    # Hint: "animal" is not accessed <- pylance
    # print(f"I found an {animal}")


# print(f"I found an {animal}")
# Error: "animal" is not defined <- builtin
# Error: Undefined name `animal` <- ruff


def returned() -> str:
    animal: str = "bug"
    print(f"I found a {animal} ")
    return animal


if __name__ == "__main__":
    creature: str = returned()
    print(f"Finally... I see the {creature}")
