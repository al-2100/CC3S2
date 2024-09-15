# Sobre la Actividad

## Documentación
El procedimiento de la Actividad 4 no se ha documentado, pues el desarrollo fue hecho en la clase del día **09/09/2024**.

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
git remote add auto-merge file:///C:/Users/Alonso/Desktop/CC3S2/try-auto-merge
git subtree add --prefix="Actividad 4/try-auto-merge" auto-merge main
git remote remove auto-merge
```

---
# Ejercicios

## Ejercicio 1: Clona un repositorio Git con múltiples ramas

- Creamos un repositorio https://github.com/al-2100/ejercicio-fusionar que tiene una estructura conveniente para el desarrollo del ejercicio.
	![[repositorio]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/repositorio.png?raw=true)
	![[repositorio1]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/repositorio1.png?raw=true)
### Pasos
1. Clonamos el repositorio
	![[consola1.1]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consola1.1.png?raw=true)
2. Revisamos el contenido
-  Contenido de `archivo.txt` en `master`:

	![[archivo]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/archivo.png?raw=true)
- Contenido de `archivo.txt` en `rama1` y `rama2` respectivamente

	![[archivo2]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/archivo2.png?raw=true)

	![[archivo3]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/archivo3.png?raw=true)
3. Aplicamos  `git merge --ff` entre `master` y `rama1`
	![[mergeff.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/mergeff.png?raw=true)
4. Revisamos los cambios en `master`

	![[consola1.2.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consola1.2.png?raw=true)

	![[archivo4.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/archivo4.png?raw=true)

### Pregunta

**¿En qué situaciones recomendarías evitar el uso de git merge --ff? Reflexiona sobre las
desventajas de este método.**
- **Evitar `--ff` cuando:**
    - Queremos mantener una historia clara de las ramas: Al utilizar `--ff`, la rama se mueve hacia adelante sin crear un commit de fusión, lo que puede hacer que la historia de la rama sea menos clara.
    - Necesitamos una trazabilidad completa de la integración de características: Con `--ff`, no hay un commit de fusión que registre la integración de la rama, lo que puede dificultar el seguimiento de los cambios.
- **Desventajas:**
    - El historial lineal puede ocultar la historia de las ramas y las fusiones, al no haber commits de fusión, es más difícil ver cuándo y cómo se integraron las características (En este caso el mensaje del commit evidencia el cambio en `rama1`, pero es la excepción).
    - La falta de commits de fusión puede hacer que el historial sea menos comprensible para otros desarrolladores o para nosotros mismos en el futuro.

---
## Ejercicio 2: Simula un flujo de trabajo de equipo

### Pasos

Continuamos trabajando en el mismo repositorio

1. Usamos `--no-ff` con master y rama2
	![[mergenoff.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/mergenoff.png?raw=true)
2. Revisamos los cambios

	![[archivo5.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/archivo5.png?raw=true)

	![[consola2.1.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consola2.1.png?raw=true)

	Aquí notamos la diferencia entre `--no-ff` y `--ff`, en este caso no tenemos un historial lineal
### Preguntas

**¿Cuáles son las principales ventajas de utilizar git merge --no-ff en un proyecto en equipo?**
- Mantiene un historial de ramas más claro: Al crear un commit de fusión, `--no-ff` ayuda a mantener una historia clara de las ramas y sus fusiones.
- Facilita la identificación de cuándo y cómo se integraron características o correcciones: Con `--no-ff`, es fácil ver cuándo y cómo se integraron características o correcciones, ya que cada fusión se registra con un commit.

**¿Qué problemas podrían surgir al depender excesivamente de commits de fusión?**   
- Puede resultar en un historial más complejo si se usa en exceso. Si se utiliza `--no-ff` para cada fusión, el historial puede volverse complejo y difícil de seguir, especialmente si hay muchas fusiones.

## Ejercicio 3: Crea múltiples commits en una rama.

### Pasos

1. Hacemos varios cambios en una rama `feature`

	![[consola3.1.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consola3.1.png?raw=true)

2. Fusiona la rama con git merge --squash para aplanar todos los commits en uno solo

	![[consola3.2.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consola3.2.png?raw=true)

3. Cambios en **master** vs **feature**
	![[consola3.3.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consola3.3.png?raw=true)

	![[consola3.4.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consola3.4.png?raw=true)

	En estas dos capturas de pantalla se aprecia de forma visual el impacto de merge y squash en **master**
### Pregunta

**¿Cuándo es recomendable utilizar una fusión squash?**
- Para consolidar varios commits en un solo commit antes de fusionar una rama.
- Ideal para mantener un historial limpio y manejable, especialmente en ramas con muchos cambios menores.

**¿Qué ventajas ofrece para proyectos grandes en comparación con fusiones estándar?**
- Simplifica el historial de la rama principal al evitar una gran cantidad de commits triviales, como por ejemplo cambios en la documentación.

## Ejercicio 4: Resolver conflictos en una fusión non-fast-forward
### Pasos

1. Crearemos un nuevo repositorio, creamos un archivo `index.html` y realizaremos commits en la rama **main** y **feature-update** para preparar las bases del ejercicio

	Pasos:

	![[consola4.1.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consola4.1.png?raw=true)

	Logs para comprender el contexto

	![[consola4.2.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consola4.2.png?raw=true)

2. Aplicamos merge con `--no-ff` para fusionar **main** y **feature-update**

	![[consola4.3.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consola4.3.png?raw=true)

3. Resolvemos conflictos

	![[html.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/html.png?raw=true)

4. Agregamos el archivo corregido y completamos la fusión

	![[consola4.4.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consola4.4.png?raw=true)
### Preguntas

1. **¿Qué pasos adicionales tuviste que tomar para resolver el conflicto?**

	Tuve que abrir el archivo `index.html` porque Git detectó un conflicto en él durante la fusión. Encontré las marcas de conflicto (`<<<<<<<`, `=======`, `>>>>>>`), que señalaban las diferencias entre la rama `main` y `feature-update`. Para resolverlo, decidí combinar ambos cambios en una nueva versión. Mantuve el encabezado original del proyecto y agregué tanto el footer como el párrafo de la actualización.
2. **¿Qué estrategias podrías emplear para evitar conflictos en futuros desarrollos colaborativos?**
	- Siempre trabajar en ramas de características y hacer revisiones de código con pull requests antes de fusionar los cambios a la rama principal.
	- Mantener mi repositorio local siempre actualizado con los últimos cambios antes de empezar a trabajar, así evito trabajar sobre versiones antiguas.
	- Mantener una buena comunicación en equipo, avisando sobre que archivos está trabajando cada uno.
## Ejercicio 5: Comparar los historiales con git log después de diferentes fusiones
### Pasos

1. Se crea un nuevo repositorio y realizamos varios commits en dos ramas

	![[consola5.1.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consola5.1.png?raw=true)

2. Fusionamos `feature-1` usando _fast-forward_

	![[consola5.2.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consola5.2.png?raw=true)

3. Fusionamos `feature-2` usando _non-fast-forward_

	![[consola5.3.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consola5.3.png?raw=true)

	Solucionamos conflictos

	![[versiontxt.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/versiontxt.png?raw=true)

	Completamos la fusión

	![[consola5.4.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consola5.4.png?raw=true)
4. Crea una nueva rama `feature-3` con múltiples commits y fusiónala con _squash_

	![[consola5.5.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consola5.5.png?raw=true)

5. Comparamos el historial de git

	![[consola5.6.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consola5.6.png?raw=true)

	![[consola5.7.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consola5.7.png?raw=true)
### Preguntas
1. **¿Cómo se ve el historial en cada tipo de fusión?**
	- **Fast-forward:** En el historial de fast-forward, no aparece un commit de fusión porque la rama principal avanza directamente al último commit de la rama de características sin crear un commit adicional.
	- **Non-fast-forward:** En el historial de non-fast-forward, se ve un commit de fusión específico que combina las ramas.
	- **Squash:** En el historial de squash, solo se ve un commit único que representa todos los cambios de la rama squash.
2. **¿Qué método prefieres en diferentes escenarios y por qué?**
	- **Fast-forward:** Cuando quiera mantener el historial simple y lineal. Es útil cuando la rama es corta y no necesito conservar el registro de cómo se hizo el trabajo en la rama.
	- **Non-fast-forward:** Cuando sea importante tener un registro de la fusión de ramas, especialmente en proyectos donde necesito seguir el rastro de cómo se integraron los cambios. Esto ayuda a ver claramente cuándo y cómo se combinaron las ramas.
	- **Squash:** Cuando quiera limpiar el historial antes de hacer un merge, combinando múltiples commits en uno solo. Esto es útil para mantener el historial más limpio y fácil de entender, especialmente cuando los commits en la rama de características no aportan mucho valor individualmente (como por ejemplo, este repositorio tiene muchos commits de documentación innecesarios).

## Ejercicio 6: Usando fusiones automáticas y revertir fusiones
### Pasos
1. Inicializamos un nuevo repositorio y realizamos commits en _main_

	![[consola6.1.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consola6.1.png?raw=true)

2. Creamos una nueva rama `auto-merge` y se realiza otro commit en `file.txt`

	![[consola6.2.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consola6.2.png?raw=true)

3. Volvemos a `main` y realizamos cambios no conflictivos en otra parte del archivo

	![[consola6.3.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consola6.3.png?raw=true)

4. Fusionamos la rama `auto-merge` con `main`

	![[consola6.4.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consola6.4.png?raw=true)

	Se presenta un conflicto

	![[conflicto1.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/conflicto1.png?raw=true)

	Solución

	![[conflicto2.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/conflicto2.png?raw=true)

	![[consola6.5.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consola6.5.png?raw=true)

5. Revertimos la fusión

	![[consola6.6.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consola6.6.png?raw=true)

6. Verificamos el historial y el archivo

	![[consola6.7.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consola6.7.png?raw=true)

	![[filetxt.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/filetxt.png?raw=true)

- **¿Qué falló en el auto-merge?**

	Parece que las instrucciones hacían que se escriba 'Linea 3' en la misma línea que 'Footer: Fin del archivo', por lo que ocurría un conflicto a solucionar de forma manual.
### Preguntas

1. **¿Cuándo usarías un comando como `git revert` para deshacer una fusión?**

	Si la fusión resultó en cambios indeseados o errores en el código que no se detectaron a tiempo. También sirve para deshacer cambios de forma segura sin modificar el historial de commits anterior.
2. **¿Qué tan útil es la función de fusión automática en Git?**

	Es muy útil pues facilita fusionar las ramas automáticamente, sin intervención manual, lo que reduce el riesgo de errores humanos; además, se mantiene un historial claro.

## Ejercicio 7: Fusión remota en un repositorio colaborativo

### Pasos
1. Regresamos al repositorio _ejercicio-fusionar_ (no es necesario clonarlo, ya se encuentra localmente). Nos ubicamos en la carpeta:

	![[consola7.1.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consola7.1.png?raw=true)

2. Creamos una nueva rama y realizamos cambios

	![[consola7.2.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consola7.2.png?raw=true)

3. Hacemos push a la rama

	![[consola7.3.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consola7.3.png?raw=true)

4. Simulamos la fusión desde la interfaz de GitHub

	Creamos el pull request

	![[pull-request.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/pull-request.png?raw=true)

	Lo aceptamos

	![[acept-pr.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/acept-pr.png?raw=true)
	![[accept-pr2.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/accept-pr2.png?raw=true)

### Preguntas

1. **¿Cómo cambia la estrategia de fusión cuando colaboras con otras personas en un repositorio remoto?**

	Cuando colaboras en un repositorio remoto, la estrategia de fusión cambia porque:
	
	- **Requiere Coordinación:** Es importante que los colaboradores se aseguren de que no se solapen los cambios entre ellos. Se debe revisar el código antes de fusionar.
	- **Uso de Pull Requests (PRs):** Utilizamos PRs para revisar el código, recibir comentarios y discutir posibles mejoras antes de fusionar los cambios.
	- **Conflictos Más Frecuentes:** Es más común encontrar conflictos cuando múltiples personas trabajan en diferentes ramas y áreas del mismo archivo.

2. **¿Qué problemas comunes pueden surgir al integrar ramas remotas?**

	Los problemas más comunes al integrar ramas remotas incluyen:
	
	- **Conflictos de Fusión:** Cuando dos personas modifican la misma parte del código en diferentes ramas, se generan conflictos que deben ser resueltos manualmente.
	- **Desincronización del Repositorio:** A veces se olvidan de hacer `pull` antes de hacer `push`, lo que provoca errores al intentar empujar cambios sin estar actualizado.

## Ejercicio final: flujo de trabajo completo

Este ejercicio está acompañado de los comandos y capturas.
### 1. Configura un proyecto simulado
- Creamos un directorio y respositorio
	``` shell
	mkdir ejercicio-final
	cd ejercicio-final
	git init
	echo "# Proyecto Ejercicio Final" > README.md 
	git add README.md 
	git commit -m "Agregar README a la rama main"
	```
	![[consolaf1.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consolaf1.png?raw=true)
- Creamos las ramas
	```shell
	git checkout -b feature1
	git checkout -b feature2
	```
	![[consolaf2.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consolaf2.png?raw=true)
- Realizamos cambios en las ramas
	- **feature1**
		```shell
		git checkout feature1
		echo "Feature 1 actualización" > feature1.txt
		git add feature1.txt
		git commit -m "Feature 1 update"
		```
		![[consolaf3.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consolaf3.png?raw=true)
	- **feature2**
		```shell
		git checkout feature2
		echo "Feature 2 actualización" > feature2.txt
		git add feature2.txt
		git commit -m "Feature 2 update"
		```
		![[consolaf4.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consolaf4.png?raw=true)
### 2. Realiza fusiones utilizando diferentes métodos
- Fusiona `feature1` con `main` utilizando **fast-forward**:
	```shell
	git checkout main
	git merge feature1 --ff
	```
	![[consolaf5.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consolaf5.png?raw=true)
- Fusiona `feature2` con `main` utilizando **non-fast-forward**:
	```shell
	git checkout main
	git merge feature2 --no-ff
	```
	![[consolaf6.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consolaf6.png?raw=true)
- Crea una nueva rama `feature3` y realiza múltiples commits, luego fusiónala utilizando **squash**:
	```shell
	git checkout -b feature3
	echo "Feature 3 paso 1" > feature3.txt
	git add feature3.txt
	git commit -m "Feature 3 paso 1"
	
	echo "Feature 3 paso 2" >> feature3.txt
	git add feature3.txt
	git commit -m "Feature 3 paso 2"
	
	git checkout main
	git merge --squash feature3
	git commit -m "Agregar feature 3 en un commit"
	```
	![[consolaf7.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consolaf7.png?raw=true)
	![[consolaf8.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consolaf8.png?raw=true)
### 3. Analiza el historial de commits
- Revisa el historial para entender cómo los diferentes métodos de fusión afectan el árbol de commits.
	```shell
	git log --graph --oneline --all
	```
	![[consolaf9.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%204/imagenes/consolaf9.png?raw=true)
	- **Fast-forward** es más limpio, pero no muestra claramente el desarrollo en ramas.
	- **Non-fast-forward** deja un commit de fusión, ideal para mantener el historial de las ramas.
	- **Squash** compacta el trabajo en un solo commit, útil para mantener un historial limpio sin detalles internos de la rama.
- Compara los resultados y discute con tus compañeros de equipo cuál sería la mejor estrategia de fusión para proyectos más grandes.
	**Pendiente...**