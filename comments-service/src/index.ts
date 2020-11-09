import http from 'http';
import mongoose from 'mongoose';

import {logger, app } from './app';
import { env } from './config';

const startServer = async() => {
    try {
        // await mongoose.connect(env.mongoURI, { useNewUrlParser: true })
        // logger.info('Connected to database!');

        const httpServer = http.createServer(app);
        const server = httpServer.listen(env.port, () => {
            logger.info(`API running on port ${env.port}`)
        })

        process.on('SIGTERM', async() => {
            await mongoose.disconnect()
            logger.info('Database connection closed!')
        })
    } catch(err) {
        logger.error(err);
    }
}

startServer();
