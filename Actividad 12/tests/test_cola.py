import pytest
from cola import ColaDeTareas

def test_procesar_tareas():
    # Arrange: Configurar la cola de prioridades y agregar las tareas
    cola = ColaDeTareas()
    cola.agregar_tarea("Tarea1", 2)
    cola.agregar_tarea("Tarea2", 5)
    cola.agregar_tarea("Tarea3", 3)

    # Act: Procesar las tareas
    tareas_procesadas = cola.procesar_tareas()

    # Assert: Verificar el orden de procesamiento
    assert tareas_procesadas == ["Tarea2", "Tarea3", "Tarea1"]


def test_procesar_tareas_en_orden_de_prioridad():
    # Arrange: Crear una cola de prioridad y agregar tareas
    cola = ColaDeTareas()
    cola.agregar_tarea("Tarea1", 2)
    cola.agregar_tarea("Tarea2", 1)
    cola.agregar_tarea("Tarea3", 2)

    # Act: Procesar las tareas
    tareas_procesadas = cola.procesar_tareas()

    # Assert: Verificar el orden correcto de las tareas procesadas
    assert tareas_procesadas == ["Tarea1", "Tarea3", "Tarea2"]

def test_procesar_cola_vacia():
    # Arrange: Crear una cola vacía
    cola = ColaDeTareas()

    # Act & Assert: Verificar que se lanza una excepción al intentar procesar una tarea en una cola vacía
    with pytest.raises(IndexError):
        cola.procesar_tarea()
