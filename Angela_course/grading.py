"""
Write a program that conversts their scores to grades. By the end of
the program, you should have a new dictionary called student_grades that
contains student names for keys and their grades for values. The final
version of the student_grades will be checked.

Constrains:
    DO NOT modify the existing student_scores dict.
    DO NOT write any print statements.
"""
from collections import defaultdict
import pprint

STUDENT_SCORES = {
    "Harry": 91,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

pp = pprint.PrettyPrinter(indent=2)


def change_scores_to_grades(scores: dict) -> dict:
    student_grades = {}

    for name, value in scores.items():
        if value >= 91:
            student_grades[name] = "Outstanding"
        elif value > 80 < 91:
            student_grades[name] = "Exceeds Expectations"
        elif value > 70 < 81:
            student_grades[name] = "Acceptable"
        elif value <= 70:
            student_grades[name] = "Fail"

    return student_grades


pp.pprint(change_scores_to_grades(STUDENT_SCORES))
