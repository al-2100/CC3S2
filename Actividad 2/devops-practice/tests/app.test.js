const request = require('supertest');
const app = require('../src/app');
describe('GET /', () => {
    let server;
    let port = 3000; // Usa el puerto que el servidor escuchará en producción o pruebas
    beforeAll((done) => {
        // Inicia el servidor en el puerto especificado
        server = app.listen(port, done);
    });

    afterAll((done) => {
        // Cierra el servidor después de que se completen los tests
        server.close(done);
    });

    it('should return Hello, World!', async () => {
        const res = await request(app).get('/');
        expect(res.statusCode).toEqual(200);
        expect(res.text).toBe('Hello, World!');
    });
});