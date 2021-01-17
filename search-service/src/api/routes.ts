import express from 'express';

import { infoController, searchController } from "./controllers";

export const router = express.Router();

router.get('/', searchController)
router.get('/info', infoController)
