from contextlib import contextmanager


class OpenFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with OpenFile("sample_text2.txt", "w") as f:
    f.write("Testing 1 2 3")


print(f.closed)


@contextmanager
def open_file(file, mode):
    """Function-based custom context manager."""

    f = open(file, mode)
    yield f
    f.close()


with open_file("sample_text.txt", "w") as f:
    f.write("que ta bañes más carnal")

print(f.closed)

