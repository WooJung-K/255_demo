# resource handler

from flask_restful import Resource

from api.app import api

# create default class
class DefaultResource(Resource):
    def get(self):
        return {"status": "success", "data": {"msg": "Hello world"}}

    def post(self):
      # placeholder return phrase
        return {"status": "success", "data": {"msg": "Hello World"}}

# add this resource to the api as a root endpoint
api.add_resource(DefaultResource, "/", endpoint = "home")
