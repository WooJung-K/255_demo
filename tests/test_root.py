# using the built-in unittest
import unittest

# leverage generic class for case classes
from unittest import TestCase

# import API app that we are going to test 
from api.app import create_app, db


class UserTestCase(TestCase):
    def setUp(self):
      # instantiate the application
        self.app = create_app("testing")
      # grab context for the application
        self.app_context = self.app.app_context() 
        self.app_context.push()
        db.create_all()
      # create client object
        self.client = self.app.test_client(use_cookies=True)


    def tearDown(self):
      # remove/drop/clear out the application
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


    def test_root_response(self):
      # getting response from the api - as a good request
        response = self.client.get("/", headers = {"Content-Type": "application/json"},)
      
      # ensure that the response HTTP code is 200
        self.assertEqual(response.status_code, 200)
