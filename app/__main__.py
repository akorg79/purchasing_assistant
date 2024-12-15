import asyncio

from .request import featch_page

async def main():
    await featch_page()


if __name__ == "__main__":
    asyncio.run(main())