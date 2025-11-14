import asyncio
import time


async def foo_sleep(time: int = 3):
    print(f"start load data {time}")
    await asyncio.sleep(time)
    print(f"end load data {time}")
    return time


async def main():
    task1 = asyncio.create_task(foo_sleep(7))
    task2 = asyncio.create_task(foo_sleep(5))
    await print(result1)
    result1 = await task1
    print("kek")

    result2 = await task2
    print(result2)


asyncio.run(main())
