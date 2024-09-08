# Preguntas de reflexión:

**• Pregunta 1: ¿Qué significa "desplazar a la izquierda" en el contexto de DevSecOps y por qué es
importante?**

"Desplazar a la izquierda" en DevSecOps significa integrar la seguridad desde el principio del desarrollo de software, en lugar de esperar hasta el final. Esto ayuda a encontrar y solucionar problemas de seguridad de manera más eficiente, reduciendo costos y riesgos. Al hacerlo, se crea una seguridad proactiva, asegurando que las aplicaciones sean seguras desde el diseño.

---

**• Pregunta 2: Explica cómo IaC mejora la consistencia y escalabilidad en la gestión de infraestructuras**

La Infraestructura como Código (IaC) mejora la consistencia y escalabilidad al definir la infraestructura en código y aplicarla automáticamente. Esto elimina errores manuales y asegura una gestión uniforme en diferentes entornos.

---

**• Pregunta 3: ¿Cuál es la diferencia entre monitoreo y observabilidad? ¿Por qué es crucial la
observabilidad en sistemas complejos?**

El monitoreo se enfoca en observar elementos predefinidos de un sistema, basándose en reglas y métricas establecidas para detectar problemas conocidos. Por otro lado, la observabilidad ofrece una visión más profunda del sistema al utilizar datos de telemetría como métricas, registros y trazas. En sistemas complejos, la observabilidad es crucial para entender no solo si el sistema falla, sino por qué falla, y para optimizar su rendimiento.

---

**• Pregunta 4: ¿Cómo puede la experiencia del desarrollador impactar el éxito de DevOps en una
organización?**

La experiencia del desarrollador impacta el éxito de DevOps al promover una cultura próspera. Si los desarrolladores tienen las herramientas adecuadas, un flujo de trabajo eficiente, y sienten que su trabajo es valorado, estarán más motivados y comprometidos, lo que a su vez mejora la colaboración y la comunicación. Esto reduce los silos organizacionales y facilita el éxito de las prácticas DevOps.

---

**• Pregunta 5: Describe cómo InnerSource puede ayudar a reducir silos dentro de una organización**

InnerSource reduce silos al adoptar prácticas de colaboración de código abierto en un entorno corporativo. Fomenta la apertura, transparencia y contribución voluntaria, rompiendo barreras entre departamentos y facilitando la comunicación.

---
**• Pregunta 6:  ¿Qué rol juega la ingeniería de plataformas en mejorar la eficiencia y la experiencia del desarrollador?**

La ingeniería de plataformas mejora la eficiencia y experiencia del desarrollador al proporcionar herramientas reutilizables y automatización de operaciones. Esto reduce la carga cognitiva de los desarrolladores y acelera el proceso de desarrollo y despliegue.

# Documentación del proceso de la actividad

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

