from flask import Blueprint, request, jsonify, make_response
from flask_cors import CORS
from app.api.utils import get_col, auth_required, log

midigator_api_v1 = Blueprint(
    'midigator_api_v1', 'midigator_api_v1', url_prefix='/api/v1/midigator')
CORS(midigator_api_v1)


@midigator_api_v1.route('/', methods=['GET'])
@auth_required
def api_hello():
    request_json = get_request_json(request)
    response_body = {
        "greetings": "you have setup flask successfully! you need to install mongodb if you haven't done so!",
        "page": 0,
    }
    return create_response(request.path, response_body, 200)


@midigator_api_v1.route('/', methods=['POST'])
@auth_required
def api_registration_new():
    request_json = get_request_json(request)
    response_body = {'ack': f'successfully received {request.path}!'}
    return create_response(request.path, response_body, 200)


@midigator_api_v1.route('/chargeback-new-event', methods=['POST'])
@auth_required
def api_chargeback_new():
    request_json = get_request_json(request)
    response_body = {'ack': f'successfully received {request.path}!'}
    return create_response(request.path, response_body, 200)


@midigator_api_v1.route('/chargeback-match-event', methods=['POST'])
@auth_required
def api_chargeback_match():
    request_json = get_request_json(request)
    response_body = {'ack': f'successfully received {request.path}!'}
    return create_response(request.path, response_body, 200)


@midigator_api_v1.route('/order-validation-new-event', methods=['POST'])
@auth_required
def api_order_validation_new():
    request_json = get_request_json(request)
    response_body = {'ack': f'successfully received {request.path}!'}
    return create_response(request.path, response_body, 200)


@midigator_api_v1.route('/order-validation-match-event', methods=['POST'])
@auth_required
def api_order_validation_match():
    request_json = get_request_json(request)
    response_body = {'ack': f'successfully received {request.path}!'}
    return create_response(request.path, response_body, 200)


@midigator_api_v1.route('/prevention-new-event', methods=['POST'])
@auth_required
def api_prevention_new():
    request_json = get_request_json(request)
    response_body = {'ack': f'successfully received {request.path}!'}
    return create_response(request.path, response_body, 200)


@midigator_api_v1.route('/prevention-match-event', methods=['POST'])
@auth_required
def api_prevention_match():
    request_json = get_request_json(request)
    response_body = {'ack': f'successfully received {request.path}!'}
    return create_response(request.path, response_body, 200)


@midigator_api_v1.route('/order', methods=['GET'])
@auth_required
def api_get_orders():
    request_json = get_request_json(request)
    order = get_col('orders', 'sticky').find_one({})
    response_body = {
        "order": dict(order),
        "page": 0,
    }
    return create_response(request.path, response_body, 200)


@midigator_api_v1.route('/user', methods=['GET'])
@auth_required
def api_get_user():
    request_json = get_request_json(request)
    user = get_col('EmailUnsubscriber', 'user').find_one({})
    response_body = {
        "user": dict(user),
        "page": 0,
    }
    return create_response(request.path, response_body, 200)


def get_request_json(req):
    request_json = req.get_json()
    log({f"received request in {req.path}": request_json})
    return request_json


def create_response(path, response_body, status_code=200):
    response = make_response(jsonify(response_body), status_code)
    log({f"send response in {path} with code {status_code}": response.json})
    return response
