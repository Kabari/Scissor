import unittest
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

        data = {
            "first_name": "test",
            "last_name": "user",
            "email": "testuser@test.com", 
            "password": "test"
        }

        response = self.client.post('/auth/signup', json=data)

        user = User.query.filter_by(email="testuser@test.com").first()

        assert user.first_name == 'test'
        assert user.last_name == 'user'
        assert user.email == 'testuser@test.com'

        assert response.status_code == 201
        

    def test_user_login(self):
        data = {
            "email": "testuser@test.com", 
            "password": "test"
        }

        response = self.client.post('/auth/login', json=data)

        assert data['email'] == 'testuser@test.com'
        assert response.status_code == 200

