from math import nan
from uuid import uuid1

from ml_api import service, schema


def test_ml_prediction():
    given = [schema.InputObject(feature1=0.1, feature2=0.2, feature3=3, feature4=True, identity=uuid1()),
             schema.InputObject(feature1=nan, feature2=0.2, feature3=3, feature4=True, identity=uuid1()),
             schema.InputObject(feature1=0.1, feature2=0.2, feature3=3, feature4=True, identity=uuid1()),
             ]
    result = service.ml_prediction(given, service.function_must_be_replaced)
    assert len(result) == len(given)
    assert isinstance(result[0], schema.Prediction)
    assert result[1].label is None