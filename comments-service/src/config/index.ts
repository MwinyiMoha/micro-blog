import { environment as local } from './local';
import {environment as production } from  './production';


const getEnv = () => {
    const BLOG_ENV = process.env.BLOG_ENV || null;

    if (BLOG_ENV && BLOG_ENV == 'production') {
        return production;
    }

    return local;
}

export const env = getEnv();
