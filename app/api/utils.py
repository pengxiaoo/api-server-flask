from flask import request, make_response
from app.database import mongo
from functools import wraps
import os

(username, password) = (os.environ['MIDIGATOR_SANDBOX_USERNAME'], os.environ['MIDIGATOR_SANDBOX_PASSWORD'])


def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == username and auth.password == password:
            return f(*args, **kwargs)
        return make_response('basic auth failed, check your username and password!', 401)

    return decorated


def get_col(col_name, db_name='midigator'):
    return mongo.cx[db_name][col_name]


def expect(input, expectedType, field):
    if isinstance(input, expectedType):
        return input
    raise AssertionError("Invalid input for type", field)
