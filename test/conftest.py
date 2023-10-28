from uuid import uuid1

from pytest import fixture
from fastapi.testclient import TestClient

from ml_api.run_api import create_app


@fixture
def client() -> TestClient:
    app = create_app()
    return TestClient(app)


@fixture
def batch() -> list[dict[str, str | float | int | bool]]:
    return [
        {
            'feature1': 0.2,
            'feature2': 0.3,
            'feature3': 31,
            'feature4': False,
            'identity': f'{uuid1()}',
        },
        {
            'feature1': 0.2,
            'feature2': 0.3,
            'feature3': 31,
            'feature4': False,
            'identity': f'{uuid1()}',
        },
        {
            'feature1': 0.2,
            'feature2': 0.3,
            'feature3': 31,
            'feature4': False,
            'identity': f'{uuid1()}',
        },
    ]
