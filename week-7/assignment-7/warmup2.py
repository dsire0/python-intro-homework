import csv
from typing import Any

example_csv: str = "./week-7/assignment-7/readmewriteme.csv"


# region Reader vs DictReader
def open_csv_by_index_example() -> None:
    with open(example_csv, "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip the header row
        for row in reader:
            print(row[0], row[2])  # product name and price — by index


def open_csv_by_dictreader_example() -> None:
    with open(example_csv, "r") as file:
        reader: csv.DictReader[str] = csv.DictReader(file)
        for row in reader:
            print(row["product"], row["price"])  # access by name


# endregion Reader vs DictReader


# region Rows into List
def open_csv_rows_to_list_example() -> None:
    records: list[dict[str, str]] = []
    with open(example_csv, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            records.append(row)
            print(row)


def open_csv_rows_to_list_by_list_example() -> None:
    records: list[dict[str | Any, str | Any]] = []
    with open(example_csv, "r") as file:
        records = list(csv.DictReader(file))
    print(records[0:])
    for item in records:
        print(f"    {item['product']}: ${item['price']}")


# endregion Rows into List


# region Mini Pipeline
def mini_pipeline() -> None:
    # Load all rows into memory
    with open(example_csv, "r") as file:
        records: list[dict[str | Any, str | Any]] = list(csv.DictReader(file))

    # Convert numeric fields
    for item in records:
        item["price"] = float(item["price"])
        item["quantity"] = int(item["quantity"])

    # Filter to one category
    office_items: list[dict[str | Any, str | Any]] = [
        item for item in records if item["category"] == "Office"
    ]

    # Compute total inventory value
    total_value: float = sum(
        float(item["price"]) * int(item["quantity"]) for item in office_items
    )
    print(f"Office inventory value: ${total_value:.2f}")


# endregion Mini Pipeline


# region warmup2
def read_a_csv_with_dictreader() -> None:
    with open("./week-7/data/students.csv", "r") as file:
        reader: csv.DictReader[str] = csv.DictReader(file)
        for row in reader:
            print(f"{row['name']}: {row['score']}")


# endregion warmup2
# region main


def main() -> None:
    # print("\nopen_csv_by_index_example")
    # open_csv_by_index_example()
    # print("\nopen_csv_by_dictreader_example")
    # open_csv_by_dictreader_example()
    # print("\nopen_csv_rows_to_list_example")
    # open_csv_rows_to_list_example()
    # print("\nopen_csv_rows_to_list_by_list_example")
    # open_csv_rows_to_list_by_list_example()
    print("\nread_a_csv_with_dictreader")
    read_a_csv_with_dictreader()


if __name__ == "__main__":
    main()
# endregion main
