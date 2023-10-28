from fastapi import APIRouter

from ml_api import schema, service

route = APIRouter()


@route.post("/predict")
def predict(input_objects: list[schema.InputObject]) -> list[schema.Prediction]:
    return service.ml_prediction(input_objects)
