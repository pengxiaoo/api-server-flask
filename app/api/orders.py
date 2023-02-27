from flask import Blueprint, request, jsonify
from app.database import mongo
from flask_cors import CORS
from app.api.utils import expect
from datetime import datetime

orders_api_v1 = Blueprint(
    'orders_api_v1', 'orders_api_v1', url_prefix='/api/v1/orders')
CORS(orders_api_v1)


def get_col(col_name, db_name='sticky'):
    return mongo.cx[db_name][col_name]


@orders_api_v1.route('/', methods=['GET'])
def api_get_orders():
    order = get_col('orders').find_one({})
    response = {
        "order": dict(order),
        "page": 0,
    }
    return jsonify(response)


@orders_api_v1.route('/user', methods=['GET'])
def api_get_user():
    user = get_col('EmailUnsubscriber', 'user').find_one({})
    response = {
        "user": dict(user),
        "page": 0,
    }
    return jsonify(response)
