def test_homepage_StatusCode(client):
    resp = client.get('/')
    assert resp.status_code == 200