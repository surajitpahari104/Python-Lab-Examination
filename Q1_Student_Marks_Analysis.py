# Question 1: Student Marks Analysis

def analyze_marks(marks):
    print("Highest mark:", max(marks))
    print("Lowest mark:", min(marks))
    print("Average mark:", round(sum(marks) / len(marks), 2))
    passed = sum(1 for mark in marks if mark >= 40)
    print("Number of students passed:", passed)

analyze_marks([78, 35, 92, 45, 60, 28, 88])
