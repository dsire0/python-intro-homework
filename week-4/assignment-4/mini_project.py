students: list[dict[str, str | int]] = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]


print("Top scorer: ")

adding: float = 0
average: float = 0
subject_set: set[str] = set()
highscore_list: list[str] = []
for tionary in students:
    for key, value in tionary.items():
        # print(type(key))
        # print(type(value))
        if key == "score":
            adding += float(value)
            if int(value) > 75:
                highscore_list.append

        if key == "subject":
            subject_set.add(str(value))


average = adding / len(students)
print(f"Class average: {average}")

print(f"Subjects offered: {subject_set}")


print("High scorers:")