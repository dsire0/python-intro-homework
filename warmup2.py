# scratchpad


pad: dict[str, str] = {"scritch" : "light", "scratch" : "normal", "scrunch" : "heavy"}

# scenario: extract -- variable pad: dict is known.
# how to see just the keys, just the values, and both key value side by side?

# well... what is built in to a dict?
print(pad.items()) # cover both key and value but is hard to read
print(pad.copy()) # shallow copy?
print(pad.get("scritch")) # ahh but I need to know the keys first
print(pad.keys()) # like .items but only for keys
print(pad.pop("scritch"), "has been removed from the dictionary") # Odd explanation. It's like a destructive scan. returns a string
print(pad.fromkeys([6,7,8], [1,2,3])) # The tooltip is killer. First argument is the iterable, second argument is the value each key will receive.
print(pad.values()) # like .items but only for values -- 'normal', 'heavy' expected
print(pad.popitem()) # like .pop but returns a tuple
print(".setdefault returns the value only: ", pad.setdefault("odd-name", "for-method")) # tooltip provides little info. Is like .get but will also insert kv pairs if 'key' is not found; outputs value.
print(".update returns: ", pad.update({"scratch":"that-itch"})) # tooltip is hard to read. Update sounds like replacing a value, and it does, however it also OVERWRITES key value pairs. returns none
print(pad.clear()) # clears the dict
print(pad) # empty dict, as expected
original: dict[str, str | list[str]] = {"animal": "cat", "toys": ["ball"]}
print(original)
copied: dict[str, str | list[str]] = original.copy()
print(copied)

# oy vey!
# /scratchpad