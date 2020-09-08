import json


def test_create_quote(client):
    response = client.post(
        '/quote/create',
        data=json.dumps(dict(
            author='nimra',
            quote='we\'re testing stage'
        )),
        content_type='application/json',
    )
    data = json.loads(response.data.decode())
    assert response.status_code == 201
    assert 'success' in data['message']

