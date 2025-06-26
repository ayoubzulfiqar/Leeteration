import asyncio

async def addTwoPromises(promise1, promise2):
    val1 = await promise1
    val2 = await promise2
    return val1 + val2