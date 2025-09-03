from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flasgger import Swagger

from api.config import env_config

from flask_sqlalchemy import SQLAlchemy

api = Api()

db = SQLAlchemy()

# define function that takes in configuration

def create_app(config_name):
    import resources
    # create flask application itself
    app = Flask(__name__)

    # take in environmental config & get configuration name as a key
    app.config.from_object(env_config[config_name])

    # initialize the application
    api.init_app(app)
    db.init_app(app)
    # add cors and swagger documentation
    CORS(app)
    Swagger(app)

    return app


