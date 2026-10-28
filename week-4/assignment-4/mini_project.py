"""
Each 'dict' is a 'row'
Each 'key' is a 'column'
Each value is a cell located at dict key
This is one of the most confusing concepts for me.
Reasoning:
    Each dict vertically stacks the columns and rows (rows make sense)
    Each column, as seen below, is vertically stacked.
    Since I am visually based, seeing it as it is below throws me in a loop.
"""
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

top_student: str = ""
top_score: int = -1
total_score: float = 0.0
subject_set: set[str] = set() # set() is required since an empty '{}' creates a dictionary.
high_scorers: list[str] = []

for student in students:
    name: str = str(student["name"])
    score: int = int(student["score"])
    subject: str = str(student["subject"])
    
    # 1. Track top scorer
    #    records score and name only if the score is greater than the last input score
    if score > top_score:
        top_score = score
        top_student = name

    # 2. Accumulate total score for class average
    #    for each 'row' (dictionary), the score 'column' is added to the total_score
    total_score += score

    # 3. Collect unique subjects
    #    Since sets remove duplicates, overlaps when adding are ok.
    #    Add is used since the object is a set.
    subject_set.add(subject)

    # 4. Collect students scoring above 75
    #    Greater than comparison to filter results. 
    #    Append is used since the object is a list.
    if score > 75:
        high_scorers.append(name)

class_average: float = total_score / len(students)

print(f"Top scorer:       {top_student} ({top_score})")
print(f"Class average:    {class_average}")
print(f"Subjects offered: {subject_set}")
print(f"High scorers:     {high_scorers}")