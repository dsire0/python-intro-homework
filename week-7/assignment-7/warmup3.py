import os

# region 1
print(os.getcwd())
# endregion 1

# region 2
path: str = "./week-7/data/expenses.csv"
if os.path.exists(path):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")

# endregion 2

# region 3
path = os.path.join(".", "week-7", "data", "expenses.csv")
print(path)
if os.path.exists(path):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")
# endregion 3
