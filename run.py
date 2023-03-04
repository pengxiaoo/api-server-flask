from app.factory import create_app
import os
import configparser

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))

if __name__ == "__main__":
    mongo_uri = config['PROD']['DB_URI']
    app = create_app(mongo_uri)
    app.config['DEBUG'] = True
    app.config['MONGO_URI'] = mongo_uri
    app.run(host="0.0.0.0", debug=False)
