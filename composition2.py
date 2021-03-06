
class Bookshelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books."


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


book = Book("Go 101")
boo2 = Book("Python 101")
shelf = Bookshelf(book, boo2)

print(shelf)
print(len(shelf.books))

