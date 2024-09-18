# Sobre la Actividad

## Documentación
Se presenta una lista detallada de los pasos seguidos y los comandos ejecutados para cada parte, al final de cada una se incluyen capturas de pantalla de la consola para mostrar los resultados obtenidos. En varios casos, se utilizaron comandos adicionales o variantes de los indicados en las instrucciones originales, ya que la actividad no se completaba únicamente con los comandos proporcionados.
## Manejo de repositorios
Dado que se usaban tags en la parte 6, se optó por crear un repositorio separado para gestionar estos elementos. Este repositorio se adjuntó al proyecto principal (CC3S2) mediante submódulos.

---
# Actividad 6

## 1. Inicialización del proyecto y creación de ramas

### Paso 1: Crea un nuevo proyecto en tu máquina local.
```bash
mkdir proyecto-colaborativo
cd proyecto-colaborativo
```

### Paso 2: Inicializa Git en tu proyecto.
```bash
git init
```

### Paso 3: Crea un archivo de texto llamado `archivo_colaborativo.txt` y agrega algún contenido inicial.
```bash
echo "Este es el contenido inicial del proyecto" > archivo_colaborativo.txt
```

### Paso 4: Agrega el archivo al área de staging y haz el primer commit.
```bash
git add .
git commit -m "Commit inicial con contenido base"
```

### Paso 5: Crea dos ramas activas: `main` y `feature-branch`.
```bash
$ git branch feature-branch
```

### Paso 6: Haz checkout a la rama `feature-branch` y realiza un cambio en el archivo `archivo_colaborativo.txt`.
```bash
git checkout feature-branch
echo "Este es un cambio en la feature-branch" >> archivo_colaborativo.txt
git add .
git commit -m "Cambios en feature-branch"
```

### Paso 7: Regresa a la rama `main` y realiza otro cambio en la misma línea del archivo `archivo_colaborativo.txt`.
```bash
git checkout main
echo "Este es un cambio en la rama main" >> archivo_colaborativo.txt
git add .
git commit -m "Cambios en main"
```

