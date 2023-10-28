from typing import Callable

from ml_api import schema


def ml_prediction(input_objects: list[schema.InputObject],
                  vectorize_func: Callable[[schema.InputObject], list],
                  predict_func: Callable[[list], int]) -> list[schema.Prediction]:
    predictions: list[schema.Prediction] = []
    for input_object in input_objects:
        vector = vectorize_func(input_object)
        predicted_label = predict_func(vector)
        predictions.append(schema.Prediction(identity=input_object.identity,
                                             label=predicted_label,
                                             ))
    return predictions
