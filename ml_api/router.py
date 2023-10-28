from typing import Callable

from fastapi import APIRouter, Depends

from ml_api import schema, service, dependency

route = APIRouter()


@route.post("/predict")
def predict(input_objects: list[schema.InputObject],
            vectorize_func: Callable[[schema.InputObject], list] = Depends(dependency.get_vectorize_func),
            predict_func: Callable[[list], int] = Depends(dependency.get_predict_func)) -> list[schema.Prediction]:
    return service.ml_prediction(input_objects, vectorize_func, predict_func)
