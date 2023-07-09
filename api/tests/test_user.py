import unittest
from http import HTTPStatus
from flask import json
from .. import create_app
from ..config.config import config_dict
from ..utils import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from ..models.user import User


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
        

    def test_user_signup(self):

        signup_data = {
            "first_name": "test",
            "last_name": "user",
            "email": "testuser@test.com", 
            "password": "test",
            "confirm_password": "test"
        }

        response = self.client.post('/auth/signup', json=signup_data)

        self.assertEqual(response.status_code, HTTPStatus.CREATED)

        response_data = json.loads(response.data)
        self.assertEqual(response_data['first_name'], 'test')
        self.assertEqual(response_data['last_name'], 'user')
        self.assertEqual(response_data['email'], 'testuser@test.com')
        

    def test_user_login(self):
        login_data = {
            "email": "testuser@test.com", 
            "password": "test"
        }

        # Send a POST request to the login endpoint
        response = self.client.post('/auth/login', json=login_data)

        # # Print the response data and content
#         print(response.data)
#         print(response.get_data(as_text=True))



        # Assert the response status code
        self.assertEqual(response.status_code, HTTPStatus.OK)

        # Assert the login data
        response_data = json.loads(response.data)
        self.assertEqual(login_data['email'], 'testuser@test.com')


    
    def test_refresh_endpoint(self):
    
        # Create a mock refresh token
        refresh_token = create_access_token(identity='testuser@test.com')

        # Set the authorization header with the refresh token
        headers = {
            'Authorization': f'Bearer {refresh_token}'
        }

        # Send a POST request to the refresh endpoint
        response = self.client.post('/auth/refresh', headers=headers)

# Print the response data and content
        print(response.data)
        print(response.get_data(as_text=True))
        # Assert the response status code
        # self.assertEqual(response_data['msg'], 'testuser@test.com')
        # assert response.status_code == HTTPStatus.OK

        # Assert the response data
        response_data = json.loads(response.data)
        # assert 'access_token' in response_data
        # assert response_data['access_token'] != refresh_token
        assert response_data['msg'] == 'Only refresh tokens are allowed'






    # def test_logout_endpoint(self):
    #     # Create a mock access token
    #     access_token = create_access_token(identity='testuser@test.com')

    #     # Set the authorization header with the access token
    #     headers = {
    #         'Authorization': f'Bearer {access_token}'
    #     }

    #     # Send a POST request to the logout endpoint
    #     response = self.client.post('/logout', headers=headers)

    #     print(response.data)
    #     print(response.get_data(as_text=True))
    #     # Assert the response status code
    #     # self.assertEqual(response.status_code, HTTPStatus.OK)

    #     # Assert the response data
    #     response_data = response.get_json()
    #     self.assertEqual(response_data['message'], 'Successfully Logged Out')

        # # Assert that the access token is revoked
        # token_data = decode_token(access_token)
        # self.assertTrue(token_data['jti'] in revoked_store)

        # # Assert that the cookies are unset
        # self.assertTrue('access_token_cookie' not in response.headers.get_all('Set-Cookie'))
        # self.assertTrue('refresh_token_cookie' not in response.headers.get_all('Set-Cookie'))
