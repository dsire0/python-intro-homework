# scratchpad

pad: dict[str, str] = {"scritch" : "light", "scratch" : "normal", "scrunch" : "heavy"}

# scenario: extract -- variable pad: dict is known.
# how to see just the keys, just the values, and both key value side by side?

# well... what is built in to a dict?
print(".items returns         :", pad.items()) # cover both key and value but is hard to read
print(".items-list returns    :", list(pad.items())) # using list returns the values as a list instead of being classed as a 'dict_items()' 
print(".copy returns          :", pad.copy()) # shallow copy?
print(".get returns           :", pad.get("scritch")) # ahh but I need to know the keys first
print(".keys returns          :", pad.keys()) # like .items but only for keys
print(".keys-list returns     :", list(pad.keys())) # using list returns the values as a list instead of being classed as a 'dict_keys()' 
print(".pop returns           :", pad.pop("scritch"), "has been removed from the dictionary") # Odd explanation. It's like a destructive scan. returns a string
print(".fromkeys returns      :", pad.fromkeys([6,7,8], [1,2,3])) # The tooltip is killer. First argument is the iterable, second argument is the value each key will receive.
print(".values returns        :", pad.values()) # like .items but only for values -- 'normal', 'heavy' expected
print(".values-list returns   :", list(pad.values())) # using list returns the values as a list instead of being classed as a 'dict_values()' 
print(".popitem returns       :", pad.popitem()) # like .pop but returns a tuple
print(".setdefault returns    :", pad.setdefault("odd-name", "for-method")) # tooltip provides little info. Is like .get but will also insert kv pairs if 'key' is not found; outputs value.
print(".update returns        :", pad.update({"scratch":"that-itch"})) # tooltip is hard to read. Update sounds like replacing a value, and it does, however it also OVERWRITES key value pairs. returns none
print("  after                 :", list(pad.items()))
print(".clear returns         :", pad.clear()) # clears the dict
print(" after clearing pad    :", pad) # empty dict, as expected
original: dict[str, str | list[str]] = {"animal": "cat", "toys": ["ball"]}
print(original)
copied: dict[str, str | list[str]] = original.copy()
print(copied)
# The real question is: How do you work with the nested list?

# oy vey!
# /scratchpad

student: dict = {
    "name" : "Named",
    "grade": "Hard-boiled",
    "score": "More Dakka"
}


def printer() -> None:
    print("")
    """I didn't want to type this out twice."""
    for key, value in student.items():
        print(f"{key}: {value}")


printer()
student.setdefault("graduated", False)
printer()


