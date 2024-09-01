# Preguntas de reflexión:

**• Pregunta 1: ¿Qué significa "desplazar a la izquierda" en el contexto de DevSecOps y por qué es
importante?**



---

**• Pregunta 2: Explica cómo IaC mejora la consistencia y escalabilidad en la gestión de infraestructuras**



---

**• Pregunta 3: ¿Cuál es la diferencia entre monitoreo y observabilidad? ¿Por qué es crucial la
observabilidad en sistemas complejos?**



---

**• Pregunta 4: ¿Cómo puede la experiencia del desarrollador impactar el éxito de DevOps en una
organización?**



---

**• Pregunta 5: Describe cómo InnerSource puede ayudar a reducir silos dentro de una organización**



---
**• Pregunta 6:  ¿Qué rol juega la ingeniería de plataformas en mejorar la eficiencia y la experiencia del desarrollador?**


# Documentación del Proyecto

## 1. Configuración del Entorno

 Al igual que en la actividad 1, utilizaré **WSL (Windows Subsystem for Linux)**.
 
 Sin embargo, a diferencia de la documentación anterior, en esta ocasión solo incluiré capturas de la configuración del entorno, ya que los pasos y explicaciones son los mismos y están detalladamente descritos en la documentación de la actividad 1.

 ![config](https://github.com/al-2100/CC3S2/blob/main/Actividad%202/imagenes/config.png?raw=true)

 ![app](https://github.com/al-2100/CC3S2/blob/main/Actividad%202/imagenes/app.png?raw=true)

 ![app-test](https://github.com/al-2100/CC3S2/blob/main/Actividad%202/imagenes/app-test.png?raw=true)
 
 ![package](https://github.com/al-2100/CC3S2/blob/main/Actividad%202/imagenes/package.png?raw=true)
## 2. Implementación de DevSecOps

### Integración de Seguridad

1. Configurar una herramienta de análisis de seguridad estática como `npm audit` para encontrar vulnerabilidades en las dependencias:
   ```bash
   npm audit
   ```

2. Automatizar el análisis de seguridad en GitHub Actions:
   - Actualizar el archivo `.github/workflows/ci.yml` para incluir un paso de seguridad:
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
           working-directory: 'Actividad 2/devops-practice/'  
     
         - name: Run tests  
           run: npm test  
           working-directory: 'Actividad 2/devops-practice/'  
     
         - name: Run security audit  
           run: npm audit  
           working-directory: 'Actividad 2/devops-practice/'

   ```
Hay que señalar que se agrega `working-directory` para configurar el directorio en el flujo de trabajo, pues a diferencia de la actividad 1, ahora hay sub-carpetas que contienen a cada actividad.

## 3. Implementación de Infraestructura como Código (IaC)

### Usar Docker para contenerizar la aplicación

1. Crear un archivo `Dockerfile`:
   ```dockerfile
   FROM node:14
   WORKDIR /app
   COPY package*.json ./
   RUN npm install
   COPY . .
   EXPOSE 3000
   CMD ["node", "src/app.js"]
   ```

2. Construir y correr el contenedor:
   ```bash
   docker build -t devops-practice .
   docker run -p 3000:3000 devops-practice
   ```
![docker](https://github.com/al-2100/CC3S2/blob/main/Actividad%202/imagenes/docker.png?raw=true)
### Automatiza la gestión de contenedores usando Docker Compose

1. Crear un archivo `docker-compose.yml`:
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

2. Correr la aplicación usando Docker Compose:
   ```bash
   docker-compose up --build -d
   ```
![docker2](https://github.com/al-2100/CC3S2/blob/main/Actividad%202/imagenes/docker2.png?raw=true)

## 4. Implementación de Observabilidad

### Configura Prometheus y Grafana para monitorear la aplicación

1. Crea un archivo `prometheus.yml` para configurar Prometheus:
   ```yaml
   global:
     scrape_interval: 15s

   scrape_configs:
     - job_name: 'node-app'
       static_configs:
         - targets: ['app:3000']
   ```

2. Configura Grafana utilizando un `docker-compose.yml` actualizado:
   ```yaml
   version: '3.8'
   services:
     app:
       build: .
       ports:
         - "3000:3000"
       environment:
         - NODE_ENV=production

     prometheus:
       image: prom/prometheus
       volumes:
         - ./prometheus.yml:/etc/prometheus/prometheus.yml
       ports:
         - "9090:9090"

     grafana:
       image: grafana/grafana
       ports:
         - "3001:3001"
   ```
   3. Correr la aplicación usando Docker Compose:
   ![grafana](https://github.com/al-2100/CC3S2/blob/main/Actividad%202/imagenes/grafana.png?raw=true)


## 5. Evaluación y comentarios de la experiencia

Al implementar DevSecOps en una aplicación web sencilla en Node.js, reflexionamos sobre cómo cada componente contribuye a un flujo de trabajo DevOps más seguro, eficiente y visible. A continuación, exploramos los beneficios de cada paso:

1. **Configuración del Entorno**: Inicializamos el proyecto, instalamos dependencias, implementamos la API REST y realizamos pruebas básicas. Esto nos aseguró que el código base estuviera libre de errores críticos y vulnerabilidades desde el inicio, lo que mejora la seguridad y eficiencia. Además, la estructura del proyecto y las pruebas nos proporcionaron una base clara para el desarrollo y facilitaron la comprensión del funcionamiento de la aplicación.
    
2. **Implementación de DevSecOps**: Integramos análisis de seguridad estática y automatización en GitHub Actions. Esto mejora la seguridad al detectar vulnerabilidades en dependencias antes de que llegaran a producción. La automatización de pruebas reduce el tiempo manual de revisión y aumenta la velocidad de desarrollo.
    
3. **Implementación de Infraestructura como Código (IaC)**: Contenerizamos la aplicación con Docker y usamos Docker Compose para la gestión de contenedores. Esto reduce el riesgo de conflictos y problemas de seguridad al ejecutar aplicaciones en entornos aislados. La contenerización también simplifica la gestión de dependencias y despliegue, facilitando la creación de entornos consistentes y replicables.
    
4. **Implementación de Observabilidad**: Configuramos Prometheus y Grafana para monitorear la aplicación. Esto permite identificar comportamientos anómalos que podrían indicar problemas de seguridad.
    

En conclusión, cada componente del flujo de trabajo DevSecOps contribuye a un proceso de desarrollo más seguro, eficiente y visible. Cada paso que dimos nos ayudó a mejorar la seguridad, reducir errores y trabajar de manera más eficiente. Esto nos enseñó que, al integrar todos estos componentes, podemos crear un proceso de desarrollo que sea realmente efectivo y seguro.

## 6. Correciones y consideraciones finales

Posterior a la experiencia de la actividad y al subirla finalizada a github, se realizaron las siguientes observaciones y ajustes en este orden:

1. Se observa que el workflow falla
   ![directorio](https://github.com/al-2100/CC3S2/blob/main/Actividad%202/imagenes/directorio.png?raw=true)
3. Se agregó la configuración para los directorios en el flujo de trabajo en `.github/workflows/ci.yml`, la documentación del paso 2 ya fue actualizada.
4. Se observa que el workflow no pasa de `run tests` a pesar que pasa el test
   ![test](https://github.com/al-2100/CC3S2/blob/main/Actividad%202/imagenes/test.png?raw=true)
5. Tras muchos intentos se modifica app.js y app.test.js para que se cierre correctamente el test
   ![test2](https://github.com/al-2100/CC3S2/blob/main/Actividad%202/imagenes/test2.png?raw=true)
   
   ![app2](https://github.com/al-2100/CC3S2/blob/main/Actividad%202/imagenes/app2.png?raw=true)
7. Funciona
   
   ![fix](https://github.com/al-2100/CC3S2/blob/main/Actividad%202/imagenes/fix.png?raw=true)
