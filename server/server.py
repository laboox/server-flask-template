
import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from flask_security import MongoEngineUserDatastore
from http import HTTPStatus
from werkzeug.exceptions import HTTPException
from mongoengine import NotUniqueError
import traceback, sys
from getpass import getpass
import click

def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is not None:
        app.config.from_mapping(test_config)

    app.config.from_pyfile('config.py')

    if test_config is not None:
        app.config.from_mapping(test_config)

    cors = CORS(app, resources={r'/api/*': {'origins': '*'}})

    from .core import db, security
    db.init_app(app)

    from .models import User, Role 
    user_datastore = MongoEngineUserDatastore(db, User, Role)
    security.init_app(app, user_datastore)

    from .controllers import auth_controller
    app.register_blueprint(auth_controller, url_prefix='/api/auth')
    from .controllers import test_controller
    app.register_blueprint(test_controller, url_prefix='/api/test')

    @app.route('/api/hello', methods=['GET'])
    def home():
        return jsonify({'message': 'Hello'})

    @app.after_request
    def apply_headers(response):
        response.headers["Content-Type"] = "application/json"
        return response

    @app.cli.command()
    @click.argument('adminPassword')
    def initdb(adminpassword):
        
        Role.objects(name='admin').update(name='admin', upsert=True)
        superId = Role.objects.get(name='admin')
        Role.objects(name='user').update(name='user', upsert=True)
        userId = Role.objects.get(name='user')

        User.objects(email='admin').update(email='admin', roles= [superId, \
                userId], password=adminpassword, upsert=True)

    @app.errorhandler(Exception)
    def handle_error(e):
        code = 500
        if isinstance(e, HTTPException):
            code = e.code
        elif isinstance(e, NotUniqueError):
            code = HTTPStatus.CONFLICT
        else:
            ex_type, ex, tb = sys.exc_info()
            traceback.print_tb(tb)
            print(e)
        return jsonify(error=str(e)), code

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
