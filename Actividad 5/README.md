# Sobre la Actividad

## Documentación
- El procedimiento de la Actividad 5 no se ha documentado, pues el desarrollo fue hecho en la clase del día **11/09/2024**.
- En la **Actividad 4** se incluyeron capturas de pantalla de la consola en cada paso de los ejercicios. Sin embargo, para esta **Actividad 5**, no se incluirán capturas de **todos** los pasos, ya que esto dificulta la documentación. Además, los comandos utilizados son los mismos que se indican en las instrucciones de la actividad. Solo se mostrarán capturas en caso de ser necesario (ejemplo: mostrar alguna salida relevante).
## Manejo de repositorios
**Objetivo:** Se deben integrar varios repositorios, que contienen ejercicios específicos, en un único repositorio del curso (`CC3S2`) de manera organizada y manteniendo el historial de commits de cada repositorio.

**Solución:** Usar `git subtree` porque permite integrar el contenido de un repositorio en otro sin perder el historial de commits y también se puede agregar repositorios en subcarpetas específicas.

**Ejemplo:**
1. Nos posicionamos en el directorio principal
2. Agregar el Repositorio como _remote_
3. Integrar el Repositorio Usando `git subtree`
4. Eliminar el _remote_
	```shell
	cd C:\Users\Alonso\Documents\GitHub\CC3S2
	git remote add scrum-workflow file:///C:/Users/Alonso/Desktop/CC3S2/scrum-workflow
	git subtree add --prefix="Actividad 5/scrum-workflow" scrum-workflow main
	git remote remove scrum-workflow
	```

El repositorio para el ejercicio de `scrum-project` se encuentra en GitHub: https://github.com/al-2100/scrum-project.git

---
# Preguntas de discusión
1. ¿Por qué se considera que rebase es más útil para mantener un historial de proyecto lineal en comparación con merge?

	El rebase es una herramienta efectiva para mantener un historial de proyecto lineal, ya que reescribe los commits de una rama aplicándolos sobre la base de otra rama, creando una línea de tiempo continua y simplificada. En contraste, el merge preserva el historial completo, incluyendo los commits de fusión, lo que puede generar un historial más complejo.

2. ¿Qué problemas potenciales podrían surgir si haces rebase en una rama compartida con otros miembros del equipo?

	El rebase en una rama compartida puede generar confusiones y conflictos entre los miembros del equipo. Los commits reescritos pueden causar problemas de sincronización y pérdida de trabajo. Por lo tanto, es recomendable realizar rebase solo en ramas locales y privadas.

3. ¿En qué se diferencia cherry-pick de merge, y en qué situaciones preferirías uno sobre el otro?

	El cherry-pick permite seleccionar commits específicos de una rama y aplicarlos a otra, lo que es útil cuando solo se necesitan integrar ciertos cambios. Por otro lado, el merge combina todo el historial de una rama con otra, lo que es preferible cuando se desea integrar una rama completa. La elección entre cherry-pick y merge dependerá de las necesidades específicas del proyecto.

4. ¿Por qué es importante evitar hacer rebase en ramas públicas?

	Es fundamental evitar realizar rebase en ramas públicas, ya que la reescritura del historial puede generar problemas complejos para los colaboradores y afectar la integridad del proyecto. En su lugar, se recomienda utilizar merge para integrar cambios y mantener un historial consistente y preservar la colaboración efectiva.

---
# Ejercicios teóricos
## 1. Diferencias entre git merge y git rebase
Pregunta: Explica la diferencia entre git merge y git rebase y describe en qué escenarios sería más adecuado utilizar cada uno en un equipo de desarrollo ágil que sigue las prácticas de Scrum.

**git merge**

`git merge` combina los cambios de dos ramas en una nueva "commit de fusión" (merge commit), manteniendo intacta la historia de ambas ramas. Esta opción es ideal para:

