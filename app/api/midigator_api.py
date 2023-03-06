from flask import Blueprint, request, jsonify, make_response
from app.database import mongo
from flask_cors import CORS
from functools import wraps
from app.api.utils import expect
from datetime import datetime

midigator_api_v1 = Blueprint(
    'midigator_api_v1', 'midigator_api_v1', url_prefix='/api/v1/midigator')
CORS(midigator_api_v1)


def get_col(col_name, db_name='midigator'):
    return mongo.cx[db_name][col_name]


def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == 'username' and auth.password == 'password':
            return f(*args, **kwargs)
        return make_response('basic auth failed, check your username and password!', 401)

    return decorated


@midigator_api_v1.route('/', methods=['GET'])
def api_hello():
    response = {
        "greetings": "you have setup flask successfully! you need to install mongodb if you haven't done so!",
        "page": 0,
    }
    return make_response(jsonify(response), 200)


@midigator_api_v1.route('/', methods=['POST'])
def api_registration_new():
    body = request.get_json()
    print(body)
    data = {'ack': 'successfully received registration-new-event!'}
    return make_response(jsonify(data), 200)


@midigator_api_v1.route('/chargeback-new-event', methods=['POST'])
def api_chargeback_new():
    body = request.get_json()
    print(body)
    data = {'ack': 'successfully received chargeback-new-event!'}
    return make_response(jsonify(data), 200)


@midigator_api_v1.route('/chargeback-match-event', methods=['POST'])
def api_chargeback_match():
    body = request.get_json()
    print(body)
    data = {'ack': 'successfully received chargeback-match-event!'}
    return make_response(jsonify(data), 200)


@midigator_api_v1.route('/order-validation-new-event', methods=['POST'])
def api_order_validation_new():
    body = request.get_json()
    print(body)
    data = {'ack': 'successfully received order-validation-new-event!'}
    return make_response(jsonify(data), 200)


@midigator_api_v1.route('/order-validation-match-event', methods=['POST'])
def api_order_validation_match():
    body = request.get_json()
    print(body)
    data = {'ack': 'successfully received order-validation-match-event!'}
    return make_response(jsonify(data), 200)


@midigator_api_v1.route('/prevention-new-event', methods=['POST'])
def api_prevention_new():
    body = request.get_json()
    print(body)
    data = {'ack': 'successfully received prevention-new-event!'}
    return make_response(jsonify(data), 200)


@midigator_api_v1.route('/prevention-match-event', methods=['POST'])
def api_prevention_match():
    body = request.get_json()
    print(body)
    data = {'ack': 'successfully received prevention-match-event!'}
    return make_response(jsonify(data), 200)


@midigator_api_v1.route('/order', methods=['GET'])
@auth_required
def api_get_orders():
    order = get_col('orders', 'sticky').find_one({})
    response = {
        "order": dict(order),
        "page": 0,
    }
    return jsonify(response)


@midigator_api_v1.route('/user', methods=['GET'])
@auth_required
def api_get_user():
    user = get_col('EmailUnsubscriber', 'user').find_one({})
    response = {
        "user": dict(user),
        "page": 0,
    }
    return jsonify(response)
