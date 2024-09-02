# Índice

1. [Conceptos básicos de Git](#conceptos-básicos-de-git)
   1. [Git config: Preséntate a Git](#1-git-config-preséntate-a-git)
   2. [git init: Donde comienza tu viaje de código](#2-git-init-donde-comienza-tu-viaje-de-código)
   3. [git add: Preparando tu código](#3-git-add-preparando-tu-código)
   4. [git commit: Registra cambios](#4-git-commit-registra-cambios)
   5. [git log: Recorrer el árbol de commits](#5-git-log-recorrer-el-árbol-de-commits)
   6. [git branch: Entendiendo los conceptos básicos de Git branch](#6-git-branch-entendiendo-los-conceptos-básicos-de-git-branch)
   7. [git checkout/git switch: Cambiar entre branches](#7-git-checkoutgit-switch-cambiar-entre-branches)
   8. [git merge: Fusionando branches y git branch -d: Eliminando una Branch](#8-git-merge-fusionando-branches-y-git-branch--d-eliminando-una-branch)
3. [Preguntas](#preguntas)
4. [Ejercicios](#ejercicios)
   1. [Ejercicio 1: Manejo avanzado de branches y resolución de conflictos](#ejercicio-1-manejo-avanzado-de-branches-y-resolución-de-conflictos)
   2. [Ejercicio 2: Exploración y manipulación del historial de commits](#ejercicio-2-exploración-y-manipulación-del-historial-de-commits)
   3. [Ejercicio 3: Creación y gestión de branches desde commits específicos](#ejercicio-3-creación-y-gestión-de-branches-desde-commits-específicos)
   4. [Ejercicio 4: Manipulación y restauración de commits con git reset y git restore](#ejercicio-4-manipulación-y-restauración-de-commits-con-git-reset-y-git-restore)
   5. [Ejercicio 5: Trabajo colaborativo y manejo de Pull Requests](#ejercicio-5-trabajo-colaborativo-y-manejo-de-pull-requests)
   6. [Ejercicio 6: Cherry-Picking y Git Stash](#ejercicio-6-cherry-picking-y-git-stash)


# Conceptos básicos de Git

En esta sección se siguen los pasos de la actividad 3 y al final se suben a GitHub.
## 1. Git config: Preséntate a Git

![git config](https://github.com/user-attachments/assets/c9324f6e-c3c8-4499-883e-6fb790ece430)

## 2. git init: Donde comienza tu viaje de código

![init](https://github.com/user-attachments/assets/63a6acfb-c543-458c-b801-c5467d2d6fbd)

## 3. git add: Preparando tu código

![add](https://github.com/user-attachments/assets/eabaa9e8-25d0-4c4f-afdf-a54e4595b574)

## 4. git commit: registra cambios

![commit](https://github.com/user-attachments/assets/cd5e6d95-eec0-4bf9-8468-0be4bb0f6a59)

## 5. git log: Recorrer el árbol de commits

![formato](https://github.com/user-attachments/assets/9f8a0e86-40ac-46da-86fd-25c68443b4fc)

Pregunta: ¿ Cual es la salida de este comando?

En un repositorio con branches podría tener una salida como la siguiente:

``` bash
*  f9d7baf 2 hours ago ("Jorge Barriga") Initial commit
*  c4e50a9 1 day ago  ("Jorge Barriga") Added new feature
|\
| *  d3d2e2a 2 days ago ("Alonso Barriga") Merged branch 'feature'
|/
*  e1d9c0a 3 days ago ("Jorge Barriga") Updated README.md

```
## 6. git branch: Entendiendo los conceptos básicos de Git branch

![log2](https://github.com/user-attachments/assets/9cb38723-ae02-4e13-88b5-1f84b8eed71b)

## 7. git checkout/git switch: Cambiar entre branches

![branch 1](https://github.com/user-attachments/assets/38d05feb-ab2d-4bc6-9f79-7cad76b15517)

## 8. git merge: Fusionando branches y git branch -d: Eliminando una Branch

![branch 2](https://github.com/user-attachments/assets/91cdd9ca-d871-44be-91ad-3e5ffc4c0770)

---
# Preguntas

**• Pregunta 1: ¿Cómo te ha ayudado Git a mantener un historial claro y organizado de tus cambios?**

Git me ayuda a mantener un historial claro de mis cambios al permitirme hacer un seguimiento detallado de cada modificación. Cada commit representa un paso en el desarrollo, con un mensaje que describe el cambio. Esto me permite revisar y entender el progreso del proyecto.

---

**• Pregunta 2: ¿Qué beneficios ves en el uso de branches para desarrollar nuevas características o corregir errores?**

El uso de branches en Git me permite trabajar en una copia aislada del código base, evitando afectar el resto del proyecto. Esto es útil para desarrollar nuevas funcionalidades o probar soluciones sin riesgo. Las ramas también facilitan la colaboración en equipo, permitiendo trabajar en ramas separadas y fusionar cambios de manera controlada.

---

**• Pregunta 3: Realiza una revisión final del historial de commits para asegurarte de que todos los cambios se han registrado correctamente.**


![commits-revision](https://github.com/user-attachments/assets/b8d34155-1621-4ce8-8ab4-cd0aab1657fe)

---

**• Pregunta 4: Revisa el uso de branches y merges para ver cómo Git maneja múltiples líneas de desarrollo**

Durante los ejercicios que resolveré a continuación, estaremos manejando y respondiendo mejor a esta pregunta. 

---
# Ejercicios

# Ejercicio 1: Manejo avanzado de branches y resolución de conflictos

## Objetivo:
Practicar la creación, fusión y eliminación de ramas, así como la resolución de conflictos que puedan surgir durante la fusión.

## Instrucciones:

### 1. Crear una nueva rama para una característica:
- Crea una nueva rama llamada `feature/advanced-feature` desde la rama `main`:

    ```bash
    $ git branch feature/advanced-feature
    $ git checkout feature/advanced-feature
    ```
    ![ej1-1](https://github.com/user-attachments/assets/7159a50d-c027-4b12-8455-58c91ecf6e11)

### 2. Modificar archivos en la nueva rama:
- Edita el archivo `main.py` para incluir una función adicional:

    ```python
    def greet():
        print('Hello from advanced feature')

    greet()
    ```

- Añade y confirma estos cambios en la rama `feature/advanced-feature`:

    ```bash
    $ git add main.py
    $ git commit -m "Add greet function in advanced feature"
    ```
    ![ej1-2](https://github.com/user-attachments/assets/a0c29163-0187-40c9-b27e-507ed2d0c13d)

### 3. Simular un desarrollo paralelo en la rama `main`:
- Cambia de nuevo a la rama `main`:

    ```bash
    $ git checkout main
    ```

- Edita el archivo `main.py` de forma diferente (por ejemplo, cambia el mensaje del `print` original):

    ```python
    print('Hello World - updated in main')
    ```

- Añade y confirma estos cambios en la rama `main`:

    ```bash
    $ git add main.py
    $ git commit -m "Update main.py message in main branch"
    ```
    ![ej1-3](https://github.com/user-attachments/assets/b806a597-609b-4277-a368-434afbb0dea3)

### 4. Intentar fusionar la rama `feature/advanced-feature` en `main`:
- Fusiona la rama `feature/advanced-feature` en `main`:

    ```bash
    $ git merge feature/advanced-feature
    ```
    ![ej1-4](https://github.com/user-attachments/assets/8e3057e4-f3c9-4042-a288-f356d84c138b)

### 5. Resolver el conflicto de fusión:
- Git generará un conflicto en `main.py`. Abre el archivo y resuelve el conflicto manualmente, eligiendo cómo combinar las dos versiones.
- Después de resolver el conflicto, añade el archivo resuelto y completa la fusión:

    ```bash
    $ git add main.py
    $ git commit -m "Resolve merge conflict between main and feature/advanced-feature"
    ```

**main.py durante conflicto:**
```python
<<<<<<< HEAD
print('Hello World - updated in main')
=======
def greet():
    print('Hello from advanced feature')
greet()
>>>>>>> feature/advanced-feature
```
**main.py con conflicto resuelto:**
```python
print('Hello World - updated in main')

def greet():
    print('Hello from advanced feature')
greet()

```
![ej1-5](https://github.com/user-attachments/assets/a6887819-3d6f-4eec-ade4-ba87458e2d20)

### 6. Eliminar la rama fusionada:
- Una vez que hayas fusionado con éxito y resuelto los conflictos, elimina la rama `feature/advanced-feature`:

    ```bash
    $ git branch -d feature/advanced-feature
    ```

![ej1-7](https://github.com/user-attachments/assets/387a6bda-92be-415f-8254-855799efce0e)

# Ejercicio 2: Exploración y manipulación del historial de commits

**Objetivo:** Aprender a navegar y manipular el historial de commits usando comandos avanzados de Git.

## Instrucciones:

1. **Ver el historial detallado de commits:**
   - Usa el comando `git log` para explorar el historial de commits, pero esta vez con más detalle:
     ```bash
     $ git log -p
     ```
     ![ej2-1](https://github.com/user-attachments/assets/aa77736f-8345-4389-bd01-4b6c7e35596d)

   - Examina las diferencias introducidas en cada commit. ¿Qué cambios fueron realizados en cada uno?
	   El comando git log -p muestra el historial de commits con los cambios específicos que cada uno introdujo en los archivos del proyecto. Proporciona:

		- La lista de commits con información básica (hash, autor, fecha, mensaje)
    
		- Las diferencias o "diffs" de cada commit, incluyendo líneas añadidas (+) y eliminadas (-)

2. **Filtrar commits por autor:**
   - Usa el siguiente comando para mostrar solo los commits realizados por un autor específico:
     ```bash
     $ git log --author="al-2100"
     ```
     Por ejemplo:
     ![ej2-2](https://github.com/user-attachments/assets/f3468576-f9ee-418c-929a-5073bf47bfff)

3. **Revertir un commit:**
   - Imagina que el commit más reciente en `main.py` no debería haberse hecho. Usa `git revert` para revertir ese commit:
     ```bash
     $ git revert HEAD
     ```
   - Verifica que el commit de reversión ha sido añadido correctamente al historial.
     ![ej2-3](https://github.com/user-attachments/assets/6c2484aa-aa2c-41e2-8063-0f827d1f50e6)

4. **Rebase interactivo:**
   - Realiza un rebase interactivo para combinar varios commits en uno solo. Esto es útil para limpiar el historial de commits antes de una fusión.
   - Usa el siguiente comando para empezar el rebase interactivo:
     ```bash
     $ git rebase -i HEAD~3
     ```
     ![ej2-4](https://github.com/user-attachments/assets/59398a48-5d92-41a2-bf29-bbc000ca75d3)
   - En el editor que se abre, combina los últimos tres commits en uno solo utilizando la opción `squash`.
     ![ej2-5](https://github.com/user-attachments/assets/238f0688-a998-4919-b070-a0498e5c89dd)
     
     ![ej2-6](https://github.com/user-attachments/assets/681a22a4-74da-49ec-83c6-3cc265ca2ada)

5. **Visualización gráfica del historial:**
   - Usa el siguiente comando para ver una representación gráfica del historial de commits:
     ```bash
     $ git log --graph --oneline --all
     ```
	   ![ej2-7](https://github.com/user-attachments/assets/7b52ee5b-b395-4bf3-853b-fffa0e96b549)

   - Reflexiona sobre cómo el historial de tu proyecto se visualiza en este formato. ¿Qué información adicional puedes inferir?

     La representación gráfica nos permite ver todos los cambios de forma más simple a la vista. Esto nos permite hacerle seguimiento a las mejoras, correcciones y cambios significativos, y entender cómo los diferentes colaboradores han contribuido al proyecto.
     En este caso no se muestra el ejercicio 1 donde se hizo la fusión de ramas, pues experimentando con rebase por casualidad terminé eliminando todo ese historial.

# Ejercicio 3: Creación y gestión de branches desde commits específicos

## Objetivo
Practicar la creación de ramas desde commits específicos y comprender cómo Git maneja las referencias históricas.

## Instrucciones

1. **Crear una nueva rama desde un commit específico:**
   - Usa el historial de commits para identificar un commit antiguo desde el cual crear una nueva rama:
     ```bash
     $ git log --oneline
     ```
   - Crea una nueva rama `bugfix/rollback-feature` desde ese commit:
     ```bash
     $ git branch bugfix/rollback-feature <commit-hash>
     $ git checkout bugfix/rollback-feature
     ```
     ![3-1](https://github.com/user-attachments/assets/01488b75-98a3-491a-9e70-895d63cab36f)

2. **Modificar y confirmar cambios en la nueva rama:**
   - Realiza algunas modificaciones en `main.py` que simulen una corrección de errores:
     ```python
     def greet():
         print('Fixed bug in feature')
     ```
   - Añade y confirma los cambios en la nueva rama:
     ```bash
     $ git add main.py
     $ git commit -m "Fix bug in rollback feature"
     ```
     ![3-2](https://github.com/user-attachments/assets/2f1bf4f4-b3aa-4ddc-8dd8-7fece31cac6b)

3. **Fusionar los cambios en la rama principal:**
   - Cambia de nuevo a la rama `main` y fusiona la rama `bugfix/rollback-feature`:
     ```bash
     $ git checkout main
     $ git merge bugfix/rollback-feature
     ```

4. **Explorar el historial después de la fusión:**
   - Usa `git log` y `git log --graph` para ver cómo se ha integrado el commit en el historial:
     ```bash
     $ git log --graph --oneline
     ```
     ![3-3](https://github.com/user-attachments/assets/37377b08-c214-4478-bb47-10b68e236c69)

5. **Eliminar la rama `bugfix/rollback-feature`:**
   - Una vez fusionados los cambios, elimina la rama `bugfix/rollback-feature`:
     ```bash
     $ git branch -d bugfix/rollback-feature
     ```

# Ejercicio 4: Manipulación y restauración de commits con `git reset` y `git restore`

## Objetivo
Comprender cómo usar `git reset` y `git restore` para deshacer cambios en el historial y en el área de trabajo.

## Instrucciones

1. **Hacer cambios en el archivo `main.py`:**
   - Edita el archivo `main.py` para introducir un nuevo cambio:
     ```python
     print('This change will be reset')
     ```
   - Añade y confirma los cambios:
     ```bash
     $ git add main.py
     $ git commit -m "Introduce a change to be reset"
     ```

2. **Usar `git reset` para deshacer el commit:**
   - Deshaz el commit utilizando `git reset` para volver al estado anterior:
     ```bash
     $ git reset --hard HEAD~1
     ```
   - Verifica que el commit ha sido eliminado del historial y que el archivo ha vuelto a su estado anterior.

     ![4-1](https://github.com/user-attachments/assets/1d554aeb-cbc2-4921-adbb-4908ce152083)

3. **Usar `git restore` para deshacer cambios no confirmados:**
   - Realiza un cambio en `README.md` y no lo confirmes:
     ```bash
     $ echo "Another line in README" >> README.md
     $ git status
     ```
   - Usa `git restore` para deshacer este cambio no confirmado:
     ```bash
     $ git restore README.md
     ```
   - Verifica que el cambio no confirmado ha sido revertido.

     ![4-2](https://github.com/user-attachments/assets/db33b449-88fe-4ff4-a610-aa87ffea9560)

# Ejercicio 5: Trabajo colaborativo y manejo de Pull Requests

## Objetivo
Simular un flujo de trabajo colaborativo utilizando ramas y pull requests.
## Instrucciones

1. **Crear un nuevo repositorio remoto:**
   - Usa GitHub o GitLab para crear un nuevo repositorio remoto y clónalo localmente:
     ```bash
     $ git clone https://github.com/al-2100/Actividad3-Ejercicio5.git
     ```

2. **Crear una nueva rama para desarrollo de una característica:**
   - En tu repositorio local, crea una nueva rama `feature/team-feature`:
     ```bash
     $ git branch feature/team-feature
     $ git checkout feature/team-feature
     ```

3. **Realizar cambios y enviar la rama al repositorio remoto:**
   - Realiza cambios en los archivos del proyecto y confírmalos:
     ```bash
     $ echo "print('Collaboration is key!')" > collaboration.py
     $ git add .
     $ git commit -m "Add collaboration script"
     ```
   - Envía la rama al repositorio remoto:
     ```bash
     $ git push origin feature/team-feature
     ```

4. **Abrir un Pull Request:**
   - Abre un Pull Request (PR) en la plataforma remota (GitHub/GitLab) para fusionar `feature/team-feature` con la rama `main`.
   - Añade una descripción detallada del PR, explicando los cambios realizados y su propósito.

     ![5-1](https://github.com/user-attachments/assets/954e10c0-3afb-4804-a3c3-2ed39e1e1883)

5. **Revisar y Fusionar el Pull Request:**
   - Simula la revisión de código, comenta en el PR y realiza cualquier cambio necesario basado en la retroalimentación.
   - Una vez aprobado, fusiona el PR en la rama `main`.

     ![5-2](https://github.com/user-attachments/assets/9864af8d-2bfe-4380-9473-f6e70e05e435)

6. **Eliminar la rama remota y local:**
   - Después de la fusión, elimina la rama tanto local como remotamente:
     ```bash
     $ git branch -d feature/team-feature
     $ git push origin --delete feature/team-feature
     ```
     ![5-3](https://github.com/user-attachments/assets/f32b2440-507e-4a5a-84d3-3faddd2b58e2)

## Ejercicio 6: Cherry-Picking y Git Stash

**Objetivo:** Aprender a aplicar commits específicos a otra rama utilizando `git cherry-pick` y a guardar temporalmente cambios no confirmados utilizando `git stash`.

### Instrucciones:

1. **Hacer cambios en `main.py` y confirmarlos:**
   - Realiza y confirma varios cambios en `main.py` en la rama `main`:
     ```bash
     $ echo "print('Cherry pick this!')" >> main.py
     $ git add main.py
     $ git commit -m "Add cherry-pick example"
     ```

2. **Crear una nueva rama y aplicar el commit específico:**
   - Crea una nueva rama `feature/cherry-pick` y aplícale el commit específico:
     ```bash
     $ git branch feature/cherry-pick
     $ git checkout feature/cherry-pick
     $ git cherry-pick <commit-hash>
     ```

3. **Guardar temporalmente cambios no confirmados:**
   - Realiza algunos cambios en `main.py` pero no los confirmes:
     ```bash
     $ echo "This change is stashed" >> main.py
     $ git status
     ```
   - Guarda temporalmente estos cambios utilizando `git stash`:
     ```bash
     $ git stash
     ```

4. **Aplicar los cambios guardados:**
   - Realiza otros cambios y confírmalos si es necesario.
   - Luego, recupera los cambios guardados anteriormente:
     ```bash
     $ git stash pop
     ```

5. **Revisar el historial y confirmar la correcta aplicación de los cambios:**
   - Usa `git log` para revisar el historial de commits y verificar que todos los cambios se han aplicado correctamente.
     ```bash
     $ git log
     ```
     ![6-1](https://github.com/user-attachments/assets/354c80c4-85db-4d4c-bffe-6563a9069300)