- Integrar ramas completas: Cuando una rama de características está completamente desarrollada y lista para ser integrada con la rama principal.
- Colaboración en equipo: Cuando múltiples desarrolladores trabajan en ramas compartidas y necesitan fusionar sus cambios.

Ventajas de `git merge`:

- Mantiene un historial completo y detallado.
- Las decisiones y combinaciones están claramente documentadas en el historial de commits.

Desventajas de `git merge`:

- El historial puede volverse complicado con múltiples commits de fusión.

**git rebase**

`git rebase` reescribe el historial de una rama aplicando sus commits sobre la base de otra rama. Esta opción es ideal para:

- Limpiar el historial de una rama antes de fusionarla con la rama principal.
- Trabajo en ramas locales: Antes de compartir cambios con el equipo, es útil rebasar para mantener un historial lineal.

Ventajas de `git rebase`:

- El historial se mantiene lineal y más fácil de seguir.
- Simplifica la revisión y el entendimiento del historial de cambios.

Desventajas de `git rebase`:

- Puede causar conflictos si se usa en ramas compartidas.
- Requiere que los cambios locales se resuelvan antes de la fusión.

En conclusión, `git merge` es ideal para integrar ramas completas y colaborar en equipo, mientras que `git rebase` es mejor para limpiar el historial de una rama antes de fusionarla y para trabajo en ramas locales.

## 2. Relación entre git rebase y DevOps
Pregunta: ¿Cómo crees que el uso de git rebase ayuda a mejorar las prácticas de DevOps, especialmente en la implementación continua (CI/CD)? Discute los beneficios de mantener un historial lineal en el contexto de una entrega continua de código y la automatización de pipelines.

Mantener un historial lineal con rebase ayuda a simplificar la comprensión del historial del código, lo cual es crucial para la entrega continua (CI). Un historial limpio facilita el rastreo de cambios y la identificación de problemas. Además, La resolución de conflictos en una historia lineal es más manejable, especialmente cuando se automatiza el proceso en pipelines CI/CD.

En la implementación continua (CD), los pipelines CI/CD pueden ejecutarse de manera más eficiente con un historial claro, ya que es más fácil determinar qué cambios han sido aplicados y cómo afectan el código.

## 3. Impacto del git cherry-pick en un equipo Scrum
Pregunta: Un equipo Scrum ha finalizado un sprint, pero durante la integración final a la rama principal (main) descubren que solo algunos commits específicos de la rama de una funcionalidad deben aplicarse a producción. ¿Cómo podría ayudar git cherry-pick en este caso? Explica los beneficios y posibles complicaciones.

Cuando solo algunos commits de una rama de características deben aplicarse a producción, git cherry-pick permite seleccionar y aplicar esos commits específicos a la rama principal (main).

Beneficios:

- Permite integrar cambios específicos sin arrastrar todo el historial de la rama feature, lo que puede ser útil si solo ciertos cambios son relevantes para la producción.
- Ofrece la capacidad de aplicar correcciones o mejoras específicas de una rama a otra sin necesidad de fusionar completamente todas las modificaciones.

Posibles Complicaciones:

- Puede generar conflictos si los commits seleccionados dependen de otros cambios que no están presentes en la rama de destino.

---
# Ejercicios
## Ejercicio 1: Simulación de un flujo de trabajo Scrum con git rebase y git merge

### Pasos
1. Crea un repositorio y haz algunos commits en la rama main.
	```shell
	mkdir scrum-workflow
	cd scrum-workflow
	git init
	echo "Commit inicial en main" > mainfile.md
	git add mainfile.md
	git commit -m "Commit inicial en main"
	```
2. Crea una rama feature, agrega nuevos commits, y luego realiza algunos commits adicionales en main.
	```shell
	git checkout -b feature
	echo "Nueva característica en feature" > featurefile.md
	git add featurefile.md
	git commit -m "Commit en feature"
	
	git checkout main
	echo "Actualización en main" >> mainfile.md
	git add mainfile.md
	git commit -m "Actualización en main"
	```
