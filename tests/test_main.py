from dependency_intelligence_ai.main import app
from fastapi.testclient import TestClient
client = TestClient(app)
class TestRoot:
    def test_read_root(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World"}

class TestScan:
    def test_scan_success(self):
        response = client.post("/scan", json={"package": "test", "version": "1.0.0"})
        assert response.status_code == 200
        assert response.json() == {"package": "test", "version": "1.0.0"}

    def test_scan_missing_version(self):
        response = client.post("/scan", json={"package": "test"})
        assert response.status_code == 422

    def test_scan_invalid_version(self):
        response = client.post("/scan", json={"package": "test", "version": 123})
        assert response.status_code == 422
