import heapq

class ColaDeTareas:
    def __init__(self):
        self.cola = []
        self.contador = 0  # Para mantener el orden de llegada

    def agregar_tarea(self, nombre, prioridad):
        heapq.heappush(self.cola, (-prioridad, self.contador, nombre))
        self.contador += 1

    def procesar_tarea(self):
        if not self.cola:
            raise IndexError("No hay tareas en la cola")
        # Retornar el nombre de la tarea con mayor prioridad
        return heapq.heappop(self.cola)[2]
    def procesar_tareas(self):
        tareas = []
        while self.cola:
            tareas.append(self.procesar_tarea())
        return tareas