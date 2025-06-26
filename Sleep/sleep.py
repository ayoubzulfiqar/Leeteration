import asyncio

async def sleep(millis: int):
    await asyncio.sleep(millis / 1000.0)