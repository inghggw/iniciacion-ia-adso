import httpx
from mcp.server.mcpserver import MCPServer

API = "http://localhost:8000"
mcp = MCPServer("tareas")


@mcp.tool()
def listar_tareas() -> list[dict]:
    """Devuelve todas las tareas con su id, título y si están hechas."""
    return httpx.get(f"{API}/tareas").json()


@mcp.tool()
def crear_tarea(titulo: str) -> dict:
    """Crea una tarea pendiente con el título indicado y la devuelve."""
    return httpx.post(f"{API}/tareas", json={"titulo": titulo}).json()


if __name__ == "__main__":
    mcp.run()
