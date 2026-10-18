# Part 2: Mini-Project — Day Planner
# Write a program that asks the user for a day of the week and a time of day (morning, afternoon, or evening), then suggests an activity.
# Requirements:
# Cover at least 3 days × 3 times = 9 combinations with distinct suggestions
# Handle any unrecognized day or time with a friendly fallback message
# Normalize input so capitalization doesn't matter (e.g., "Monday" and "monday" both work)
# Example output (the suggestion and fallback wording are your own — any sensible messages are fine):

# What day is it? Tuesday
# What time of day? morning
# Suggestion: Morning Python class — great time to focus!
# What day is it? Saturday
# What time of day? evening
# Suggestion: Perfect night for a movie or trying a new recipe.
# What day is it? blah
# What time of day? morning
# Sorry, I don't recognize that day. Try: Monday, Tuesday, Wednesday...

d= day = input("What day is it?: ").lower() # monday, tuesday, wednesday
t= time = input("What time of day?: ").lower() # pre-dawn, dawn, morning

d1, d2, d3 = "monday", "tuesday", "wednesday"
t1, t2, t3 = "pre-dawn", "dawn", "morning"


if d == d1 and t == t1:
    print()
elif d == d2 and t == t1:
    print()
elif d == d3 and t == t1:
    print()
elif d == d1 and t == t2:
    print()
elif d == d2 and t == t2:
    print()
elif d == d3 and t == t2:
    print()
elif d == d1 and t == t3:
    print()
elif d == d2 and t == t3:
    print()
elif d == d3 and t == t3:
    print()
else:
    print()