import bodyParser from "body-parser";
import express, { Request, Response, NextFunction } from 'express';
import pino from 'pino';
import expressPino from 'express-pino-logger';

import { router as searchRouter } from "./api/routes";
import { IError } from "./utils/models";

const logger = pino({ level: process.env.LOG_LEVEL || 'info' });
const appLogger = expressPino(logger)

const app = express()

app.use(appLogger)
app.use(bodyParser.json({ limit: '10mb' }));
app.use(bodyParser.urlencoded({ extended: false }));

app.use((req: Request, res: Response, next: NextFunction) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Methods', 'GET, HEAD, OPTIONS');
    res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept, Authorization, X-User-Id');
    req.setTimeout(6000);
    next();
});

app.use(searchRouter)

app.use((req: Request, res: Response, next: NextFunction) => {
    let error: IError = new Error('Not Found');
    error.status = 404;
    next(error)
});

app.use((err: IError, req: Request, res: Response, next: NextFunction) => {
    res.locals.message = err.message;
    res.locals.error = process.env.ENV == 'production' ? {} : err;
    
    res.status(err.status || 500);
    res.send(err);
});

export { logger, app }