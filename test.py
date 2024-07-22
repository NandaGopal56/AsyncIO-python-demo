import httpx
import asyncio

async def make_request(client, url):
    try:
        print('Making an api call...')
        response = await client.get(url)
        print(response.json())
    except httpx.RequestError as exc:
        print(f"An error occurred while requesting {exc.request.url!r}: {exc}")

async def main():
    url = 'http://127.0.0.1:8000/sync'
    timeout = httpx.Timeout(60.0, read=60.0)
    async with httpx.AsyncClient(timeout=timeout) as client:
        tasks = [make_request(client, url) for _ in range(5)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())