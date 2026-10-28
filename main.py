from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="API de tareas")


class TareaNueva(BaseModel):
    titulo: str
    hecha: bool = False


class Tarea(TareaNueva):
    id: int


tareas: dict[int, Tarea] = {}
siguiente_id = 1


@app.get("/tareas")
def listar() -> list[Tarea]:
    return list(tareas.values())


@app.post("/tareas", status_code=201)
def crear(datos: TareaNueva) -> Tarea:
    global siguiente_id
    tarea = Tarea(id=siguiente_id, **datos.model_dump())
    tareas[tarea.id] = tarea
    siguiente_id += 1
    return tarea
