
import os
from flask import Flask, jsonify
from .controllers import *
from .models import *
from .core import db, security
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from flask_security import MongoEngineUserDatastore
from http import HTTPStatus
from werkzeug.exceptions import HTTPException
from mongoengine import NotUniqueError
import traceback, sys

app = Flask(__name__)

app.config.from_pyfile('config.cfg')

db.init_app(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

user_datastore = MongoEngineUserDatastore(db, User, Role)

security.init_app(app, user_datastore)

app.register_blueprint(auth_controller, url_prefix='/api/auth')
app.register_blueprint(test_controller, url_prefix='/api/test')

@app.route('/hello')
def home():
    return jsonify({'message': 'Hello'})

@app.after_request
def apply_headers(response):
    response.headers["Content-Type"] = "application/json"
    return response

@app.cli.command()
def initdb():
    Role.objects(name='admin').update(name='admin', upsert=True)
    superId = Role.objects.get(name='admin')
    Role.objects(name='user').update(name='user', upsert=True)
    userId = Role.objects.get(name='user')

    User.objects(email='admin').update(email='admin', roles= [superId, \
            userId], password='myBigSuperAdmin', upsert=True)

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


if __name__ == '__main__':
    if(os.environ['SERVER_PROD']!=None):
        app.run(host='0.0.0.0', port=80)
    else:
        app.run()
