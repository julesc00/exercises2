x, y = 5, 10

students_attendance = {"Benito": 96, "Michele": 80, "Charbel": 90}

print(list(students_attendance.items()))

for s, a in students_attendance.items():
    print(s, a)


# Example 2
people = [
    ("Caricia", 21, "Chef"),
    ("Franz-che", 19, "Artist"),
    ("Jules", 18, "Saint"),
    ("Cesar", 17, "Engineer"),
    ("Julito", 16, "Engineer"),
    ("Lucien", 13, "Teacher"),
    ("Brigitte", 12, "Athlete"),
    ("Michele", 11, "Dancer"),
    ("Benito", 4, "Athlete"),
    ("Charbel", 2, "Scientist"),
    ("Jemima", 1, "Scientist")
]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profression: {profession}")

# or, which looks weird, but it's accessing indexes.
for person in people:
    print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")


# ignoring a value _
person = ("Claudia", 39, "Athlete")
name, _, profession = person

# head and tail or tail and head
head, *tail = [1, 2, 3, 4, 5]  # prints 1 and then: [2, 3, 4, 5]
*head2, tail2 = [1, 2, 3, 4, 5]  # prints [1, 2, 3, 4] and then 5
print(head)
print(tail)
print(head2)
print(tail2)
