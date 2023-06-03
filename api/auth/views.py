# import secrets
from flask import request
from flask_restx import Resource, Namespace, fields
from ..models.user import User
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, create_refresh_token, unset_jwt_cookies
from ..utils import db
from werkzeug.security import generate_password_hash, check_password_hash
from uuid import UUID
from http import HTTPStatus
# from flask_mail import Message, Mail
# from datetime import datetime, timedelta
# from ...api.__init__ import mail

# mail = Mail()
# token_expiration = timedelta(hours=2)

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

# def generate_verification_token():
#         token = secrets.token_urlsafe(16)
#         verification_token = token
#         return verification_token


# def send_verification_email(email, verification_url):
#     message = Message('Verify Your Email', recipients=[email])
#     message.body = f"Please click the link below to verify your email:\n{verification_url}"
#     mail.send(message)

@auth_ns.route('/signup')
class Signup(Resource):
    @auth_ns.expect(signup_model)
    @auth_ns.marshal_with(user_model, code=HTTPStatus.CREATED)
    @auth_ns.doc(description='Register a new account',
                responses={
                HTTPStatus.CREATED: 'Success',
                HTTPStatus.BAD_REQUEST: 'Validation Error',
                HTTPStatus.CONFLICT: 'User already exists'
            })
    def post(self):
        data = request.get_json()

        user = User.query.filter_by(email=data['email']).first()

        if user:
            return {
                'message': 'User already exists'
            }, HTTPStatus.BAD_REQUEST

        new_user = User(
            first_name = data.get('first_name'),
            last_name = data.get('last_name'),
            email = data.get('email'),
            password_hash = generate_password_hash(data.get('password')),
            is_verified=False
        )

        new_user.save()

        return new_user, HTTPStatus.CREATED
        # token = generate_verification_token()
        # verification_url = f"http://localhost:5000/api/auth/verify_email/token={token}"
        # send_verification_email(new_user.email, verification_url)

        # access_token = create_access_token(identity=new_user.email)
        # refresh_token = create_refresh_token(identity=new_user.email)

        # token = {
        #     'access_token': access_token,
        #     'refresh_token': refresh_token
        # }

        # response = {
        #     'uuid': new_user.uuid,
        #     'email': new_user.email,
        #     'token': token 
        # }

    
        # """send a verification email to the user's email address"""
        # msg = Message(
        #     subject='Email Verification',
        #     sender='Scissor Team',
        #     recipients=[new_user.email],
        #     body=f'Thank you for signing up on scissor \nVerify your email by clicking on the link: http://localhost:5000/api/auth/verify_email?access_token={access_token}'
        # )

        
        # mail.send(msg)

        # return {
        #     'message': 'User created successfully. Check your email for verification'
        # }, HTTPStatus.CREATED
        


    


# @auth_ns.route('/resend_verification_email')
# class ResendVerificationEmail(Resource):
#     @auth_ns.doc(description='Resend verification email')
#     @jwt_required()
#     def get(self):
#         current_user = get_jwt_identity()

#         user = User.query.filter_by(email=current_user).first()

#         if user.is_verified:
#             return {
#                 'message': 'User already verified'
#             }, HTTPStatus.BAD_REQUEST
        
#         token = generate_verification_token()
#         verification_url = f"http://localhost:5000/api/auth/verify_email/token={token}"
#         send_verification_email(user.email, verification_url)

#         return {
#             'message': 'Verification email sent successfully'
#         }, HTTPStatus.OK



# @auth_ns.route('/verify_email/token=<string:token>')
# class VerifyEmail(Resource):
#     @auth_ns.doc(description='Verify user email address')
#     @jwt_required()
#     def get(self):
#         current_user = get_jwt_identity()

#         user = User.query.filter_by(email=current_user).first()

#         if user.is_verified:
#             return {
#                 'message': 'User already verified'
#             }, HTTPStatus.BAD_REQUEST
        
#         user.is_verified = True

#         user.save()

#         return {
#             'message': 'User verified successfully'
#         }, HTTPStatus.OK
    

@auth_ns.route('/login')
class Login(Resource):

    @auth_ns.expect(login_model)
    def post(self):
        data = request.get_json()

        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()

        # if not user:
        #     return {
        #         'message': 'User does not exist'
        #     }, HTTPStatus.NOT_FOUND

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
    # @jwt_refresh_token_required
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()

        access_token = create_access_token(identity=current_user)

        return {
            'access_token': access_token
        }, HTTPStatus.OK
    

@auth_ns.route('/logout')
class Logout(Resource):
    @jwt_required()
    def post(self):
        """
        Log the User Out
        """
        unset_jwt_cookies
        db.session.commit()
        return {"message": "Successfully Logged Out"}, HTTPStatus.OK
