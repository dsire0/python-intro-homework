# Warmup letter grades

# List of values to test
# for -1, D is expected because I did not compare the "score" for grades D,C,B,A with >= or >.
scores: list = [-1,0,59,60,69,70,79,80,89,90,99,100,101]

# Single hardcode value
score: int = 0

# Empty Intial string
grade: str = ""

# For each value in the list "scores", check the grade.
for value in scores:
    score = value

    if score < 60 and score >= 0 :
        grade = "F"
    elif score < 70:
        grade = "D"
    elif score < 80:
        grade = "C"
    elif score < 90:
        grade = "B"
    elif score <= 100:
        grade = "A"
    else:
        score = 9001
        grade = "It's over 9000!"

    print(f"Score: {score} - Grade: {grade}")