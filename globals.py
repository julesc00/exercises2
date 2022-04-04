
A = "hello"

def my_func():
    A = "hhi"
    print(A)

def my_func2():
    print(A)

def my_func3():
    global A
    A = "que show!"
    print(A)

def my_func4():
    print(A)

my_func()
my_func2()
my_func3()
my_func4()


def pick_random():
    names = ["Diego", "Alfonso", "Lucero", "Javier G", "Camilo", "Norberto"]