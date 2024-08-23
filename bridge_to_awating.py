import asyncio


class Awaitable:
    def __await__(self):
        print('About to await')
        yield
        print('Resuming')

def function():
    return Awaitable() #returns a new instance of an Awaitable type

async def main():#designates main as an asynchronous function
    await function()

print(main())#doesn't execute, just get a coroutine object back

asyncio.run(main())#must run main under the supervision of other code