from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


class TestApp:
    def test_list_posts(self):
        response = client.get("/posts")

        assert response.status_code == 200
        assert response.json() == {"posts": []}

    def test_retrieve_post(self):
        pass

    def test_create_post(self):
        pass

    def test_update_post(self):
        pass

    def test_delete_post(self):
        pass
