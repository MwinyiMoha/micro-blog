import express,{ Request, Response, NextFunction } from 'express';
import bodyParser from 'body-parser';
import pino from 'pino';
import expressPino from 'express-pino-logger';

import { env } from './config';
import { getCommentsRouter } from './routes/get-comments';
import { IResError } from './models';

const logger = pino({ level: env.logLevel || 'info' });
const xLogger = expressPino(logger);

const app = express();
app.use(xLogger);

app.use(bodyParser.json({ limit: '10mb' }));
app.use(bodyParser.urlencoded({ extended: false }));

app.use((req: Request, res: Response, next: NextFunction) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Methods', 'GET, HEAD, OPTIONS, POST, PUT, DELETE');
    res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept, Authorization');
    req.setTimeout(6000);
    next();
});

app.use(getCommentsRouter);

app.use((req: Request, res: Response, next: NextFunction) => {
    let error: IResError = new Error('Not Found');
    error.status = 404;
    next(error)
});

app.use((err: IResError, req: Request, res: Response, next: NextFunction) => {
    res.locals.message = err.message;
    res.locals.error = env.production ? {} : err;
    
    res.status(err.status || 500);
    res.send(err);
});

export { logger, app };
