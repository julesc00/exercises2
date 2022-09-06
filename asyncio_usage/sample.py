"""
Book: Using Asyncio in Python Understanding Asynchronous Programming Features
Example 2.1 Best practice for threading
"""
from concurrent.futures import ThreadPoolExecutor as Executor


def worker(data):
    # <Process the data>
    with Executor(max_workers=10) as exe:
        future = exe.submit(worker, data)