3. Realiza un rebase de feature sobre main.
	```shell
	git checkout feature
	git rebase main
	```
4. Finalmente, realiza una fusión fast-forward de feature con main.
	```shell
	git checkout main
	git merge feature --ff-only
	```
### Preguntas
- ¿Qué sucede con el historial de commits después del rebase?
	El rebase toma los commits de la rama `feature` y los coloca sobre los commits más recientes de `main`, reescribiendo el historial. Esto hace que los commits de `feature` parezcan haber sido realizados después de los últimos cambios en `main`, creando un historial más lineal y limpio.
- ¿En qué situación aplicarías una fusión fast-forward en un proyecto ágil?
	Una fusión fast-forward se puede aplicar cuando no ha habido divergencias entre las ramas, lo que suele ocurrir cuando se trabaja en sprints cortos y los desarrolladores integran sus cambios de manera frecuente. Esta técnica ayuda a mantener un historial simple y fácil de seguir, algo que es beneficioso en proyectos ágiles donde la claridad y la transparencia son importantes.
## Ejercicio 2: Cherry-pick para integración selectiva en un pipeline CI/CD

### Pasos
1. Crea un repositorio con una rama main y una rama feature.
	```shell
	mkdir ci-cd-workflow
	cd ci-cd-workflow
	git init
	echo "Commit inicial en main" > main.md
	git add main.md
	git commit -m "Commit inicial en main"
	```
2. Haz varios commits en la rama feature, pero solo selecciona uno o dos commits específicos que consideres listos para producción.
	```shell
	git checkout -b feature
	echo "Primera característica" > feature1.md
	git add feature1.md
	git commit -m "Agregar primera característica"
	echo "Segunda característica" > feature2.md
	git add feature2.md
	git commit -m "Agregar segunda característica"
	```
