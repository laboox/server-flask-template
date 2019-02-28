
def test_hello(client):
    rv = client.get('/api/hello')
    assert {'message': 'Hello'}, rv.get_json()


