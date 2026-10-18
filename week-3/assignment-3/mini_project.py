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

d1, d2, d3 = "monday", "tuesday", "wednesday"
t1, t2, t3 = "pre-dawn", "dawn", "morning"

d= day = input("What day is it? monday, tuesday, wednesday: ").lower() # monday, tuesday, wednesday
if d not in [d1, d2, d3]:
    print("Invalid input, try monday, tuesday, or wednesday")

t= time = input("What time of day? pre-dawn, dawn, morning: ").lower() # pre-dawn, dawn, morning
if t not in [t1, t2, t3]:
    print("Invalid input, try pre-dawn, dawn, or morning")


if d == d1 and t == t1:
    print("Suggestion: Pre-dawn rituals are the best, try making a new one!")
elif d == d2 and t == t1:
    print("Suggestion: Take some time to yourself, you deserve it.")
elif d == d3 and t == t1:
    print("Suggestion: Try getting up at 3:00 AM.")
elif d == d1 and t == t2:
    print("Suggestion: Dawn has arrived! keep working hard!")
elif d == d2 and t == t2:
    print("Suggestion: Why not. Take a little extra time to yourself.")
elif d == d3 and t == t2:
    print("Suggestion: Yesterday is yesterday; don't worry and be happy!")
elif d == d1 and t == t3:
    print("Suggestion: Hell yeah, perfect time to catch a nap")
elif d == d2 and t == t3:
    print("Suggestion: Keep your code simple")
elif d == d3 and t == t3:
    print("Suggestion: Try a new way to handle an old problem")
else:
    print("And how did we get here?")