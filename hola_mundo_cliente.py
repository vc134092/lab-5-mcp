import asyncio
from fastmcp import Client

async def main():
    async with Client("hola_mundo_server.py") as client:
        result = await client.call_tool(
            name="say_hello", 
            arguments={"name": "Pedro"}
        )
    print(result)

asyncio.run(main())