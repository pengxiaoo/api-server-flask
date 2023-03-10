from flask import Flask, jsonify, request, make_response
from flask.json import JSONEncoder
from flask_cors import CORS
##from flask_bcrypt import Bcrypt
##from flask_jwt_extended import JWTManager
from bson import json_util, ObjectId
from datetime import datetime
from app.api.midigator_api import midigator_api_v1
from app.database import mongo


class MongoJsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%m/%d/%Y-%H:%M:%S')
        if isinstance(obj, ObjectId):
            return str(obj)
        return json_util.default(obj, json_util.CANONICAL_JSON_OPTIONS)


def create_app(mongo_uri):
    app = Flask(__name__)
    mongo.init_app(app, uri=mongo_uri)
    CORS(app)
    app.json_encoder = MongoJsonEncoder
    app.register_blueprint(midigator_api_v1)

    @app.route('/')
    def home():
        data = {'ack': 'successfully received /!'}
        print(data)
        return make_response(jsonify(data), 200)

    return app
