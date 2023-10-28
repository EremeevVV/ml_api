from typing import Callable
from random import randint

from ml_api import schema

function_must_be_replaced = lambda x: randint(0, 10)


def ml_prediction(input_objects: list[schema.InputObject],
                  prediction_function: Callable[[list], int] = function_must_be_replaced) -> list[schema.Prediction]:
    predicitons: list[schema.Prediction] = []
    for el in input_objects:
        if el.has_nan_or_inf():
            predicted_label = None
        else:
            predicted_label = prediction_function(el.list())
        predicitons.append(schema.Prediction(identity=el.identity,
                                             label=predicted_label,
                                             ))
    return predicitons
