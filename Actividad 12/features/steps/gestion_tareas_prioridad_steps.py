from behave import *
from cola import ColaDeTareas

@given('que agrego la tarea "{nombre_tarea}" con prioridad {prioridad:d}')
def paso_agregar_tarea(contexto, nombre_tarea, prioridad):
    if not hasattr(contexto, 'cola'):
        contexto.cola = ColaDeTareas()  # Inicializa la cola si no existe aún
    contexto.cola.agregar_tarea(nombre_tarea, prioridad)


@when('proceso las tareas')
def paso_procesar_tareas(contexto):
    contexto.tareas_procesadas = contexto.cola.procesar_tareas()

@then('la tarea "{tarea_esperada}" debe procesarse primero')
def paso_verificar_primera_tarea(contexto, tarea_esperada):
    assert contexto.tareas_procesadas[0] == tarea_esperada

@then('la tarea "{tarea_esperada}" debe procesarse después')
def paso_verificar_tarea_siguiente(contexto, tarea_esperada):
    assert contexto.tareas_procesadas[1].strip() == tarea_esperada.strip()

@then('la tarea "{tarea_esperada}" debe procesarse al final')
def paso_verificar_tarea_final(contexto, tarea_esperada):
    assert contexto.tareas_procesadas[-1] == tarea_esperada

@given('que la cola está vacía')
def paso_cola_vacia(contexto):
    contexto.cola = ColaDeTareas()  # Cola inicializada, pero vacía

@when('intento procesar una tarea')
def paso_procesar_cola_vacia(contexto):
    try:
        contexto.cola.procesar_tarea()
        assert False, "Se esperaba una excepción IndexError"
    except IndexError:
        contexto.error = "IndexError"

@then('debo recibir un error de tipo "IndexError"')
def paso_verificar_error(contexto):
    assert contexto.error == "IndexError"

