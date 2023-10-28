from typing import Callable, Generator
from random import randint

from ml_api import schema


def to_vector(input_object: schema.InputObject) -> list[float | int | bool]:
    """Функция должна превращать в pydantic Basemodel в вектор признаков, без идентификатора"""
    return list(input_object.model_dump(exclude={'identity'}).values())


def predict(input_vector: list) -> int:
    """Fake model prediction"""
    return randint(0, 10)


def get_predict_func() -> Generator[Callable[[list], int], None, None]:
    prediction_func = predict
    try:
        yield prediction_func
    finally:
        pass


def get_vectorize_func() -> Generator[Callable[[schema.InputObject], list], None, None]:
    vectorize_func = to_vector
    try:
        yield vectorize_func
    finally:
        pass