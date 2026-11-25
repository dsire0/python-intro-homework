import csv
import os
from datetime import datetime

# I went a little overboard I think
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


# dirty
def generate_path(filename: str) -> str:
    path: str = os.path.join(".", "week-7", "data", filename)
    print(f"Generated path: {path}.")
    return path


def generate_relative_path(filename: str) -> str:
    path: str = os.path.join(".", "week-7", "assignment-7", filename)
    print(f"Generated path: {path}.")
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
    with open(file=path, mode="r", newline="", encoding="utf-8") as libre:
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
def food_filter(
    typed_rows: list[dict[str, str | float]], target_category: str = "Food"
) -> list[dict[str, str | float]]:
    # typed_rows is looped through, assigning the dict obj to row
    # from row lookup key "category" and pull value into memory then compare against target_category.
    # row: dict[str, str | float] - row being a dictionary.
    return [row for row in typed_rows if str(row["category"]) == target_category]


# def brack(
#     typed_rows: list[dict[str, str | float]], target_category: str = "Food"
# ) -> list[dict[str, str | float]]:
#     row: dict[str, str | float] = {}
#     filtered_rows: list[dict[str, str | float]] = []
#     for row in typed_rows:
#         if str(row["category"]) == target_category:
#             filtered_rows.append(row)
#     return filtered_rows


# 'filtered_rows' process
# Calculate the total amount spent on Food.
def food_cost(filtered_food: list[dict[str, str | float]]) -> float:
    return sum((float(food["amount"]) for food in filtered_food), start=0.0)


# Write a report to food_report.txt with this structure:
# First line: Food Expense Report — generated [today's date as "Month DD, YYYY"]
# One line per food expense: [date]: $[amount]
# Last line: Total: $[total to 2 decimal places]
def generate_report(
    rows: list[dict[str, str | float]],
    total: float,
    target_category: str = "Food",
) -> None:
    # Today's date formatted.
    today_str: str = datetime.now().strftime(format="%B %d, %Y")  # noqa - stop being annoying
    report_name: str = f"{target_category.lower()}_report.txt"
    file_path: str = generate_relative_path(filename=report_name)

    with open(file=file_path, mode="w", encoding="utf-8") as file:
        # Using '_ =' since '.write' returns an int based on character amount (I think character amount)
        _ = file.write(f"{target_category} Expense Report — generated {today_str}\n")
        for row in rows:
            _ = file.write(f"{row['date']}: ${(row['amount']):.2f}\n")
        _ = file.write(f"Total: ${total:.2f}\n")

    # print(f"Food Expense Report - generated {today.strftime(format='%B %d, %Y')}.")


# endregion processing

# region main


def main() -> None:
    # 1. generate the path
    csv_path: str = generate_path(filename="expenses.csv")
    target_category: str = "Food"
    # 2. validate the path
    if validate_path(test_path=csv_path):
        # 3. open file with open_file_mit_dictreader and store the list[dict[str, str | float]] in memory inside main()
        raw_rows: list[dict[str, str | float]] = open_file_mit_dictreader(path=csv_path)
        # 4. convert the str to float
        typed_rows: list[dict[str, str | float]] = convert(raw_rows=raw_rows)
        # 5. filter the categories
        filtered_rows: list[dict[str, str | float]] = food_filter(
            typed_rows=typed_rows, target_category=target_category
        )
        # 6. get total cost
        cost_from_rows: float = food_cost(filtered_food=filtered_rows)
        # 7. write the report
        generate_report(
            rows=filtered_rows, total=cost_from_rows, target_category=target_category
        )
        # brack: list[dict[str, str | float]] = brack(typed_rows=typed_rows)


if __name__ == "__main__":
    main()

# endregion main
