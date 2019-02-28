
def test_private(client, auth):
    token = auth.login('admin', 'TEST_PASS')
    rv = client.get('api/test/myprivatestuff', \
            headers={'Authorization': token}) 
    json = rv.get_json()
    assert 'email' in json and json['email'] == 'admin'
