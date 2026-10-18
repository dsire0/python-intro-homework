# Warmup 3: Boolean Expression Practice
# Write a script that evaluates the five expressions below and prints each one with its result. Add a comment on each line explaining why the result is what it is:
# print(not True and False)
# print(True or False and False)
# print(not (5 > 3))
# print(10 == 10 and 4 != 4)
# print(not False or not True)
# Example format:

# False   # not True is False; False and False is False

print(not True and False) # False - 'not True' is False; 'False and {anything}' is False since python lazily evaluates the 'and' comparison operator.
print(not (True and False)) # True - python evaluates 'True and False' completely since 'True' is the first argument. not flips the result to 'True'
print(True or False and False) # True - Order of operations: not, and, or. 'False and False' is evaluated to 'False' first, then 'True or False' is evaluated to True
print(True or (False and False)) # True - same as above except easier to read.
print(not (5 > 3)) # False - (5 > 3) evaluates to 'True', not() flipped the bool from 1 to 0
print(10 == 10 and 4 != 4) # False - '10 == 10' is 'True so python continues to evaluate 'and'; 4 != 4 is 'False' so Python evaluates 'True and 'False.
print(not False or not True) # True - '(not False) or (not True)' -> 'True or False' == 'True'