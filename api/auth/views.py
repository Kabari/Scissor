# import secrets
from flask import request
from flask_restx import Resource, Namespace, fields
from ..models.user import User
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, create_refresh_token, unset_jwt_cookies
from ..utils import db
from werkzeug.security import generate_password_hash, check_password_hash
from uuid import UUID
from http import HTTPStatus


auth_ns = Namespace('auth', description='Authentication related operations')

signup_model = auth_ns.model(
    'Signup', {
        'id': fields.Integer(),
        'uuid': fields.String(max_length=36, description='User unique identifier'),
        'first_name': fields.String(required=True, max_length=50, description='User first name'),
        'last_name': fields.String(required=True, max_length=50, description='User last name'),
        'email': fields.String(required=True, max_length=50, description='User email address'),
        'password': fields.String(required=True, description='User password')
    }
)

user_model = auth_ns.model(
    'User', {
        'id': fields.Integer(),
        'uuid': fields.String(max_length=36, description='User unique identifier'),
        'first_name': fields.String(required=True, max_length=50, description='User first name'),
        'last_name': fields.String(required=True, max_length=50, description='User last name'),
        'email': fields.String(required=True, max_length=50, description='User email address'),
        'password_hash': fields.String(required=True, description='User password'),
        'is_verified': fields.Boolean(),
        'created_at': fields.DateTime(description='User creation date'),
        'updated_at': fields.DateTime(description='User data update date'),
        'urls': fields.List(fields.String(description='No of urls of the user'))
        
    }
)

login_model = auth_ns.model(
    'Login', {
        'email': fields.String(required=True, max_length=50, description='User email address'),
        'password': fields.String(required=True, description='User password')
    }
)


@auth_ns.route('/signup')
class Signup(Resource):
    @auth_ns.expect(signup_model, validate=False)
    @auth_ns.marshal_with(user_model, code=HTTPStatus.CREATED)
    @auth_ns.doc(description='Register a new account',
                responses={
                HTTPStatus.CREATED: 'Success',
                HTTPStatus.BAD_REQUEST: 'Validation Error',
                HTTPStatus.CONFLICT: 'User already exists'
            })
    def post(self):
        """
        Register a new account
        """
        print("Signup endpoint called")  # Add this line
        data = request.json

        user = User.query.filter_by(email=data['email']).first()

        if user:
            return {
                'message': 'User already exists'
            }, HTTPStatus.BAD_REQUEST
        
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password != confirm_password:
            return {
                'message': 'Passwords do not match'
            }, HTTPStatus.BAD_REQUEST


        new_user = User(
            first_name = data.get('first_name'),
            last_name = data.get('last_name'),
            email = data.get('email'),
            password_hash = generate_password_hash(password),
            # confirm_password_hash = generate_password_hash(data.get('confirm_password')),
            is_verified=False
        )

        new_user.save()

        return new_user, HTTPStatus.CREATED
    
        

@auth_ns.route('/login')
class Login(Resource):
    @auth_ns.doc(description='Login to your account',
                 responses={
                     HTTPStatus.OK: 'Success',
                     HTTPStatus.UNAUTHORIZED: 'Invalid credentials'
                     })
    @auth_ns.expect(login_model)
    def post(self):
        """
        Login to your account
        """
        print("Login endpoint called")  # Add this line
        data = request.get_json()

        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()

        # if not user:
        #     return {
        #         'message': 'User does not exist'
        #     }, HTTPStatus.UNAUTHORIZED

        if (user is not None) and check_password_hash(user.password_hash, password):
            access_token = create_access_token(identity=user.email)
            refresh_token = create_refresh_token(identity=user.email)

            response = {
                'message': 'Logged in as {}'.format(user.email),
                'access_token': access_token,
                'refresh_token': refresh_token
            }
            return response, HTTPStatus.OK
        # else:
        #     return {
        #         'message': 'Wrong credentials'
        #     }, HTTPStatus.UNAUTHORIZED
        

@auth_ns.route('/refresh')
class Refresh(Resource):
    @auth_ns.doc(security='jwt',
                    responses={
                    HTTPStatus.OK: 'Success'
                })
    # @jwt_refresh_token_required
    @jwt_required(refresh=True)
    def post(self):
        """
        Refresh the User's Access Token
        """
        current_user = get_jwt_identity()

        access_token = create_access_token(identity=current_user)

        return {
            'access_token': access_token
        }, HTTPStatus.OK
    

@auth_ns.route('/logout')
class Logout(Resource):
    @auth_ns.doc(security='jwt',
                 responses={
                HTTPStatus.OK: 'Success'
            })
    @jwt_required()
    def post(self):
        print("Endpoint called!!!")
        """
        Log the User Out
        """
        unset_jwt_cookies
        db.session.commit()
        return {"message": "Successfully Logged Out"}, HTTPStatus.OK
