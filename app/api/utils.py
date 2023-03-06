from flask import request, make_response
from app.database import mongo
from functools import wraps
import os
import logging

logging.basicConfig(filename='record.log',
                    level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


def log(text, level='WARNING'):
    if level == 'WARNING':
        logging.warning(text)
    elif level == 'ERROR':
        logging.error(text)


(username, password) = (os.environ['MIDIGATOR_SANDBOX_USERNAME'], os.environ['MIDIGATOR_SANDBOX_PASSWORD'])


def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == username and auth.password == password:
            return f(*args, **kwargs)
        response = make_response('basic auth failed, check your username and password!', 401)
        log({f"send response in {request.path} with code {response.status_code}": response.data})
        return response

    return decorated


def get_col(col_name, db_name='midigator'):
    return mongo.cx[db_name][col_name]
