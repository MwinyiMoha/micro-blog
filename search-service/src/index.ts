import { app, logger } from './app';

const PORT = Number(process.env.PORT || 3000);

const start = () => {
    app.listen(PORT)
    logger.info(`App running on ${PORT}`)
}

start();