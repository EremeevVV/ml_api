from uuid import uuid1

from ml_api import schema, dependency

def test_to_vector():
    expected = [0.1, 0.2, 3, True]
    given = schema.InputObject(feature1=expected[0],
                               feature2=expected[1],
                               feature3=expected[2],
                               feature4=expected[3],
                               identity=uuid1()
                               )
    result = dependency.to_vector(given)
    assert expected == result