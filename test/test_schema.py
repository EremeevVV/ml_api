from uuid import uuid1
from math import nan, inf

from ml_api import schema


def test_has_nan_or_inf_positive():
    given = schema.InputObject(feature1=nan, feature2=inf, feature3=1, feature4=False, identity=uuid1())
    assert given.has_nan_or_inf()


def test_has_nan_or_inf_negative():
    given = schema.InputObject(feature1=0.1, feature2=0.2, feature3=1, feature4=False, identity=uuid1())
    assert not given.has_nan_or_inf()


def test_has_nan_or_inf_positive_inf():
    given = schema.InputObject(feature1=0.1, feature2=inf, feature3=1, feature4=False, identity=uuid1())
    assert given.has_nan_or_inf()


def test_has_nan_or_inf_positive_nan():
    given = schema.InputObject(feature1=0.1, feature2=nan, feature3=1, feature4=False, identity=uuid1())
    assert given.has_nan_or_inf()

