from fastapi.testclient import TestClient

from main import app

cliente = TestClient(app)


def test_crear_y_listar():
    respuesta = cliente.post("/tareas", json={"titulo": "Estudiar FastAPI"})
    assert respuesta.status_code == 201
    tarea = respuesta.json()
    assert tarea["titulo"] == "Estudiar FastAPI"
    assert tarea["hecha"] is False

    lista = cliente.get("/tareas").json()
    assert tarea in lista
