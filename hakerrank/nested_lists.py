
def list_students_grades():
    students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    students.sort(key=lambda x: x[1], reverse=True)
    second_lowest_students = []
    for student in students:
        if student[1] == students[-2][1]:
            second_lowest_students.append(student)
    # Oneliner [second_lowest_students.append(student) for student in students if student[1] == students[-2][1]]
    for student in sorted(second_lowest_students):
        print(student[0])
    # Oneliner [print(student[0]) for student in sorted(second_lowest_students)]


if __name__ == "__main__":
    list_students_grades()
