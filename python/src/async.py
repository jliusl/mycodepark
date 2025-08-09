import asyncio
import time


async def process_data(num):
    await asyncio.sleep(1)
    print(f"start coroutine: {num}")


async def main():
    start = time.time()
    objs = [process_data(i) for i in range(10)]
    await asyncio.gather(*objs)
    end = time.time()
    print(f"elapsed time: {end - start:.2f}")

if __name__ == "__main__":
    asyncio.run(main())