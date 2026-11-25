import csv
import os

# region instruction
# Write a program that analyzes this data and writes a formatted report to a new file. Follow these steps:

# Use os.path.exists() to verify that ../data/expenses.csv exists before opening it. If it doesn't, print an error message and stop.
# Read ../data/expenses.csv into a list of dictionaries using csv.DictReader.

# Convert the amount field to float for each row.
# Filter the list to only rows where category is "Food".
# Calculate the total amount spent on Food.
# Write a report to food_report.txt with this structure:
# First line: Food Expense Report — generated [today's date as "Month DD, YYYY"]
# One line per food expense: [date]: $[amount]
# Last line: Total: $[total to 2 decimal places]
# Hint: All values from csv.DictReader come back as strings. Remember to convert amount with float() before doing any math.

# Optional: If you want extra practice, modify your program to work for any category, not just "Food". Running it for "Transport" should produce a transport_report.txt with the same format.

# Save as: mini_project.py (and include food_report.txt to show your output)
# endregion instruction

# region pathfinding
# # Use os.path.exists() to verify that ../data/expenses.csv exists before opening it.
# If it doesn't, print an error message and stop.


def generate_path() -> str:
    path: str = os.path.join(".", "week-7", "data", "expenses.csv")
    print(
        f"Generated path: {path}. \
    Passing to 'validate_path'."
    )
    return path


def validate_path(test_path: str) -> bool:
    if not os.path.exists(path=test_path):
        print(f"{test_path} not found.")
        return False
    else:
        return True


# endregion pathfinding
# region csv.dictreader
## Read ../data/expenses.csv into a list of dictionaries using csv.DictReader.
def open_file_mit_dictreader(path: str) -> list[dict[str, str | float]]:
    # Coding languages are so odd; Static statements represent active states.
    # Opens 'path' with a read only permission as an iterable 'obj'
    with open(file=path, mode="r") as libre:
        expenses_list: list[dict[str, str | float]] = list(csv.DictReader(libre))
        return expenses_list


# endregion csv.dictreader

# region processing


# 'raw_rows' to converted 'typed_rows'
# Convert the amount field to float for each row.
def convert(raw_rows: list[dict[str, str | float]]) -> list[dict[str, str | float]]:
    # so I need to access expenses_list in main() and pass the raw_rows here
    # then return the converted rows
    for row in raw_rows:
        row["amount"] = float(row["amount"])
    # unless I want to assign a new variable just to return the converted rows, I'll have to stick with raw_rows
    return raw_rows  # pass this to food_filter


# 'typed_rows' to 'filtered_rows'
# Filter the list to only rows where category is "Food".
def food_filter(category: list[dict[str, str | float]]) -> list[dict[str, str | float]]:
    # At this point, I have a whole spreadsheet with the amount column values typed as float
    # Imagine the parameter being named "category" as well.
    # Aw hell... I have to.
    filtered_food: list[dict[str, str | float]] = [
        category for category in category if category["category"] == "category"
    ]
    return filtered_food


# 'filtered_rows' process
# Calculate the total amount spent on Food.
def food_cost(filtered_food):
    pass


# Write a report to food_report.txt with this structure:
def generate_report():
    pass


# First line: Food Expense Report — generated [today's date as "Month DD, YYYY"]
# One line per food expense: [date]: $[amount]
# Last line: Total: $[total to 2 decimal places]

# endregion processing

# region main


def main():
    # 1. generate the path
    csv_path: str = generate_path()
    # 2. validate the path
    if validate_path(test_path=csv_path):
        # 3. open file with open_file_mit_dictreader and store the list[dict[str, str | float]] in memory inside main()
        raw_rows: list[dict[str, str | float]] = open_file_mit_dictreader(path=csv_path)
        # 4. convert the
        typed_rows: list[dict[str, str | float]] = convert(raw_rows=raw_rows)
        filtered_rows: list[dict[str, str | float]] = food_filter(raw_rows=typed_rows)


if __name__ == "__main__":
    main()

# endregion main
