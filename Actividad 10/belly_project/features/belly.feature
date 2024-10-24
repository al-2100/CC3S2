Feature: Característica del Estómago Extendida

  Scenario: comer muchos pepinos y gruñir
    Given que he comido 42 pepinos
    When espero 2 horas
    Then mi estómago debería gruñir

  Scenario: comer pocos pepinos y no gruñir
    Given que he comido 10 pepinos
    When espero 2 horas
    Then mi estómago no debería gruñir

  Scenario: comer muchos pepinos y esperar menos de una hora
    Given que he comido 50 pepinos
    When espero media hora
    Then mi estómago no debería gruñir

  Scenario: comer pepinos y esperar en minutos
    Given que he comido 30 pepinos
    When espero 90 minutos
    Then mi estómago debería gruñir

  Scenario: comer pepinos y esperar en diferentes formatos
    Given que he comido 25 pepinos
    When espero "dos horas y treinta minutos"
    Then mi estómago debería gruñir

  Scenario: Comer diferentes cantidades de pepinos en varios tiempos
    Given que he comido 30 pepinos
    When espero "una hora y treinta minutos"
    Then mi estómago debería gruñir

  Scenario: Comer pepinos sin especificar cantidad exacta
    Given que he comido "un montón" pepinos
    When espero 3 horas
    Then mi estómago debería gruñir

  Scenario: Comer pepinos y esperar un tiempo exacto en minutos
    Given que he comido 20 pepinos
    When espero 120 minutos
    Then mi estómago debería gruñir

  Scenario: Comer pepinos expresados en palabras y tiempo en minutos
    Given que he comido veinticinco pepinos
    When espero "noventa minutos"
    Then mi estómago debería gruñir

  Scenario: Comer una cantidad no válida de pepinos
    Given que he comido mil pepinos
    When espero 2 horas
    Then debería ocurrir un error de cantidad no válida

  Scenario: Comer cero pepinos y esperar mucho tiempo
    Given que he comido 0 pepinos
    When espero 5 horas
    Then mi estómago no debería gruñir

  Scenario: Comer una cantidad negativa de pepinos
    Given que he comido -5 pepinos
    When espero 2 horas
    Then debería ocurrir un error de cantidad no válida

  Scenario: Comer más de 100 pepinos
    Given que he comido 150 pepinos
    When espero 3 horas
    Then debería ocurrir un error de cantidad no válida
