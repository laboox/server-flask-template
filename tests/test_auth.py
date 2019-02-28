
def test_login(client, auth):
    token = auth.login('admin', 'TEST_PASS')
    assert token

