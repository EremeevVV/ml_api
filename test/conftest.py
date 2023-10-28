from pytest import fixture
from fastapi.testclient import TestClient

from ml_api.run_api import create_app


@fixture
def client() -> TestClient:
    app = create_app()
    return TestClient(app)


@fixture
def batch() -> list[dict[str, str]]:
    return [{},{}]