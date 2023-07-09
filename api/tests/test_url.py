from datetime import datetime
import unittest
from unittest.mock import patch
from .. import create_app
from ..config.config import config_dict
from ..utils import db
from flask_jwt_extended import create_access_token, get_jwt_identity
from ..models.url import Url
from ..models.user import User
from ..models.click import Click
from http import HTTPStatus
from flask import json
import io
from PIL import Image


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
    
        # def test_create_url(self):
        #     # Mock the JWT identity
        #     with patch('flask_jwt_extended.view_decorators.get_jwt_identity', return_value='user@example.com'):
        #         # Prepare the request data
        #         data = {
        #             'long_url': 'https://example.com',
        #             'custom_domain': 'example.com'
        #         }
        #         headers = {'Content-Type': 'application/json'}

        #         # Send a POST request to the endpoint
        #         response = self.client.post('/create', json=data, headers=headers)

        #         # Assert the response
        #         self.assertEqual(response.status_code, 201)
        #         response_data = response.get_json()
        #         self.assertEqual(response_data['long_url'], 'https://example.com')
        #         self.assertEqual(response_data['custom_domain'], 'example.com')
        #         self.assertEqual(response_data['user_id'], 'user@example.com')
        #     # Add more assertions as needed

    def test_dashboard_endpoint(self):
    # Create a mock user
        user = User(
            id=0,
            uuid='1234567890123456',
            first_name='John',
            last_name='Doe',
            email='johndoe@test.com',
            password_hash='hashed_password',
            is_verified=True
        )
        db.session.add(user)
        db.session.commit()

        # Generate a JWT access token for the user
        access_token = create_access_token(identity=user.email)

        # Set the authorization header with the access token
        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        # Send a GET request to the dashboard endpoint
        response = self.client.get('/url/dashboard', headers=headers)

        print(response.data)
        print(response.get_data(as_text=True))

        # Assert the response status code
        self.assertEqual(response.status_code, HTTPStatus.OK)

        # Assert the response data
        response_data = json.loads(response.data)
        self.assertEqual(response_data['first_name'], 'John')
        self.assertEqual(response_data['total_urls'], 0)
        self.assertEqual(response_data['total_clicks'], 0)


    def test_create_url_endpoint(self):
        # Create a mock user
        user = User(
            id=0,
            uuid='1234567890123456',
            first_name='John',
            last_name='Doe',
            email='johndoe@test.com',
            password_hash='hashed_password',
            is_verified=True
        )
        db.session.add(user)
        db.session.commit()

        # Generate a JWT access token for the user
        access_token = create_access_token(identity=user.email)

        # Set the authorization header with the access token
        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        # Prepare the request payload
        payload = {
            'long_url': 'https://www.example.com'
        }

        # Send a POST request to the create URL endpoint
        response = self.client.post('/url/create', json=payload, headers=headers)

        print(response.data)
        print(response.get_data(as_text=True))

        # Assert the response status code
        self.assertEqual(response.status_code, HTTPStatus.CREATED)

        # Assert the response data
        response_data = json.loads(response.data)
        self.assertIn('long_url', response_data)
        self.assertIn('short_code', response_data)
        self.assertIn('short_url', response_data)
        self.assertEqual(response_data['long_url'], 'https://www.example.com')
        # self.assertEqual(response_data['user_id'], 'johndoe@test.com')


    def test_redirect_url_endpoint(self):
        # Create a mock URL
        url = Url(
            id=0,
            uuid=1234567890123456,
            long_url='https://www.example.com',
            short_code='abcd1234',
            short_url='http://localhost:5000/url/abcd1234',
            user_id='johndoe@test.com'
        )
        db.session.add(url)
        db.session.commit()

        # Send a GET request to the redirect URL endpoint
        response = self.client.get('/url/abcd1234')

        # Assert the response status code
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

        # Assert the response headers
        self.assertIn('Location', response.headers)
        self.assertEqual(response.headers['Location'], 'https://www.example.com')



    def test_custom_url_endpoint(self):
        # Create a mock URL
        url = Url(
            id=0,
            uuid=1234567890123456,
            long_url='https://www.example.com',
            short_code='abcd1234',
            short_url='http://localhost:5000/url/abcd1234',
            custom_domain=None,
            custom_url=None,
            user_id='johndoe@test.com'
        )
        db.session.add(url)
        db.session.commit()

        # Set the authorization header with a valid JWT
        access_token = create_access_token(identity='johndoe@test.com')
        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        # Send a PATCH request to the custom URL endpoint
        data = {
            'custom_domain': 'customdomain.com'
        }
        response = self.client.patch('/url/custom/abcd1234', json=data, headers=headers)

        # Assert the response status code
        self.assertEqual(response.status_code, HTTPStatus.CREATED)

        # Assert the response data
        response_data = response.get_json()
        # self.assertEqual(response_data['custom_domain'], 'customdomain.com')
        self.assertEqual(response_data['custom_url'], 'https://customdomain.com/url/abcd1234')


    def test_all_urls_endpoint(self):
        # Create a mock user
        user = User(
            id=0,
            uuid='1234567890123456',
            email='johndoe@test.com',
            password_hash='hashed_password',
            first_name='John',
            last_name='Doe',
            is_verified=True
        )
        db.session.add(user)
        db.session.commit()

        # Create mock URLs associated with the user
        url1 = Url(
            id=0,
            uuid=1234567890123456,
            long_url='https://www.example1.com',
            short_code='abcd1234',
            short_url='http://localhost:5000/url/abcd1234',
            custom_domain=None,
            custom_url=None,
            user_id=user.email
        )
        url2 = Url(
            id=1,
            uuid=2345678901234567,
            long_url='https://www.example2.com',
            short_code='efgh5678',
            short_url='http://localhost:5000/url/efgh5678',
            custom_domain=None,
            custom_url=None,
            user_id=user.email
        )
        db.session.add_all([url1, url2])
        db.session.commit()

        # Set the authorization header with a valid JWT
        access_token = create_access_token(identity='johndoe@test.com')
        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        # Send a GET request to the all URLs endpoint
        response = self.client.get('/url/urls', headers=headers)

        # Assert the response status code
        self.assertEqual(response.status_code, HTTPStatus.OK)

        # Assert the response data
        response_data = response.get_json()
        self.assertEqual(len(response_data), 2)
        self.assertEqual(response_data[0]['long_url'], 'https://www.example1.com')
        self.assertEqual(response_data[1]['long_url'], 'https://www.example2.com')


    def test_url_analytics_endpoint(self):
        # Create a mock URL
        url = Url(
            id=0,
            uuid=1234567890123456,
            long_url='https://www.example.com',
            short_code='abcd1234',
            short_url='http://localhost:5000/url/abcd1234',
            custom_domain=None,
            custom_url=None,
            user_id='johndoe@test.com'
        )
        db.session.add(url)
        db.session.commit()

        # Create mock clicks associated with the URL
        click1 = Click(
            url_id=url.id,
            timestamp=datetime.now(),
            ip_address='127.0.0.1',
            referrer='http://www.example.com',
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        )
        click2 = Click(
            url_id=url.id,
            timestamp=datetime.now(),
            ip_address='127.0.0.1',
            referrer='http://www.example.com',
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        )
        db.session.add_all([click1, click2])
        db.session.commit()

        # Set the authorization header with a valid JWT
        access_token = create_access_token(identity='johndoe@test.com')
        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        # Send a GET request to the URL analytics endpoint
        response = self.client.get('/url/analytics/abcd1234', headers=headers)

        # Assert the response status code
        self.assertEqual(response.status_code, HTTPStatus.OK)

        # Assert the response data
        response_data = response.get_json()
        self.assertEqual(response_data['short_code'], 'abcd1234')
        self.assertEqual(len(response_data['clicks']), 2)
        self.assertEqual(response_data['clicks'][0]['referrer'], 'http://www.example.com')
        self.assertEqual(response_data['clicks'][1]['referrer'], 'http://www.example.com')



    def test_qr_code_endpoint(self):
        # Create a mock URL
        url = Url(
            id=0,
            uuid=1234567890123456,
            long_url='https://www.example.com',
            short_code='abcd1234',
            short_url='http://localhost:5000/url/abcd1234',
            custom_domain=None,
            custom_url=None,
            user_id='johndoe@test.com'
        )
        db.session.add(url)
        db.session.commit()

        # Set the authorization header with a valid JWT
        access_token = create_access_token(identity='johndoe@test.com')
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'image/png',
            # 'Content-Disposition': 'attachment; filename=qrcode.png'
        }

        # Send a GET request to the QR code endpoint
        response = self.client.get('/url/qr-code/abcd1234')

        # Assert the response status code
        self.assertEqual(response.status_code, HTTPStatus.OK)

        # Assert the response headers
        self.assertIn('Content-Type', response.headers)
        self.assertEqual(response.headers['Content-Type'], 'image/png')
        # self.assertIn('Content-Disposition', response.headers)
        # self.assertEqual(response.headers['Content-Disposition'], 'attachment; filename=qrcode.png')

        # Assert the response data
        qr_code_image = Image.open(io.BytesIO(response.data))
        self.assertIsNotNone(qr_code_image)
        # Add further assertions on the QR code image if necessary
