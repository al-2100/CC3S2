# Preguntas de reflexión

**• Pregunta 1: ¿Por qué surgió la necesidad de DevOps en el desarrollo de software?**

La necesidad de DevOps surgió debido a la falta de integración entre los equipos de desarrollo y operaciones, lo que causaba problemas en la entrega de software. Antes, el desarrollo de software era estático, pero ahora requiere actualizaciones constantes y gestión continua.

---

**• Pregunta 2: Explica cómo la falta de comunicación y coordinación entre los equipos de desarrollo y operaciones en el pasado ha llevado a la creación de DevOps.**

Los equipos trabajaban en silos con objetivos y herramientas diferentes, lo que generaba conflictos durante las implementaciones. El equipo de desarrollo buscaba agregar nuevas características, mientras que operaciones priorizaba la estabilidad del sistema. La falta de comunicación y coordinación llevó a la creación de DevOps como un enfoque para unir ambos equipos y alinear sus objetivos.

---

**• Pregunta 3: Describe cómo el principio de mejora continua afecta tanto a los aspectos técnicos como culturales de una organización.**

La mejora continua en DevOps mejora la eficiencia técnica mediante la automatización y el análisis de métricas. También promueve un entorno colaborativo que elimina silos, fomenta la responsabilidad y el aprendizaje, y mejora la experiencia del desarrollador. El enfoque basado en ciclos de retroalimentación asegura que las organizaciones puedan ajustarse rápidamente a los cambios y mantenerse competitivas.

---

**• Pregunta 4: ¿Qué significa que DevOps no se trata solo de herramientas, individuos o procesos?**

DevOps no se trata solo de herramientas, individuos o procesos porque, aunque estas son partes importantes, el éxito de DevOps depende de un cambio cultural dentro de la organización. No se trata solo de implementar herramientas o asignar roles específicos, sino de un cambio cultural que elimine la fricción entre los silos y mejore la colaboración y la eficiencia.

---

**• Pregunta 5: Según el texto, ¿cómo contribuyen los equipos autónomos y multifuncionales a una implementación exitosa de DevOps?**

Los equipos autónomos y multifuncionales son esenciales para DevOps porque integran diversas habilidades, eliminan cuellos de botella y agilizan el flujo de trabajo. Esto fomenta una cultura de colaboración y propiedad, fundamentales para el éxito de DevOps.
# Documentación del proceso de la actividad

## 1. Configuración del Entorno

Para seguir los pasos de la actividad en Windows, estoy utilizando **WSL (Windows Subsystem for Linux)**. Este subsistema permite ejecutar un entorno de Linux directamente en Windows, facilitando la ejecución de comandos y scripts sin necesidad de modificar los pasos originales de la actividad.

### Configuración de WSL
Para instalar WSL se siguen estos pasos:

1. **Instalar WSL**: Abrir PowerShell como administrador y ejecuta:
   ```bash
   wsl --install

Esto instalará la versión predeterminada de WSL y una distribución de Linux (ubuntu como predeterminado).

2. Acceder al Entorno WSL: Abrir la terminal de Windows (Command Prompt o PowerShell) y ejecutar:
   ```bash
   wsl