3. Vemos el historial de commits para copiar los hashes de cada commit.
	![[consola2_1.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%205/imagenes/consola2_1.png?raw=true)
4. Realiza un cherry-pick de esos commits desde feature a main.
	```shell
	git checkout main
	git cherry-pick 8ead39b
	git cherry-pick 20a0d3a
	```
	![[consola2_2.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%205/imagenes/consola2_2.png?raw=true)
5. Verifica que los commits cherry-picked aparezcan en main.
	```shell
	git log --oneline
	git log --oneline --graph --all
	```
	![[consola2_3.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%205/imagenes/consola2_3.png?raw=true)
	
	![[consola2_4.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%205/imagenes/consola2_4.png?raw=true)
### Preguntas
- ¿Cómo utilizarías cherry-pick en un pipeline de CI/CD para mover solo ciertos cambios listos a
producción?
	En un pipeline CI/CD, cherry-pick puede ser útil cuando se desea integrar solo ciertos commits listos para producción sin llevar todos los cambios de una rama en desarrollo. Esto puede suceder si la funcionalidad completa aún no está lista, pero se necesita adelantar algunos cambios críticos. Usar cherry-pick permite integrar únicamente esos commits específicos en la rama de producción, asegurando que el pipeline solo implemente lo que está listo.
- ¿Qué ventajas ofrece cherry-pick en un flujo de trabajo de DevOps?
	Cherry-pick permite mayor flexibilidad en el manejo de cambios al permitir la integración selectiva de commits. Esto es útil en DevOps cuando solo ciertos cambios han sido aprobados o necesitan ser desplegados rápidamente. También reduce el riesgo de introducir código inestable o incompleto en producción, lo que mejora la estabilidad y control sobre los despliegues en un entorno ágil.
# Git, Scrum y Sprints

Este ejercicio se desarrolla en el siguiente repositorio: https://github.com/al-2100/scrum-project.git
## Fase 1: Planificación del sprint (sprint planning)
### Ejercicio 1: Crear ramas de funcionalidades (feature branches)
#### Pasos
1. Crea un repositorio en Git.
	```shell
	mkdir scrum-project
	cd scrum-project
	git init
	```
2. Crea una rama main donde estará el código base.
	```shell
	echo "# Proyecto Scrum" > README.md
	git add README.md
	git commit -m "Commit inicial en main"
	```
3. Crea una rama por cada historia de usuario asignada al sprint, partiendo de la rama main
	```shell
	git checkout -b feature-user-story-1
	git checkout -b feature-user-story-2
	```
#### Pregunta
**¿Por qué es importante trabajar en ramas de funcionalidades separadas durante un sprint?**
Trabajar en ramas de funcionalidades separadas permite a los equipos Scrum mantener el trabajo de cada **historia de usuario** aislado del resto del proyecto. Esto nos permite trabajar sin interferir con el código de otras funcionalidades y hace posible que diferentes miembros del equipo trabajen en distintas funcionalidades sin interferir entre ellos. Además, asegura que al finalizar la funcionalidad se pueda revisar y fusionar la rama a `main` solo si el código está listo.
## Fase 2: Desarrollo del sprint (sprint execution)
### Ejercicio 2: Integración continua con git rebase
#### Pasos
1. Haz algunos commits en main.
	```shell
	git checkout main
	echo "Actualización en main" > updates.md
	git add updates.md
	git commit -m "Actualizar main con nuevas funcionalidades"
	```
2. Realiza un rebase de la rama feature-user-story-1 para actualizar su base con los últimos cambios de main.	
	```shell
	git checkout feature-user-story-1
	git rebase main
	```

![[fase2.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%205/imagenes/fase2.png?raw=true)
#### Pregunta
¿Qué ventajas proporciona el rebase durante el desarrollo de un sprint en términos de integración continua?
Si hago rebase cada vez que hay algo nuevo en `main`, me aseguro de que mi código no se quede atrás y evito grandes conflictos al final del sprint. Además, mantiene el historial mucho más limpio y lineal, lo que hace que sea más fácil revisar los cambios. También ayuda a que el proceso de integración continua sea más fluido, ya que no se tiene que lidiar con una gran cantidad de merges o conflictos justo cuando queremos fusionar todo.
## Fase 3: Revisión del sprint (sprint review)
### Ejercicio 3: Integración selectiva con git cherry-pick
#### Pasos
1. Realiza algunos commits en feature-user-story-2.
	```shell
	git checkout feature-user-story-2
	echo "Funcionalidad lista" > feature2.md
	git add feature2.md
	git commit -m "Funcionalidad lista para revisión"
	echo "Funcionalidad en progreso" > progress.md
	git add progress.md
	git commit -m "Funcionalidad aún en progreso"
	```
2. Haz cherry-pick de los commits que estén listos para mostrarse a los stakeholders durante la revisión del sprint.
	```shell
	git checkout main
	git cherry-pick <hash_del_commit_de_feature-lista>
	```
	
	![[fase3.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%205/imagenes/fase3.png?raw=true)
#### Pregunta
¿Cómo ayuda `git cherry-pick` a mostrar avances de forma selectiva en un sprint review?
Usar `git cherry-pick` en un sprint review permite seleccionar solo los cambios que están completamente listos para mostrarse a los stakeholders. 
En vez de hacer un merge de toda la rama de una funcionalidad que aún tiene partes incompletas, se elige solo los commits que ya están finalizados.
## Fase 4: Retrospectiva del sprint (sprint retrospective)
### Ejercicio 4: Revisión de conflictos y resolución
#### Pasos
1. Realiza cambios en feature-user-story-1 y feature-user-story-2 que resulten en conflictos.
	```shell
	git checkout feature-user-story-1
	echo "Cambio en la misma línea" > conflicted-file.md
	git add conflicted-file.md
	git commit -m "Cambio en feature 1"
	
	git checkout feature-user-story-2
	echo "Cambio diferente en la misma línea" > conflicted-file.md
	git add conflicted-file.md
	git commit -m "Cambio en feature 2"

	```
2. Intenta hacer merge de ambas ramas con main y resuelve los conflictos
	```shell
	git checkout main
	git merge feature-user-story-1
	git merge feature-user-story-2
	```
	
	![[fase4.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%205/imagenes/fase4.png?raw=true)
	![[conflicto.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%205/imagenes/conflicto.png?raw=true)

	![[Software/Actividad 5/conflicto2.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%205/imagenes/conflicto2.png?raw=true)
	```shell
	git add conflicted-file.md
	git commit -m "Resolver conflictos entre feature 1 y feature 2"
	```
	![[conflicto3.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%205/imagenes/conflicto3.png?raw=true)
#### Pregunta
**¿Cómo manejas los conflictos de fusión al final de un sprint? **
- Git muestra ambos cambios y permite decidir cuál debe quedar o cómo combinar los dos. Se debe asegurar de que el resultado final respete la lógica del proyecto. Después de resolverlo, se completa el merge y se hace un commit que documente la resolución.

**¿Cómo puede el equipo mejorar la comunicación para evitar conflictos grandes?**
- Para optimizar la comunicación y prevenir conflictos significativos, es esencial que el equipo mantenga una interacción constante durante el sprint. Esto implica estar informados sobre las modificaciones relevantes que cada miembro realiza. Una estrategia efectiva es revisar y fusionar los cambios en la rama principal con frecuencia, además de realizar fusiones pequeñas y periódicas, evitando así acumularlas hasta el final del sprint. Asimismo, es recomendable coordinar las secciones del código que cada persona está editando para evitar trabajar simultáneamente en los mismos archivos o líneas, lo que podría generar conflictos.
## Fase de desarrollo: automatización de integración continua (CI) con git rebase
### Ejercicio 5: Automatización de rebase con hooks de Git
#### Pasos
1. Configura un hook pre-push que haga un rebase automático de la rama main sobre la rama de funcionalidad antes de que el push sea exitoso.
	```shell
	nano .git/hooks/pre-push
	```
	Y escribimos:
	```
	#!/bin/bash
	git fetch origin main
	git rebase origin/main
	```
	Cambiamos los permisos del archivo para hacerlo ejecutable
	```shell
	chmod +x .git/hooks/pre-push
	```

2. Prueba el hook haciendo push de algunos cambios en la rama feature-user-story-1.
	```shell
	git checkout feature-user-story-1
	echo "Cambios importantes" > feature1.md
	git add feature1.md
	git commit -m "Cambios importantes en feature 1"
	git push origin feature-user-story-1
	```
	![[hook.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%205/imagenes/hook.png?raw=true)

	![[logfinal.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%205/imagenes/logfinal.png?raw=true)

	El hook `pre-push` está diseñado para asegurarse de la rama estuviera actualizada con `main` antes de realizar el `push`.
#### Pregunta

**¿Qué ventajas y desventajas observas al automatizar el rebase en un entorno de CI/CD?**
Al automatizar el rebase en un entorno de CI/CD, se pueden identificar las siguientes ventajas y desventajas:

**Ventajas:**
- **Historial Limpio**: Se mantiene un registro de commits más organizado y comprensible.
- **Reducción de Conflictos**: Se minimiza la posibilidad de conflictos significativos en el futuro, ya que la rama de funcionalidad se mantiene actualizada regularmente.
- **Integración Suave**: Facilita la integración de cambios recientes de la rama principal en las ramas de funcionalidad.

**Desventajas:**
- **Comportamiento Inesperado**: Puede generar problemas si el rebase no se maneja adecuadamente, especialmente si surgen conflictos que no se resuelven automáticamente.
- **Dependencia de la Configuración**: Requiere una configuración correcta del hook y del entorno de CI/CD. Si hay errores en el hook, puede bloquear el proceso de push.

En resumen, la automatización del rebase puede mejorar la organización y reducir conflictos, pero también puede introducir problemas si no se configura o maneja adecuadamente.
