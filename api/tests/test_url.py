import unittest
from unittest.mock import patch
from .. import create_app
from ..config.config import config_dict
from ..utils import db
from flask_jwt_extended import create_access_token, get_jwt_identity
from ..models.url import Url
from ..models.user import User
from ..models.click import Click


class UserTestCase(unittest.TestCase):
    
        def setUp(self) -> None:
            self.app = create_app(config=config_dict['test'])
    
            self.appctx = self.app.app_context()
    
            self.appctx.push()
    
            self.client = self.app.test_client()
    
            db.create_all()
    
        def tearDown(self) -> None:
            db.drop_all()
    
            self.appctx.pop()
    
            self.app = None
    
            self.client = None
    
        def test_create_url(self):
            # Mock the JWT identity
            with patch('flask_jwt_extended.view_decorators.get_jwt_identity', return_value='user@example.com'):
                # Prepare the request data
                data = {
                    'long_url': 'https://example.com',
                    'custom_domain': 'example.com'
                }
                headers = {'Content-Type': 'application/json'}

                # Send a POST request to the endpoint
                response = self.client.post('/create', json=data, headers=headers)

                # Assert the response
                self.assertEqual(response.status_code, 201)
                response_data = response.get_json()
                self.assertEqual(response_data['long_url'], 'https://example.com')
                self.assertEqual(response_data['custom_domain'], 'example.com')
                self.assertEqual(response_data['user_id'], 'user@example.com')
            # Add more assertions as needed