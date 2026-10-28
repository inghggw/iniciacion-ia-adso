import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    servidor = StdioServerParameters(command="python", args=["servidor_mcp.py"])
    async with stdio_client(servidor) as (leer, escribir):
        async with ClientSession(leer, escribir) as sesion:
            await sesion.initialize()
            herramientas = await sesion.list_tools()
            for h in herramientas.tools:
                print(h.name, "-", h.description)
            print(await sesion.call_tool("crear_tarea", {"titulo": "Probar MCP"}))
            print(await sesion.call_tool("listar_tareas", {}))


asyncio.run(main())
