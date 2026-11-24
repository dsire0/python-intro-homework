import csv

# Open a file - using `with` to auto close the file upon completion or error


example: str = "./week-7/assignment-7/readmewriteme.txt"
example_csv: str = "./week-7/assignment-7/readmewriteme.csv"


def open_read_example() -> None:
    with open(example, "r") as file:
        content: str = file.read()
        print(content + " : open_read_example")


def open_read_by_line_example() -> None:
    with open(example, "r") as file:
        for line in file:
            print(
                line.strip() + " : open_read_by_line_example"
            )  # .strip() removes the newline character at the end


def open_readlines_example() -> None:
    with open(example, "r") as file:
        lines: list[str] = file.readlines()  # Returns a list — one string per line
        print(
            lines[0] + " : open_readlines_example"
        )  # First line - Without .strip() the newline character causes the added str to print below lines[0] & lines[1] but not lines[2] since that is the last line in the file


def open_error_example() -> None:
    try:
        with open("example.txt", "r") as file:
            content: str = file.read()
            print(content)
    except FileNotFoundError as e:
        print(f"An error occurred: {e}")
    else:
        print("File read successfully.")


def open_write_example() -> None:  # overwrites
    with open(example, "w") as file:
        file.write("hello")
        print(
            f" The content: 'hello' was written to {example}, replacing all contents : write_example"
        )
    with open(example, "+r") as file:
        content: str = file.read()
        print(content + " : write_example")


def overwrite(content: str) -> None:
    with open(example, "w+") as file:
        content = content.strip()
        file.write(content)
        newcontent: str = file.read().strip()
        print(
            f" The content: '{content}' was written to {example}, replacing all contents : overwrite"
        )
    with open(example, "r") as file:
        newcontent: str = file.read()
        print(newcontent + " : overwrite")


def open_csv_read_example() -> None:
    with open(example_csv, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"{row} : open_csv_read_example")  # Each row is a list of strings


def open_csv_write_example() -> None:
    """for each method .writerow being called, it is a literal row on a spreadsheet starting from A1 (If thinking from a view based on excel or sheets)"""
    with (
        open(example_csv, "w", newline="") as file
    ):  # The newline='' argument prevents extra blank lines from appearing on Windows.
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "City"])  # Header row
        writer.writerow(["Jazmine", 30, "New York"])  # Data row
        writer.writerow(["Luis", 35, "Chicago"])
        print(
            f"CSV rows were written to {example_csv}, replacing all contents : open_csv_write_example"
        )
    # with open(example_csv, "r") as file:
    # content: str = file.read().strip()
    # print(f"{content} : open_csv_write_example")


def open_csv_dictreader_example() -> None:
    with open(example_csv, "r") as file:
        reader: csv.DictReader[str] = csv.DictReader(file)
        for row in reader:
            print(f"{row['Name']} {row['Age']} : open_csv_dictreader_example")


def open_csv_dictwriter_example() -> (
    None
):  # Probably not a good idea to mixup types I think. Just looking at the typehints makes me cringe
    rows: list[
        dict[str, str | int]
        | dict[str, str | float | bool]
        | dict[str, int | bool | str]
    ] = [
        {"Name": "Jazmine", "Age": 30, "City": "New York"},
        {"Name": "Luis", "Age": 35, "City": "Chicago"},
        {"Name": "bloz", "Age": 662.7, "City": True},
        {"Name": 32, "Age": True, "City": "Chicago"},
    ]

    with open(example_csv, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Age", "City"])
        writer.writeheader()
        writer.writerows(rows)


def open_data_notes() -> None:
    with open("./week-7/data/notes.txt", "r") as file:
        lines: list[str] = file.readlines()  # Returns a list — one string per line.
        line_num: int = 1
        for line in lines:
            print(f"Line {line_num}: {line.strip()}")
            line_num += 1


def open_data_notes_line_by_line() -> None:
    with open("./week-7/data/notes.txt", "r") as file:
        for line_num, line in enumerate(file, start=1):
            print(f"Line {line_num}: {line.strip()}")


# endregion warmup


# region main
def main() -> None:
    # region .TXT
    # open_read_example()
    # open_read_by_line_example()
    # open_readlines_example()
    # try:
    #     open_error_example()
    # finally:
    #     print("skipping 'open_error_example'")
    # open_write_example()
    # overwrite("nono")
    # endregion .TXT

    # region .CSV
    # open_csv_read_example()
    # open_csv_write_example()
    # open_csv_dictreader_example()
    # endregion .CSV

    # warmup1
    open_data_notes()


if __name__ == "__main__":
    main()
