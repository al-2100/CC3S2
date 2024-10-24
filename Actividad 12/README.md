## Ejercicio 1: Implementación de un sistema de colas con prioridades

### Descripción General
Las tareas deben procesarse en orden de prioridad (de mayor a menor) y, en caso de igual prioridad, en orden de llegada.

### Historia de Usuario
Como usuario del sistema de gestión de tareas, 
quiero agregar tareas con diferentes niveles de prioridad, 
para que se procesen en el orden adecuado, dando prioridad a las más urgentes y respetando el orden de llegada si tienen la misma prioridad.

### Criterios de Aceptación
1. Las tareas deben procesarse en orden de prioridad, donde las de mayor prioridad se procesen primero.
2. Si dos o más tareas tienen la misma prioridad, deben procesarse en el orden en que fueron agregadas.
3. El sistema debe manejar excepciones si se intenta procesar una tarea cuando la cola está vacía.

### Funcionalidad
El sistema utiliza una estructura de datos de tipo cola de prioridad implementada con `heapq` de Python. Cada tarea se inserta en la cola junto con su prioridad y un contador para asegurar el orden de llegada en caso de igual prioridad. Cuando se procesan las tareas, se extraen en función de su prioridad y orden de llegada.

### Implementación
- **Archivo `cola.py`**: Define la clase `ColaDeTareas`, que implementa los métodos `agregar_tarea` y `procesar_tareas`. La prioridad de las tareas se maneja con una cola de prioridad.
- **Archivo `test_cola.py`**: Contiene pruebas unitarias utilizando pytest, verificando el orden correcto de las tareas, la prioridad, y el manejo de excepciones cuando la cola está vacía.
- **Archivo `gestion_tareas_prioridad.feature`**: Contiene los escenarios de pruebas en lenguaje Gherkin, los cuales describen cómo deben comportarse las tareas agregadas y procesadas en el sistema.
- **Archivo `gestion_tareas_prioridad_steps.py`**: Implementa los pasos definidos en Behave, que ejecutan las pruebas para verificar el correcto funcionamiento del sistema.

### Escenarios de Prueba
1. **Procesar tareas en orden de prioridad**: Se agrega un conjunto de tareas con diferentes prioridades y se verifica que el procesamiento siga el orden adecuado.
2. **Procesar tareas con la misma prioridad en orden de llegada**: Verifica que cuando las tareas tienen la misma prioridad, se procesan en el orden en que fueron agregadas.
3. **Manejo de excepciones en cola vacía**: Asegura que el sistema lanza una excepción si se intenta procesar una tarea en una cola vacía.
