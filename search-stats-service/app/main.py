from decouple import config
from fastapi import FastAPI

app = FastAPI()

APP_VERSION = config("APP_VERSION")
APP_NAME = config("SERVICE_NAME")
API_DOCS_URL = config("API_DOCS_URL")


@app.get("/")
def root():
    return {
        "detail": {
            "service": APP_NAME,
            "version": APP_VERSION,
            "api_docs": API_DOCS_URL,
        }
    }
