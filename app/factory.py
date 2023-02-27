import os
from flask import Flask
from flask.json import JSONEncoder
from flask_cors import CORS
##from flask_bcrypt import Bcrypt
##from flask_jwt_extended import JWTManager
from bson import json_util, ObjectId
from datetime import datetime, timedelta
from app.api.movies import movies_api_v1
from app.api.orders import orders_api_v1


class MongoJsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%m/%d/%Y-%H:%M:%S')
        if isinstance(obj, ObjectId):
            return str(obj)
        return json_util.default(obj, json_util.CANONICAL_JSON_OPTIONS)


def create_app():
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    app = Flask(__name__)
    CORS(app)
    app.json_encoder = MongoJsonEncoder
    app.register_blueprint(movies_api_v1)
    app.register_blueprint(orders_api_v1)

    @app.route('/')
    def home():
        return "Hello, World!"

    return app