2. Se agregó la configuración para los directorios en el flujo de trabajo en `.github/workflows/ci.yml`, la documentación del paso 2 ya fue actualizada.
3. Se observa que el workflow no pasa de `run tests` a pesar que pasa el test

   ![test](https://github.com/al-2100/CC3S2/blob/main/Actividad%202/imagenes/test.png?raw=true)

4. Tras muchos intentos se modifica app.js y app.test.js para que se cierre correctamente el test

   ![test2](https://github.com/al-2100/CC3S2/blob/main/Actividad%202/imagenes/test2.png?raw=true)
   
   ![app2](https://github.com/al-2100/CC3S2/blob/main/Actividad%202/imagenes/app2.png?raw=true)

5. Funciona
   
   ![fix](https://github.com/al-2100/CC3S2/blob/main/Actividad%202/imagenes/fix.png?raw=true)
  

6. Al intentar acceder a Grafana mediante localhost:3001, no hay conexión. Después de investigar se detecta que la causa es que Grafana utiliza el puerto 3000 como predeterminado, la solución más rápida en esta actividad es intercambiar los puertos de la app y Grafana.
   Resultados:

  ![localhost3000](https://github.com/al-2100/CC3S2/blob/main/Actividad%202/imagenes/localhost3000.png?raw=true)

  ![localhost3001](https://github.com/al-2100/CC3S2/blob/main/Actividad%202/imagenes/localhost3001.png?raw=true)

  ![localhost9090](https://github.com/al-2100/CC3S2/blob/main/Actividad%202/imagenes/localhost9090.png?raw=true)

# Ejercicios adicionales
## Ejercicio 1: Integración continua y DevSecOps

### Teoría 

1. **Lectura**: Revisa el concepto de DevSecOps en el texto proporcionado, poniendo énfasis en el enfoque de "desplazar a la izquierda" y cómo la seguridad se integra en el ciclo de vida del desarrollo de software (SDLC). 
2. **Pregunta de reflexión**: ¿Por qué es crucial integrar la seguridad desde las primeras fases del desarrollo en lugar de dejarla para el final?
### Práctica

#### Implementación:

Utilizamos `devops-practice` pues ya es un pipeline de CI/CD que incluye pruebas de seguridad automatizadas utilizando GitHub Actions y posee una herramienta de análisis de seguridad `npm audit`

1. Introducimos una vulnerabilidad intencionada, modificando `package.json`:

```JSON
{  
  "name": "devops-practice",  
  "version": "1.0.0",  
  "scripts": {  
    "test": "jest"  
  },  
  "dependencies": {  
    "express": "4.16.0"  //Versión con vulnerabilidades
  },  
  "devDependencies": {  
    "jest": "^27.0.0",  
    "supertest": "^6.1.3"  
  }  
}
```
2. Hacemos commit y push para que GitHub Actions se active
3. Observamos el workflow

	![vulnerabilidad](https://github.com/al-2100/CC3S2/blob/main/Actividad%202/imagenes/vulnerabilidad.png?raw=true)

4. Revisamos detalles

	![workflow-ej1](https://github.com/al-2100/CC3S2/blob/main/Actividad%202/imagenes/workflow-ej1.png?raw=true)

#### Evaluación:

- Analiza el impacto de detectar la vulnerabilidad en una fase temprana del desarrollo. ¿Qué hubiera pasado si la vulnerabilidad hubiera llegado a producción? 
	1. Vulnerabilidad: **Prototype Pollution en `qs`**
		- **Paquete afectado:** `qs`
		- **Dependencia de:** `express` y `express > body-parser`
		- **Descripción:** Esta vulnerabilidad permite que un atacante pueda modificar el prototipo de un objeto, lo que podría llevar a la corrupción de datos o incluso la ejecución de código arbitrario.
		- **Solución:** Actualizar la dependencia a una versión parcheada. El informe recomienda ejecutar `npm install express@4.19.2` para corregir esta vulnerabilidad.
	2. Vulnerabilidad: **Open Redirect en Express.js**
		- **Paquete afectado:** `express`
		- **Descripción:** Esta vulnerabilidad permite que un atacante pueda redirigir a los usuarios a una URL no deseada, lo que puede ser explotado en ataques de phishing o redirecciones maliciosas.
		- **Solución:** Actualizar el paquete `express` a una versión parcheada.
	
	Detectar vulnerabilidades de seguridad antes de lanzar el código a producción evita ataques que exploten debilidades en entornos públicos. Por ejemplo, la vulnerabilidad de **Prototype Pollution** permitiría a atacantes alterar datos o ejecutar código malicioso. Corregirla antes de lanzar minimiza estos riesgos

- Discute cómo la integración de DevSecOps puede prevenir problemas de seguridad y reducir costos.

	DevSecOps introduce prácticas de seguridad desde el inicio del desarrollo, integrando análisis de seguridad automatizados en cada paso del ciclo de vida del software. La automatización de pruebas de seguridad garantiza una revisión continua y exhaustiva del código y dependencias sin intervención humana, reduciendo errores y acelerando el desarrollo. Los desarrolladores ahorran tiempo y se evitan costos asociados con correcciones urgentes en producción al detectar y corregir vulnerabilidades temprano.

## Ejercicio 2: Infraestructura como código y gestión de configuración
### Teoría

1. **Lectura**: Repasa la sección sobre Infraestructura como Código (IaC) en el texto, enfocándote en cómo IaC mejora la reproducibilidad y reduce errores en la gestión de infraestructuras.
2. **Pregunta de reflexión**: ¿Cuáles son las ventajas y desventajas de usar IaC en comparación con la configuración manual de infraestructuras?
- IaC ofrece consistencia, escalabilidad y automatización, ideal para infraestructuras grandes y dinámicas. Sin embargo, la curva de aprendizaje es alta y el tiempo inicial para escribir los scripts de IaC puede ser mayor que la configuración manual rápida, especialmente para pequeñas infraestructuras.
- La configuración manual es rápida para pequeñas infraestructuras, pero es propensa a errores y difícil de replicar o escalar correctamente.
### Práctica

1. **Implementación**:
   - Se vuelve a utilizar `devops-practice` pues ya está configurado
   - Se debe modificar la variable de entorno `NODE_ENV`: 
	   - `development`: Indica que la app está en un entorno de desarrollo. En este modo, puede habilitar funciones útiles como logs detallados, mensajes de error completos, y ciertas herramientas para desarrolladores.
	   - `production`: Indica que la app está en un entorno de producción. En este modo, la app suele estar optimizada, con menos logs y mensajes de error genéricos para mejorar la seguridad y el rendimiento. 
   - Se modifica `app.js` para identificar el tipo de entorno

      ```javascript
      if (debug) {  
          console.log('Debugging is enabled');  
      } else {  
          console.log('Running in production mode');  
      }
      ```

2. **Simulación**:
	-  Realiza un despliegue primero en un entorno de desarrollo y luego en producción.
		  - En desarrollo agregamos debugging:
		```yaml
		environment:  
		  - NODE_ENV=development  # Modo desarrollo  
		  - DEBUG=true  # Habilitar debugging
		```

		- Despiegue en desarrollo:

			![debug](https://github.com/al-2100/CC3S2/blob/main/Actividad%202/imagenes/debug.png?raw=true)

		- Despliegue en producción:

			![[production.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%202/imagenes/production.png?raw=true)

	  - Introduce un cambio en la configuración (como cambiar el puerto o una variable de entorno) y despliega nuevamente.
		 - Cambiamos el puerto a 4000

			 ![[4000.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%202/imagenes/4000.png?raw=true)

3. **Evaluación**:
   - Compara la consistencia entre los entornos. ¿Cómo asegura IaC que ambos entornos se mantengan alineados?
	IaC (Infraestructura como Código) permite que tanto el entorno de desarrollo como el de producción se configuren de la misma forma usando archivos como `docker-compose.yml`. Al tener un archivo que describe cómo levantar la infraestructura, siempre se garantiza que los entornos se configuren igual. Si haces cambios (como agregar servicios o cambiar puertos), solo ajustas el archivo una vez y lo aplicas a ambos entornos, manteniéndolos consistentes.
   - Discute cómo IaC ayuda a escalar aplicaciones en diferentes entornos.
	IaC hace que escalar sea mucho más fácil porque todo está automatizado. Si necesitas más capacidad (por ejemplo, más instancias de la app), puedes simplemente modificar el archivo de configuración para agregar más contenedores o servicios, y estos se desplegarán automáticamente. En lugar de configurar manualmente cada servidor, IaC te permite hacer estos cambios de manera rápida y sin errores.

# Ejercicio 3: Observabilidad y monitoreo avanzado

## Teoría
1. **Lectura**: Lee la sección sobre Observabilidad en el texto, entendiendo la diferencia entre monitoreo tradicional y observabilidad.
2. **Pregunta de reflexión**: ¿Cómo puede la observabilidad mejorar la resolución de problemas en sistemas distribuidos o microservicios?
## Práctica

1. **Implementación**:
	Reutilizamos `devops-practice` y modificamos app.js para generar logs detallados y recolectar métricas (al ser tan grandes los cambios mejor revisar `app.js` que se encuentra bien comentado).
	- `winston` se utiliza para registrar eventos y actividades en la aplicación
	- `prom-client` es una librería que permite exponer métricas de rendimiento de la aplicación que pueden ser recolectadas por Prometheus.
2. **Experimentación**:
   - Se introduce un tiempo de respuesta lento en `metrics`
```javascript
// Simulando un retraso en el endpoint /metrics  
app.get('/metrics', async (req, res) => {  
    logger.info('Solicitud a /metrics con retraso simulado');  
  
    // Simulamos un retraso de 3 segundos antes de responder  
    setTimeout(async () => {  
        res.set('Content-Type', promClient.register.contentType);  
        res.end(await promClient.register.metrics());  
        logger.info('Métricas enviadas después de un retraso');  
    }, 3000);  // Retraso de 3 segundos  
});
```
 - Se configura una alerta en Grafana que se activen cuando el promedio de respuesta en `metrics` sea mayor a 0.2s en un minuto. A continuación los pasos:
	 1. Agregamos a **Prometheus** como data source en **Grafana**
		 ![[datasource.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%202/imagenes/datasource.png?raw=true)
		 
		 ![[datasource2.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%202/imagenes/datasource2.png?raw=true)
		 
	2. Creamos un dashboard con el data source y agregamos la query:
		`histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket[1m])) by (le, route))`
		
		![[dashboard3.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%202/imagenes/dashboard3.png?raw=true)
		
	3. Creamos la alerta en el panel
		![[alerta.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%202/imagenes/alerta.png?raw=true)
		![[alerta2.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%202/imagenes/alerta2.png?raw=true)
		
	4. Observamos nuestro dashboard antes y después de introducir la falla a ser detectada
		
		![[dashboard4.png]](https://github.com/al-2100/CC3S2/blob/main/Actividad%202/imagenes/dashboard4.png?raw=true)
		
3. **Evaluación**:
   - Discute cómo la observabilidad permite identificar problemas que no serían evidentes con un monitoreo tradicional.

	  La **observabilidad** nos permite ver mucho más a fondo cómo está funcionando un sistema que solo con el **monitoreo tradicional**. En el monitoreo tradicional, solo observamos cosas básicas como si un servidor está encendido o el uso de CPU, pero no siempre nos dice por qué algo va mal. Con la observabilidad, podemos mirar más detalles y encontrar problemas que no son tan evidentes a primera vista.
	
   - Reflexiona sobre la importancia de las métricas, logs y trazas en la gestión de sistemas modernos.

	  Las **métricas** nos muestran números sobre el rendimiento del sistema, como tiempos de respuesta o uso de recursos; los **logs** son como un diario que registra lo que ocurre en la aplicación, ayudándonos a ver errores y eventos clave; y las **trazas** nos permiten seguir el camino de una solicitud a través de varios servicios, viendo dónde puede estar el problema. Juntos, estos tres elementos nos dan una visión clara y detallada del sistema para encontrar y resolver problemas de forma más precisa y eficaz.