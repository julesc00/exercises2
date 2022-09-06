import os
from time import sleep
from threading import Thread

# This will generate an error in macOS
threads = [Thread(target=lambda: sleep(60)) for _ in range(10000)]

# print([t.start() for t in threads])
# print(f"PID = {os.getpid()}")
# print([t.join() for t in threads])

hellos = ["Hello" for _ in range(10)]
print(len(hellos))
