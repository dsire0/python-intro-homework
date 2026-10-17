# Warmup 2: Age Categories
# Use input() to ask the user for their age. Convert it to an integer, then use if/elif/else with and to check ranges and print which category they fall into:

def dbg(input=any) -> None:
    """Prepends input with 'DEBUG: ' """
    print(f"DEBUG: {input!s}")

# : int sets the expected type for 'user_age'. 'int()' facilitates the conversion
user_age: int = int(input("How old are you?: "))
category: str = ""
# Age-range	Category
# 0-12	    Child
# 13-17	    Teen
# 18-64	    Adult
# 65 and up	Senior

if user_age >= 0 and user_age <= 12:
    category = "Child"
elif user_age >= 13 and user_age <= 17:
    category = "Teen"
elif user_age >= 18 and user_age <= 64:
    category = "Adult"
elif user_age >= 65:
    category = "Senior"
else:
    category = "Time Traveler"

print (f"You are a {category}.")

lower_category: str = category.lower()
# I dislike repeating the same debug print statement
# print(f"DEBUG: {lower_category}")

# quick debug statement repeat. Gotta learn how to make this a package that can be imported.
dbg(lower_category)

if lower_category in ("child", "teen"):
    print("Children are not allowed!")
    if lower_category == "teen":
        print("Still too young.")
elif lower_category == "adult":
    print("Enter.")
elif lower_category == "senior":
    print("Enter. Watch the step")
elif lower_category == "time traveler":
    print("Welcome fellow relevart")
    if isinstance(user_age, int) == False:
        print("How?")
else:
    print("DeadEnd")