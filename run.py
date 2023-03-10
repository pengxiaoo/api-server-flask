from app.factory import create_app
import settings

mongo_uri = settings.DB_URI
app = create_app(mongo_uri)
app.config['DEBUG'] = True
app.config['MONGO_URI'] = mongo_uri

if __name__ == "__main__":
    app.run(host="0.0.0.0")
