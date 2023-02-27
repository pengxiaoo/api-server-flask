from flask import Blueprint, request, jsonify
from app.db import get_a_order
from flask_cors import CORS
from app.api.utils import expect
from datetime import datetime

orders_api_v1 = Blueprint(
    'orders_api_v1', 'orders_api_v1', url_prefix='/api/v1/orders')
CORS(orders_api_v1)


@orders_api_v1.route('/', methods=['GET'])
def api_get_orders():
    order = get_a_order()
    response = {
        "order": order,
        "page": 0,
    }
    return jsonify(response)
