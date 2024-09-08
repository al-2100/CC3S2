// app.js
const express = require('express');
const winston = require('winston');
const promClient = require('prom-client');  // Prometheus client

const app = express();
const PORT = 3001;

// Configuración de Winston Logger
const logger = winston.createLogger({
    level: 'info',
    format: winston.format.combine(
        winston.format.timestamp(),
        winston.format.printf(({ timestamp, level, message }) => {
            return `${timestamp} [${level.toUpperCase()}]: ${message}`;
        })
    ),
    transports: [
        new winston.transports.Console(),  // Log a consola
        new winston.transports.File({ filename: 'app.log' })  // Log a archivo
    ]
});

// Inicializar métricas de Prometheus
const collectDefaultMetrics = promClient.collectDefaultMetrics;
collectDefaultMetrics();  // Recolecta métricas básicas como CPU, memoria, etc.

const httpRequestDurationMicroseconds = new promClient.Histogram({
    name: 'http_request_duration_seconds',
    help: 'Duración de las solicitudes HTTP en segundos',
    labelNames: ['method', 'route', 'code'],
    buckets: [0.1, 0.2, 0.5, 1, 3, 5]  // Intervalos de tiempo para medir (en segundos)
});

// Middleware para registrar todas las solicitudes
app.use((req, res, next) => {
    const end = httpRequestDurationMicroseconds.startTimer();  // Inicia el cronómetro
    res.on('finish', () => {
        end({ method: req.method, route: req.path, code: res.statusCode });  // Detiene el cronómetro al finalizar la respuesta
    });
    next();
});

// Endpoint raíz
app.get('/', (req, res) => {
    logger.info('Solicitud recibida en el endpoint raíz');
    res.send('Hello, World!');
});

// Endpoint /status
app.get('/status', (req, res) => {
    logger.info('Solicitud al endpoint /status');
    res.json({ status: 'ok' });
});

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

module.exports = app;

if(require.main === module){
    const port = process.env.PORT || 3001;
    app.listen(port,()=> {
        console.log(`Server running on port ${port}`);
    })
}