### Capturas de pantalla
![[consola1_1.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%206/capturas/consola1_1.png?raw=true)
![[consola1_2.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%206/capturas/consola1_2.png?raw=true)
## 2. Fusión y resolución de conflictos

### Paso 1: Intenta fusionar `feature-branch` en `main`. Se espera que surjan conflictos de fusión.
```bash
git merge feature-branch
```

### Paso 2: Usa `git status` y `git diff` para identificar los archivos en conflicto. Examina los archivos afectados y resuelve manualmente los conflictos.
```bash
git status
git diff
git checkout --theirs archivo_colaborativo.txt
git checkout --ours archivo_colaborativo.txt
```

### Paso 3: Una vez resueltos los conflictos, commitea los archivos y termina la fusión.
```bash
git add .
git commit -m "Conflictos resueltos"
```
### Capturas de pantalla

![[Software/Actividad 6/consola2_1.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%206/capturas/consola2_1.png?raw=true)
![[Software/Actividad 6/consola2_2.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%206/capturas/consola2_2.png?raw=true)
![[Software/Actividad 6/consola2_3.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%206/capturas/consola2_3.png?raw=true)
## 3. Simulación de fusiones y uso de git diff

### Paso 1: Crear una nueva rama para simular la fusion
```bash
git checkout -b feature-branch1
echo "Cambio en feature-branch1" >> archivo_colaborativo.txt
git add .
git commit -m "Cambios en feature-branch1"
```
### Paso 2: Simula una fusión usando `git merge --no-commit --no-ff` para ver cómo se comportarían los cambios antes de realizar el commit.
```bash
git merge --no-commit --no-ff feature-branch
git diff --cached
git commit -m "Fusión de feature-branch1 en main" #Aceptamos el merge
```
### Capturas de pantalla
![[consola3_1.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%206/capturas/consola3_1.png?raw=true)
![[consola3_2.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%206/capturas/consola3_2.png?raw=true)
![[consola3_3.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%206/capturas/consola3_3.png?raw=true)
## 4. Uso de git mergetool
### Paso 1: Creamos ramas y cambios conflictivos entre ramas
```shell
# Crear una nueva rama y cambiar a ella
git checkout -b feature-branch2

# Añadir un cambio conflictivo en la nueva rama
echo "Cambio conflictivo en feature-branch2" >> archivo_colaborativo.txt
git add archivo_colaborativo.txt
git commit -m "Cambio conflictivo en feature-branch2"

# Cambiar a la rama principal
git checkout main

# Añadir un cambio conflictivo en la rama principal
echo "Cambio conflictivo en main" >> archivo_colaborativo.txt
git add archivo_colaborativo.txt
git commit -m "Cambio conflictivo en main"
```

### Paso 2: Configura `git mergetool` con una herramienta de fusión visual (como `meld`, `vimdiff`, o Visual Studio Code).
```bash
git config --global merge.tool vscode
```

### Paso 3: Realiza un `git merge` y soluciona el conflicto con `git mergetool`
```bash
git merge feature-branch2
git mergetool
git commit -m "Conflictos resueltos usando git mergetool"
```
### Capturas de pantalla
![[consola4_1.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%206/capturas/consola4_1.png?raw=true)
![[consola4_2.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%206/capturas/consola4_2.png?raw=true)
![[consola4_3.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%206/capturas/consola4_3.png?raw=true)
![[consola4_4.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%206/capturas/consola4_4.png?raw=true)
![[consola4_5.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%206/capturas/consola4_5.png?raw=true)

## 5. Uso de git revert y git reset
### Paso 1: Realizar commits a revertir
```shell
# Asegurarse de estar en la rama principal
git checkout main

# Añadir un cambio que queremos revertir
echo "Cambio que queremos revertir" >> archivo_colaborativo.txt
git add archivo_colaborativo.txt
git commit -m "Cambio que queremos revertir"

# Añadir otro cambio en la rama principal
echo "Otro cambio más en main" >> archivo_colaborativo.txt
git add archivo_colaborativo.txt
git commit -m "Otro cambio en main"

# Ver el historial de commits
git log --oneline --graph --all
```
### Paso 2: Revertir cambios usando `git revert`
```shell
# Revertir un commit específico
git revert d9191d3

# Resolver conflictos de fusión
git status
# Verifica el estado y resuelve los conflictos en archivo_colaborativo.txt
# Añadir el archivo resuelto
git add archivo_colaborativo.txt

# Continuar con el revert
git revert --continue
```
### Paso 3: Realizar commits para probar `git reset`
```shell
# Primer cambio simulado
echo "\n## Primer Cambio\n\nDetalles adicionales." >> INSTRUCCIONES.txt
git add INSTRUCCIONES.txt
git commit -m "Primer cambio en INSTRUCCIONES.txt"

# Segundo cambio simulado
echo "\n## Segundo Cambio\n\nMás detalles agregados." >> INSTRUCCIONES.txt
git add INSTRUCCIONES.txt
git commit -m "Segundo cambio en INSTRUCCIONES.txt"
```
### Paso 4: Probar `git reset --mixed`

```shell
# Aplicar reset --mixed 
git reset --mixed HEAD~1 
# Verificar el estado del repositorio
git status 
# Volver a hacer commit 
git add INSTRUCCIONES.txt git commit -m "Rehacer el segundo cambio"
```
### Capturas de pantalla
![[consola5_1.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%206/capturas/consola5_1.png?raw=true)
![[consola5_2.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%206/capturas/consola5_2.png?raw=true)
![[consola5_3.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%206/capturas/consola5_3.png?raw=true)
![[consola5_4.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%206/capturas/consola5_4.png?raw=true)
![[consola5_5.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%206/capturas/consola5_5.png?raw=true)
![[consola5_6.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%206/capturas/consola5_6.png?raw=true)
## 6. Versionado semántico y etiquetado
### Paso 1: Aplica versionado semántico al proyecto utilizando tags para marcar versiones importantes.
```shell
git tag -a v1.0.0 -m "Primera versión estable"
git push origin v1.0.0
```
### Capturas de pantalla
![[consola6_1.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%206/capturas/consola6_1.png?raw=true)
![[consola6_2.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%206/capturas/consola6_2.png?raw=true)
![[consola6_3.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%206/capturas/consola6_3.png?raw=true)
## 7. Aplicación de `git bisect` para depuración

### Paso 1: Realizamos commits para el ejercicio
```shell
# Crea un archivo feature.txt con contenido inicial 
echo "Contenido inicial del archivo feature.txt" > feature.txt 
git add feature.txt 
git commit -m "Commit inicial con feature.txt"

# Crear un cambio bueno en feature.txt
echo "\n## Cambios buenos\n\nEste commit no introduce errores." >> feature.txt
git add feature.txt
git commit -m "Cambios buenos en feature.txt"

# Crear un cambio malo en feature.txt
echo "\n## Cambios malos\n\nEste commit introduce un error." >> feature.txt
git add feature.txt
git commit -m "Cambios malos en feature.txt"

# Crear un cambio intermedio en feature.txt
echo "\n## Cambios intermedios\n\nEste commit está entre los buenos y malos." >> feature.txt
git add feature.txt
git commit -m "Cambios intermedios en feature.txt"
```

### Paso 2:  Usa git bisect para identificar el commit que introdujo un error en el código
```shell
git bisect start
git bisect bad # Indica que la versión actual tiene un error
git bisect good 513114d
# Continúa marcando como "good" o "bad" hasta encontrar el commit que introdujo el error
git bisect reset
```
### Capturas de pantalla
![[consola7_1.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%206/capturas/consola7_1.png?raw=true)

---
# Preguntas

## 1. Ejercicio para `git checkout --ours` y `git checkout --theirs`

**Contexto:** En un sprint ágil, dos equipos están trabajando en diferentes ramas. Se produce un conflicto de fusión en un archivo de configuración crucial. El equipo A quiere mantener sus cambios mientras el equipo B solo quiere conservar los suyos. El proceso de entrega continua está detenido debido a este conflicto.

**Pregunta:**
- ¿Cómo utilizarías los comandos `git checkout --ours` y `git checkout --theirs` para resolver este conflicto de manera rápida y eficiente? Explica cuándo preferirías usar cada uno de estos comandos y cómo impacta en la pipeline de CI/CD. ¿Cómo te asegurarías de que la resolución elegida no comprometa la calidad del código?
	
	Primero vería las diferencias entre ambas ramas (llamémoslas A y B), una forma de hacerlo es mediante `git diff`. Tras analizar los conflictos de ambas ramas, si lo que se quiere es solucionarlo de forma rápida y eficiente; para cada archivo decidiría si mantener la versión de la rama A o B , es aquí donde empleamos `git checkout --ours` o `git checkout --theirs`.
	
	Al elegir qué cambios mantener, estamos decidiendo cómo se integran esos cambios en el código base. Usar uno u otro comando puede afectar la funcionalidad del proyecto si no se hace con cuidado. Es crucial asegurarse de que la resolución del conflicto no comprometa la calidad del código. Para esto, deberíamos ejecutar las pruebas automatizadas de la pipeline después de resolver el conflicto para garantizar que todo funcione correctamente y que no se hayan introducido errores nuevos.
	
	Si los cambios de una rama traen conflictos, se puede utilizar `revert` o `reset` y conservar los cambios de la otra rama.

## 2. Ejercicio para `git diff`

**Contexto:** Durante una revisión de código en un entorno ágil, se observa que un pull request tiene una gran cantidad de cambios, muchos de los cuales no están relacionados con la funcionalidad principal. Estos cambios podrían generar conflictos con otras ramas en la pipeline de CI/CD.

**Pregunta:**
- Utilizando el comando `git diff`, ¿cómo compararías los cambios entre ramas para identificar diferencias específicas en archivos críticos? Explica cómo podrías utilizar `git diff feature-branch..main` para detectar posibles conflictos antes de realizar una fusión y cómo esto contribuye a mantener la estabilidad en un entorno ágil con CI/CD.
	
	Podría usar el comando `git diff feature-branch..main` para identificar las diferencias específicas entre estas dos ramas. Este comando me permitirá ver en detalle qué archivos se han modificado y cómo han cambiado desde el último punto en común. Esto me permite tomar decisiones informadas sobre qué cambios deben integrarse y cuáles podrían necesitar más revisión o ser excluidos.
	
	Usar `git diff` de esta manera ayuda a detectar posibles conflictos antes de realizar una fusión, lo cual es esencial para mantener la estabilidad en un entorno ágil con CI/CD. Al hacer esto, puedo asegurarme de que los cambios que se están introduciendo no rompan la funcionalidad existente, minimizando el riesgo de problemas durante la entrega continua.

## 3. Ejercicio para `git merge --no-commit --no-ff`

**Contexto:** En un proyecto ágil con CI/CD, tu equipo quiere simular una fusión entre una rama de desarrollo y la rama principal para ver cómo se comporta el código sin comprometerlo inmediatamente en el repositorio. Esto es útil para identificar posibles problemas antes de completar la fusión.

**Pregunta:**
- Describe cómo usarías el comando `git merge --no-commit --no-ff` para simular una fusión en tu rama local. ¿Qué ventajas tiene esta práctica en un flujo de trabajo ágil con CI/CD, y cómo ayuda a minimizar errores antes de hacer commits definitivos? ¿Cómo automatizarías este paso dentro de una pipeline CI/CD?
	
	Para simular una fusión sin comprometer los cambios de inmediato, usaría el comando `git merge --no-commit --no-ff`. Esto me permite revisar los cambios que se introducirán y detectar posibles conflictos o problemas antes de realizar el commit definitivo.
	
	La ventaja de esta práctica es que me da la oportunidad de verificar cómo se comportará el código después de la fusión sin hacer cambios permanentes en el repositorio. Esto ayuda a identificar y solucionar problemas antes de hacer el commit, lo cual es crucial para mantener un flujo de trabajo ágil con CI/CD.
	
	Para automatizar este paso en una pipeline CI/CD, podría configurar un paso en el pipeline que ejecute el merge simulado y luego ejecute pruebas automatizadas. Si todo está en orden, el paso de merge real se puede proceder; si hay problemas, se pueden corregir antes de finalizar el merge.

## 4. Ejercicio para `git mergetool`

**Contexto:** Tu equipo de desarrollo utiliza herramientas gráficas para resolver conflictos de manera colaborativa. Algunos desarrolladores prefieren herramientas como vimdiff o Visual Studio Code. En medio de un sprint, varios archivos están en conflicto y los desarrolladores prefieren trabajar en un entorno visual para resolverlos.

**Pregunta:**
- Explica cómo configurarías y utilizarías `git mergetool` en tu equipo para integrar herramientas gráficas que faciliten la resolución de conflictos. ¿Qué impacto tiene el uso de `git mergetool` en un entorno de trabajo ágil con CI/CD, y cómo aseguras que todos los miembros del equipo mantengan consistencia en las resoluciones?
	
	Se puede configurar usando el comando `git config --global merge.tool <nombre-herramienta>`. 
	El uso de `git mergetool` en un entorno ágil con CI/CD mejora la eficiencia en la resolución de conflictos y asegura que los cambios sean revisados cuidadosamente. Para asegurar que todos los miembros del equipo mantengan consistencia en las resoluciones, es importante que todos utilicen la misma configuración de `git mergetool`.
## 5. Ejercicio para `git reset`

**Contexto:** En un proyecto ágil, un desarrollador ha hecho un commit que rompe la pipeline de CI/CD. Se debe revertir el commit, pero se necesita hacerlo de manera que se mantenga el código en el directorio de trabajo sin deshacer los cambios.

**Pregunta:**
- Explica las diferencias entre `git reset --soft`, `git reset --mixed` y `git reset --hard`. ¿En qué escenarios dentro de un flujo de trabajo ágil con CI/CD utilizarías cada uno? Describe un caso en el que usarías `git reset --mixed` para corregir un commit sin perder los cambios no commiteados y cómo afecta esto a la pipeline.
	
	Si el objetivo es revertir un commit que rompió la pipeline sin perder los cambios en el directorio de trabajo, lo ideal sería utilizar `git reset --mixed`. Este comando deshace el commit, pero mantiene los cambios en el _working directory_, lo que permite corregir el código o realizar modificaciones sin perder el progreso hecho antes del commit problemático.
	
	La diferencia entre los tipos de `git reset`es qué parte del repositorio se afecta: `--soft` mantiene los cambios en el área de preparación (_staging area_), `--mixed` los mueve al directorio de trabajo, y `--hard` descarta todos los cambios.
	
	Supongamos que he agregado algunos archivos y hecho modificaciones, pero no ejecuté las pruebas adecuadas o cometí un error que rompe la funcionalidad. El commit ya está hecho, pero quiero corregir el error sin perder los cambios que he introducido. En este caso es ideal el uso de `git reset --mixed`, esto me permite revisar el código, corregir el error y volver a hacer un commit. Este enfoque permite que la pipeline se recupere más rápido porque no se necesita revertir múltiples commits ni realizar cambios drásticos en el historial; además, el commit defectuoso nunca llega a ser fusionado en la rama principal o desplegado.

## 6. Ejercicio para `git revert`

**Contexto:** En un entorno de CI/CD, tu equipo ha desplegado una característica a producción, pero se ha detectado un bug crítico. La rama principal debe revertirse para restaurar la estabilidad, pero no puedes modificar el historial de commits debido a las políticas del equipo.

**Pregunta:**
- Explica cómo utilizarías `git revert` para deshacer los cambios sin modificar el historial de commits. ¿Cómo te aseguras de que esta acción no afecte la pipeline de CI/CD y permita una rápida recuperación del sistema? Proporciona un ejemplo detallado de cómo revertirías varios commits consecutivos.
	
	Usaría `git revert` para deshacer los cambios sin alterar el historial. Este comando crea un nuevo commit que revierte los cambios hechos por un commit anterior, preservando la trazabilidad y cumpliendo con las políticas del equipo. La pipeline de CI/CD puede seguir operando de manera segura, ya que los cambios quedan documentados en nuevos commits y no se alteran los commits anteriores.
	
	Para revertir varios commits consecutivo, lo haría en el orden inverso al que fueron aplicados, esto evita problemas como los que me ocurrieron en  la parte 5, cuando intenté revertir defrente el antepenultimo commit y tuve que solucionar conflictos manualmente.

## 7. Ejercicio para `git stash`

**Contexto:** En un entorno ágil, tu equipo está trabajando en una corrección de errores urgente mientras tienes cambios no guardados en tu directorio de trabajo que aún no están listos para ser committeados. Sin embargo, necesitas cambiar rápidamente a una rama de hotfix para trabajar en la corrección.

**Pregunta:**
- Explica cómo utilizarías `git stash` para guardar temporalmente tus cambios y volver a ellos después de haber terminado el hotfix. ¿Qué impacto tiene el uso de `git stash` en un flujo de trabajo ágil con CI/CD cuando trabajas en múltiples tareas? ¿Cómo podrías automatizar el proceso de stashing dentro de una pipeline CI/CD?
	
	Para guardar temporalmente cambios sin comprometerlos y cambiar de rama, usaría `git stash`. Una vez solucionado el problema, volvería a la rama original y aplicaría los cambios guardados con `git stash pop`.
	
	En un flujo de trabajo ágil con CI/CD, esto es crucial cuando se trabaja en múltiples tareas y necesitas hacer un cambio rápido en otra rama sin afectar el desarrollo actual. Se puede automatizar este proceso integrando comandos como `git stash` en la pipeline.

## 8. Ejercicio para `.gitignore`

**Contexto:** Tu equipo de desarrollo ágil está trabajando en varios entornos locales con configuraciones diferentes (archivos de logs, configuraciones personales). Estos archivos no deberían ser parte del control de versiones para evitar confusiones en la pipeline de CI/CD.

**Pregunta:**
- Diseña un archivo `.gitignore` que excluya archivos innecesarios en un entorno ágil de desarrollo. Explica por qué es importante mantener este archivo actualizado en un equipo colaborativo que utiliza CI/CD y cómo afecta la calidad y limpieza del código compartido en el repositorio.
	
	Un ejemplo de un `.gitignore` para IntelliJ IDEA:
	```
	# Archivos de configuración del IDE IntelliJ IDEA
	.idea/
	*.iws
	*.iml
	*.ipr
	
	# Directorios de compilación
	out/
	target/
	
	# Archivos temporales de sistema
	.DS_Store
	Thumbs.db
	
	# Archivos de log
	*.log
	```
	
	Mantener este archivo `.gitignore` actualizado es crucial en un equipo colaborativo que utiliza CI/CD. Asegura que solo los archivos necesarios sean versionados, manteniendo el repositorio limpio y manejable, un ejemplo de su importancia es el repositorio donde me encuentro (CC3S2) pues por no usar un .gitignore las **Actividades 1 y 2** tienen muchos archivos innecesarios.

---
## Adicional

### Ejercicio 1: Resolución de conflictos en un entorno ágil

**Contexto:**
Estás trabajando en un proyecto ágil donde múltiples desarrolladores están enviando cambios a la rama principal cada día. Durante una integración continua, se detectan conflictos de fusión entre las ramas de dos equipos que están trabajando en dos funcionalidades críticas. Ambos equipos han modificado el mismo archivo de configuración del proyecto.

**Pregunta:**
- ¿Cómo gestionarías la resolución de este conflicto de manera eficiente utilizando Git y manteniendo la entrega continua sin interrupciones? ¿Qué pasos seguirías para minimizar el impacto en la CI/CD y asegurar que el código final sea estable?
	
	Utilizaría `git status` para ver los archivos en conflicto y `git diff` para entender las diferencias. Luego, resolvería los conflictos manualmente o con herramientas de merge. Una vez que los conflictos están resueltos, se realizaría un commit de la resolución. 
	Para minimizar el impacto en la CI/CD, se ejecutarían las pruebas automatizadas después de la fusión para verificar que el código es estable y funcional.

### Ejercicio 2: Rebase vs. Merge en integraciones ágiles

**Contexto:**
En tu equipo de desarrollo ágil, cada sprint incluye la integración de varias ramas de características. Algunos miembros del equipo prefieren realizar merge para mantener el historial completo de commits, mientras que otros prefieren rebase para mantener un historial lineal.

**Pregunta:**
- ¿Qué ventajas y desventajas presenta cada enfoque (merge vs. rebase) en el contexto de la metodología ágil? ¿Cómo impacta esto en la revisión de código, CI/CD, y en la identificación rápida de errores?
	
	El `merge` mantiene el historial completo de commits, lo que puede ser útil para rastrear el historial del proyecto y entender el contexto completo de los cambios. Sin embargo, puede resultar en un historial más complejo con múltiples ramas y commits de merge. Por otro lado, `rebase` simplifica el historial al integrar cambios de una rama en otra y aplicar los commits de una rama sobre la base de la otra. Esto resulta en un historial lineal, lo que facilita la lectura y el entendimiento.
	
	Un historial lineal puede hacer que el análisis de errores sea más fácil y que las integraciones sean más limpias, mientras que los merges pueden ser útiles para preservar la historia completa de las contribuciones.

### Ejercicio 3: Git Hooks en un flujo de trabajo CI/CD ágil

**Contexto:**
Tu equipo está utilizando Git y una pipeline de CI/CD que incluye tests unitarios, integración continua y despliegues automatizados. Sin embargo, algunos desarrolladores accidentalmente comiten código que no pasa los tests locales o no sigue las convenciones de estilo definidas por el equipo.

**Pregunta:**
- Diseña un conjunto de Git Hooks que ayudaría a mitigar estos problemas, integrando validaciones de estilo y tests automáticos antes de permitir los commits. Explica qué tipo de validaciones implementarías y cómo se relaciona esto con la calidad del código y la entrega continua en un entorno ágil.

### Ejercicio 4: Estrategias de branching en metodologías ágiles

**Contexto:**
Tu equipo de desarrollo sigue una metodología ágil y está utilizando Git Flow para gestionar el ciclo de vida de las ramas. Sin embargo, a medida que el equipo ha crecido, la gestión de las ramas se ha vuelto más compleja, lo que ha provocado retrasos en la integración y conflictos de fusión frecuentes.

**Pregunta:**
- Explica cómo adaptarías o modificarías la estrategia de branching para optimizar el flujo de trabajo del equipo en un entorno ágil y con integración continua. Considera cómo podrías integrar feature branches, release branches y hotfix branches de manera que apoyen la entrega continua y minimicen conflictos.

### Ejercicio 5: Automatización de reversiones con Git en CI/CD

**Contexto:**
Durante una integración continua en tu pipeline de CI/CD, se detecta un bug crítico después de haber fusionado varios commits a la rama principal. El equipo necesita revertir los cambios rápidamente para mantener la estabilidad del sistema.

**Pregunta:**
- ¿Cómo diseñarías un proceso automatizado con Git y CI/CD que permita revertir cambios de manera eficiente y segura? Describe cómo podrías integrar comandos como `git revert` o `git reset` en la pipeline y cuáles serían los pasos para garantizar que los bugs se reviertan sin afectar el desarrollo en curso.

