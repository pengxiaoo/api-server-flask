from flask import Blueprint, request, jsonify, make_response
from app.database import mongo
from flask_cors import CORS
from app.api.utils import expect
from datetime import datetime

midigator_api_v1 = Blueprint(
    'midigator_api_v1', 'midigator_api_v1', url_prefix='/api/v1/midigator')
CORS(midigator_api_v1)


def get_col(col_name, db_name='midigator'):
    return mongo.cx[db_name][col_name]


@midigator_api_v1.route('/registration-new-event', methods=['POST'])
def api_registration_new():
    body = request.get_json()
    print(body)
    data = {'ack': 'successfully received registration-new-event!'}
    return make_response(jsonify(data), 200)


@midigator_api_v1.route('/order-validation-new-event', methods=['POST'])
def api_order_validation_new():
    body = request.get_json()
    print(body)
    data = {'ack': 'successfully received order-validation-new-event!'}
    return make_response(jsonify(data), 200)


@midigator_api_v1.route('/chargeback-new-event', methods=['POST'])
def api_chargeback_new():
    body = request.get_json()
    print(body)
    data = {'ack': 'successfully received chargeback-new-event!'}
    return make_response(jsonify(data), 200)


@midigator_api_v1.route('/order', methods=['GET'])
def api_get_orders():
    order = get_col('orders', 'sticky').find_one({})
    response = {
        "order": dict(order),
        "page": 0,
    }
    return jsonify(response)


@midigator_api_v1.route('/user', methods=['GET'])
def api_get_user():
    user = get_col('EmailUnsubscriber', 'user').find_one({})
    response = {
        "user": dict(user),
        "page": 0,
    }
    return jsonify(response)
