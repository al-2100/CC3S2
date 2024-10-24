Feature: Gestión de tareas con prioridades

  Scenario: Procesar tareas en orden de prioridad
    Given que agrego la tarea "Tarea 1" con prioridad 2
    And que agrego la tarea "Tarea 2" con prioridad 5
    And que agrego la tarea "Tarea 3" con prioridad 3
    When proceso las tareas
    Then la tarea "Tarea 2" debe procesarse primero
    And la tarea "Tarea 3 " debe procesarse después
    And la tarea "Tarea 1" debe procesarse al final

  Scenario: Procesar tareas con igual prioridad en orden de llegada
    Given que agrego la tarea "Tarea1" con prioridad 3
    And que agrego la tarea "Tarea2" con prioridad 3
    When proceso las tareas
    Then la tarea "Tarea1" debe procesarse primero
    And la tarea "Tarea2" debe procesarse después

  Scenario: Excepción al procesar una cola vacía
    Given que la cola está vacía
    When intento procesar una tarea
    Then debo recibir un error de tipo "IndexError"

