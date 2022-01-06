import matplotlib.pyplot as p

S = [40, 30, 10, 15, 6]
L = ["Python", "JavaScript", "Java", "R", "C"]


def show_pie_chart(vals: list, lang: list):
    p.pie(vals, labels=lang)
    return p.show()


if __name__ == "__main__":
    show_pie_chart(S, L)
