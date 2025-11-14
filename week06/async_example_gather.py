import asyncio
import time

import aiohttp
import requests


async def foo_http_req(url):
    resp = requests.get(url)


async def foo_aio_http_req(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            pass


async def not_assync_main():
    print("start not_assync_main")
    i = 1
    url = ["https://www.google.com"] * i

    start_time = time.time()
    await asyncio.gather(*[foo_http_req(url_i) for url_i in url])
    print(f"Total time taken for {i} reqs: {time.time() - start_time}")


async def assync_main():
    print("start assync_main")
    i = 1
    url = ["https://www.google.com"] * i

    start_time = time.time()
    await asyncio.gather()
    print(f"Total time taken for {i} reqs: {time.time() - start_time}")


if __name__ == "__main__":
    asyncio.run(not_assync_main())
    asyncio.run(assync_main())
