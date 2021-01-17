from decouple import config
from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


class TestRoot:
    def test_root_view(self):
        response = client.get("/")
        data = response.json()
        version = config("APP_VERSION")

        assert response.status_code == 200
        assert data["detail"]["version"] == version
