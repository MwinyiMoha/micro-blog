from motor.motor_asyncio import AsyncIOMotorClient as AIOMC

from ..config.database import get_database_url
from ..config.logs import logger


class Database:
    client: AIOMC = None


db = Database()


async def connect_to_mongo():

    logger.info('Connecting to database...')

    db.client = AIOMC(get_database_url())

    logger.info('Successfully connected to database!')


async def close_mongo_connection():

    logger.info('Closing connection to database...')

    db.client.close()

    logger.info('Database connection closed!')


async def get_database() -> AIOMC:
    yield db.client
