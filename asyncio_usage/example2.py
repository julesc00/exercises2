import asyncio


# A coroutine is any function that has the 'async' word before it.
async def main():
    print("Julio")
    # Create a task to run async
    task = asyncio.create_task(foo("Me here!"))
    await task
    await asyncio.sleep(0.5)
    print("Finished")


async def foo(text):
    print(text)
    await asyncio.sleep(10)


async def bar(text):
    print(text)
    await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())
    asyncio.run(foo("Hi there!"))
    asyncio.run(bar("Hi there again!!!"))
