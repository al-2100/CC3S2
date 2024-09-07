const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('Hello, World!');
});

module.exports = app;

if (require.main === module) {
    const port = process.env.PORT || 3001;
    const debug = process.env.DEBUG === 'true';  // Leer la variable de entorno DEBUG

    if (debug) {
        console.log('Debugging is enabled');
    } else {
        console.log('Running in production mode');
    }

    app.listen(port, () => {
        console.log(`Server running on port ${port}`);
    });
}
