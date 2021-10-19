"""
Input a list of student heights
"""


def student_heights():
    s_heights = input("Enter Ss heights: ").split()
    print(s_heights)
    for n in range(0, len(s_heights)):
        s_heights[n] = round(float(s_heights[n]))

    print(s_heights)


student_heights()