![wsl](https://github.com/al-2100/CC3S2/blob/main/Actividad%201/wsl.png)

A continuación, se presenta la lista de pasos a seguir, extraída de la actividad original, junto con explicaciones adicionales.

### 1.1 Inicialización del Proyecto de Node.js

Para iniciar el proyecto de Node.js, seguimos estos pasos:

1. **Crear el directorio del proyecto y acceder a él:**

    ```bash
    mkdir devops-practice
    cd devops-practice
    ```

2. **Inicializar un nuevo proyecto de Node.js:**

    ```bash
    npm init -y
    ```

3. **Instalar las dependencias necesarias:**

    ```bash
    npm install express jest supertest
    ```
  
    A diferencia de las instrucciones originales, agregamos `supertest`.

4. **Crear la estructura del proyecto:**

    ```bash
    mkdir src tests
    touch src/app.js tests/app.test.js
    ```
- `src/app.js`: Contendrá la lógica de la aplicación.
- `tests/app.test.js`: Contendrá las pruebas para la API.
  
5. **Implementar la API REST en `src/app.js`:**
	
 	Aquí se implementa un servidor básico con Express, además, corregimos un error: 
	Faltaban las comillas simples en el mensaje de `console.log()`

    ```javascript
    const express = require('express');
    const app = express();

    app.get('/', (req, res) => {
        res.send('Hello, World!');
    });

    const port = process.env.PORT || 3000;
    app.listen(port, () => {
        console.log(`Server running on port ${port}`);
    });

    module.exports = app;
    ```
- **`app.get('/', (req, res) => {...})`:** Define un endpoint `GET` en la ruta raíz `/` que responde con el texto "Hello, World!".
- **`app.listen(port, () => {...})`:** Inicia el servidor en el puerto definido, o en el puerto 3000 por defecto.
  
6. **Escribir un test básico en `tests/app.test.js`:**
	
 	Se utiliza Jest y Supertest para realizar pruebas sobre el endpoint de la API.

    ```javascript
    const request = require('supertest');
    const app = require('../src/app');

    describe('GET /', () => {
        it('should return Hello, World!', async () => {
            const res = await request(app).get('/');
            expect(res.statusCode).toEqual(200);
            expect(res.text).toBe('Hello, World!');
        });
    });
    ```
- **`request(app).get('/')`:** Hace una solicitud HTTP `GET` al endpoint raíz `/`.
- **`expect(res.statusCode).toEqual(200)`:** Verifica que el código de estado de la respuesta sea 200 (OK).
- **`expect(res.text).toBe('Hello, World!')`:** Verifica que el texto de la respuesta sea "Hello, World!".
  
7. **Configurar el script de test en `package.json`:**
	
 	Modificamos el archivo `package.json` para añadir un script que ejecute las pruebas.
    ```json
    {
        "name": "devops-practice",
        "version": "1.0.0",
        "scripts": {
            "test": "jest"
        },
        "dependencies": {
            "express": "^4.17.1"
        },
        "devDependencies": {
            "jest": "^27.0.0",
            "supertest": "^6.1.3"
        }
    }
    ```
  8. Probamos que el test funcione
      ```bash
        npm test
      ```
  
![npmtest](https://github.com/al-2100/CC3S2/blob/main/Actividad%201/npmtest.png)

## 2. Pipeline CI/CD

### Parte 1: Configura Integración Continua (CI) con GitHub Actions

GitHub Actions automatiza la integración continua, ejecutando pruebas cada vez que se realiza un push o pull request en la rama `main`.

1. **Creamos un archivo de configuración para GitHub Actions:**

    ```bash
    mkdir -p .github/workflows
    touch .github/workflows/ci.yml
    ```

2. **Definimos el flujo de trabajo en `.github/workflows/ci.yml`:**

    ```yaml
    name: CI Pipeline
    on:
      push:
        branches:
          - main
      pull_request:
        branches:
          - main

    jobs:
      build:
        runs-on: ubuntu-latest
        steps:
          - name: Checkout code
            uses: actions/checkout@v2

          - name: Set up Node.js
            uses: actions/setup-node@v2
            with:
              node-version: '14'

          - name: Install dependencies
            run: npm install

          - name: Run tests
            run: npm test
    ```
- **`actions/checkout@v2`**: Revisa el código del repositorio.
- **`actions/setup-node@v2`**: Configura la versión de Node.js.
- **`npm install`**: Instala las dependencias del proyecto.
- **`npm test`**: Ejecuta las pruebas definidas en el proyecto.
  
3. **Subimos el código a GitHub:**

    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    git branch -M main
    git remote add origin https://github.com/al-2100/CC3S2.git
    git push -u origin main
    ```

### Parte 2: Configura Entrega Continua (CD) con Docker

Docker permite contenerizar la aplicación y desplegarla en diferentes entornos de manera consistente.

1. **Creamos un archivo Docker para contenerizar la aplicación:**

    - **Creamos un `Dockerfile`:**

        ```dockerfile
        # Usa la imagen oficial de Node.js
        FROM node:14

        # Establece el directorio de trabajo en el contenedor
        WORKDIR /app

        # Copia los archivos package.json y package-lock.json
        COPY package*.json ./

        # Instala las dependencias
        RUN npm install

        # Copia el resto de los archivos de la aplicación
        COPY . .

        # Expone el puerto en el que la aplicación correrá
        EXPOSE 3000

        # Comando para iniciar la aplicación
        CMD ["node", "src/app.js"]
        ```

    - **Construimos la imagen de Docker:**

        ```bash
        docker build -t devops-practice .
        ```

    - **Correr el contenedor localmente:**

        ```bash
        docker run -p 3000:3000 devops-practice
        ```

        ![dockerrun](https://github.com/al-2100/CC3S2/blob/main/Actividad%201/dockerrun.png)

2. **Automatizar el despliegue con GitHub Actions:**

    - **Actualizamos el archivo `.github/workflows/ci.yml` para construir y desplegar la imagen de Docker:**

        ```yaml
        name: CI/CD Pipeline
        on:
          push:
            branches:
              - main
          pull_request:
            branches:
              - main

        jobs:
          build:
            runs-on: ubuntu-latest
            steps:
              - name: Checkout code
                uses: actions/checkout@v2

              - name: Set up Node.js
                uses: actions/setup-node@v2
                with:
                  node-version: '14'

              - name: Install dependencies
                run: npm install

              - name: Run tests
                run: npm test

              - name: Build Docker image
                run: docker build -t devops-practice .

              - name: Run Docker container
                run: docker run -d -p 3000:3000 devops-practice
        ```

3. **Verificamos que la aplicación se despliegue correctamente localmente usando Docker:**

    - Abrimos un navegador web y accedemos a [http://localhost:3000](http://localhost:3000) para verificar que la aplicación esté funcionando.

  ![screenshot1](https://github.com/al-2100/CC3S2/blob/main/Actividad%201/screenshot1.png)
## 3. Automatización

### 3.1 Automatiza la Configuración y Gestión del Entorno Local usando Docker Compose

Docker Compose permite definir y ejecutar aplicaciones Docker con múltiples contenedores.
1. **Crea un archivo `docker-compose.yml`:**

    ```yaml
    version: '3.8'

    services:
      app:
        build: .
        ports:
          - "3000:3000"
        environment:
          - NODE_ENV=production
    ```

2. **Corre la aplicación usando Docker Compose:**

    ```bash
    docker-compose up --build -d
    ```

## 4. Evaluación y comentarios de la experiencia

El proceso incluyó la creación de un entorno de desarrollo con Node.js, la implementación de una API REST sencilla y la configuración de pruebas. Posteriormente, se estableció un pipeline CI/CD utilizando GitHub Actions y Docker para automatizar la construcción y el despliegue de la aplicación. Esta actividad nos ha permitido experimentar cómo estas herramientas trabajan en conjunto para automatizar tareas críticas en el ciclo de vida del desarrollo de software:

- La **API**: Durante la actividad, esta API se integra en el pipeline automatizado, asegurando que cualquier cambio en su código pase por el proceso de pruebas y despliegue antes de estar disponible para su uso en producción. Esto permite detectar y corregir errores en etapas tempranas, evitando sorpresas y garantizando que solo el código que cumple con los estándares de calidad llegue a producción.

- **Docker**: Asegura que la aplicación se ejecute de manera consistente, sin importar el entorno en el que se despliegue. Esto elimina problemas comunes como las diferencias entre entornos de desarrollo, pruebas y producción, reduciendo así posibles fricciones entre los equipos de desarrollo (Dev) y operaciones (Ops).

- **GitHub Actions**: Es la herramienta que define el pipeline automatizado. En esta actividad, se configuró un flujo de trabajo que se activa automáticamente cuando se realizan cambios en el repositorio de GitHub. Los cambios en el código se construyen, prueban y despliegan automáticamente, reduciendo el tiempo entre el desarrollo y la implementación. La automatización de estos pasos reduce significativamente la intervención manual, evitando así retrasos y errores manuales.

En resumen, al automatizar el proceso de construcción, pruebas y despliegue, y al estandarizar el entorno con Docker, el pipeline automatizado facilita una colaboración más eficaz entre los equipos de desarrollo y operaciones.

## 5. Correciones y consideraciones finales

Después de completar la actividad y subirla finalizada a GitHub, se realizaron las siguientes observaciones y ajustes en este orden:

1. Se agregó la configuración para los directorios en el flujo de trabajo en `.github/workflows/ci.yml`.
   ```yaml
   name: CI/CD Pipeline

	on:
	  push:
	    branches:
	      - main
	  pull_request:
	    branches:
	      - main
	
	jobs:
	  build:
	    runs-on: ubuntu-latest

	    steps:
	      - name: Checkout code
	        uses: actions/checkout@v2
	      
	      - name: Set up Node.js
	        uses: actions/setup-node@v2
	        with:
	          node-version: '14'
	      
	      - name: Install dependencies
	        run: npm install
	        working-directory: 'Actividad 1/devops-practice/'
	      
	      - name: Run tests
	        run: npm test
	        working-directory: 'Actividad 1/devops-practice/'
	      
	      - name: Build Docker image
	        run: docker build -t devops-practice .
	        working-directory: 'Actividad 1/devops-practice/'
	      
	      - name: Run Docker container
	        run: docker run -d -p 3000:3000 devops-practice
	        working-directory: 'Actividad 1/devops-practice/'
   ```
2. Se observa que el workflow no pasa de `run tests` a pesar que pasa el test
   
   ![test-actividad1](https://github.com/user-attachments/assets/5f501760-10fd-4593-b310-115921900e86)

3. Se modifica app.js y app.test.js para que se cierre correctamente el test

   ![test2](https://github.com/user-attachments/assets/11e8262c-1bc0-4834-b2a8-350e89023f77)
   ![app2](https://github.com/user-attachments/assets/a658aa70-abc1-4b76-99df-71de07c927de)
   
4. Funciona
   
   ![fix-actividad1](https://github.com/user-attachments/assets/e2809c7e-32b7-430e-90de-47d00cd3ae23)
