from fastapi import FastAPI

from .api import router as posts_router
from .database.utils import connect_to_mongo, close_mongo_connection

app = FastAPI()

app.add_event_handler('startup', connect_to_mongo)
app.add_event_handler('shutdown', close_mongo_connection)

app.include_router(posts_router)
