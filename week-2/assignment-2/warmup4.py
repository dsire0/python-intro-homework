# <1>
# Traceback (most recent call last):
#   File "d:\WinDev\WinGitRepos\python-intro-homework\week-2\assignment-2\warmup4.py", line 1, in <module>
#     print(f"I found the {lost}!")
#                          ^^^^
# NameError: name 'lost' is not defined. Did you mean: 'list'?

# <3>
# added variable 'lost' to resolve NameError.
lost = "Yacht"

# <2>
# 'lost' was not defined
print(f"I found the {lost}!")