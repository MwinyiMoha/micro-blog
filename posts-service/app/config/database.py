from urllib.parse import quote_plus

from decouple import config

DEBUG = config('DEBUG', False)

DB = config("DB_NAME", None)
posts_db = DB
posts_coll = 'posts'

HOST = config("MONGO_HOST", None)
PORT = config("MONGO_PORT", None)
USER = config("MONGO_USER", None)
MONGO_PASS = config("MONGO_PASSWORD", "")


def get_database_url():
    PASS = quote_plus(MONGO_PASS)

    if DEBUG:
        return f"mongodb://{USER}:{PASS}@{HOST}:{PORT}/{DB}?authSource=admin"

    return f"mongodb+srv://{USER}:{PASS}@{HOST}/{DB}?retryWrites=true&w=majority"
