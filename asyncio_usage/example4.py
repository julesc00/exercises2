import asyncio

"""
def task1():
    print("Send first email")
    print("First email reply")
    task2()


def task2():
    print("Send Second email")
    print("Second email reply")
    task3()


def task3():
    print("Send Third email")
    print("Third email reply")
    print("====")
    print("END")


task1()
"""


async def task1():
    print("Sending first email")
    asyncio.create_task(task2())
    await asyncio.sleep(2)  # Simulating that the email replay takes 2 seconds.
    print("First email reply")


async def task2():
    print("Send second email")
    asyncio.create_task(task3())
    await asyncio.sleep(2)
    print("Second email reply")


async def task3():
    print("Send third email")
    await asyncio.sleep(2)
    print("Third email reply")


if __name__ == '__main__':
    asyncio.run(task1())

