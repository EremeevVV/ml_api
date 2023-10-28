def test_predict(client, batch):
    response = client.post('/predict', json=batch)
    assert response.status_code == 200
    result = response.json()
    assert len(result) == len(batch)
    for pred in result:
        label = pred.get('label')
        assert isinstance(label, int)
