
import os
import tempfile

import pytest

from server import create_app
from flask import jsonify, session 

from mongoengine import connect

@pytest.fixture(scope='session')
def client():
    app = create_app(dict(MONGODB_DB='justtest', TESTING=True))
    client = app.test_client()

    runner = app.test_cli_runner()
    print(runner.invoke(args=['initdb', 'TEST_PASS']).output)

    yield client

    db = connect('justtest')
    db.drop_database('justtest')

class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, email='test', password='test'):
        rv = self._client.post('/api/auth/login', json=dict(
            email=email,
            password=password
        ))
        assert 'authentication_token' in rv.get_json()
        token = rv.get_json()['authentication_token']
        return token

@pytest.fixture(scope='session')
def auth(client):
    return AuthActions(client)


