import { Request, Response } from "express"

export const searchController = async (req: Request, res: Response) => {
    return res.json({
        detail: {
            results: []
        }
    })
}

export const infoController = async (req: Request, res: Response) => {
    return res.json({
        detail: {
            service: 'Search Service',
            version: '0.1.0',
            api_docs: '/docs'
        }
    })
}