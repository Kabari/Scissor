import uuid
from flask import render_template, request, redirect, send_file, make_response
from flask_restx import Resource, Namespace, fields, abort
from ..models.url import Url, generate_short_url
from ..models.user import User
from ..models.click import Click
from ..utils import db
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity
from validators import url as validate_url
from uuid import uuid4
import qrcode
import io
from PIL import Image
import requests
# from ...api import cache
from flask_caching import Cache

# cache = Cache(app, config={'CACHE_TYPE': 'simple'})


url_ns = Namespace('url', description='Shorten related operations')

url_model = url_ns.model(
    'Url', {
        # 'id': fields.Integer(),
        # 'uuid': fields.String(max_length=16, description='Shortened URL unique identifier'),
        'long_url': fields.String(required=True, max_length=1000, description='URL to be shortened'),
        'short_url': fields.String(required=True, max_length=6, description='Shortened URL'),
        # 'custom_domain': fields.String(required=False, max_length=255, description='Custom URL'),
        # 'user_id': fields.String(description='User ID'),
        'created_at': fields.DateTime(description='Shortened URL creation date'),
        # 'qr_code': fields.String(description='QR code of the short url'),
        # 'clicks': fields.List(fields.String(description='No of clicks for the url'))
    }
)

shorten_url_model = url_ns.model(
    'ShortenUrl', {
        # 'user_uuid': fields.String(description='User UUID'),
        # 'uuid': fields.String(max_length=36, description='Shortened URL unique identifier'),
        # 'user_id': fields.Integer(description='User ID'),
        'long_url': fields.String(required=True, max_length=1000, description='URL to be shortened')
    }
)

custom_domain_model = url_ns.model(
    'CustomUrl', {
        'custom_domain': fields.String(required=False, max_length=255, description='Custom URL')
    }
)

shortened_url_model = url_ns.model(
    'ShortenedUrl', {
        'long_url': fields.String(required=True, max_length=1000, description='URL to be shortened'),
        'short_url': fields.String(required=True, max_length=6, description='Shortened URL'),
        'created_at': fields.DateTime(description='Shortened URL creation date'),
        # 'user_uuid': fields.String(description='User UUID'),
        # 'uuid': fields.String(max_length=36, description='Shortened URL unique identifier'),
        # 'user_id': fields.String(description='User ID'),
        # 'long_url': fields.String(required=True, max_length=1000, description='URL to be shortened')
    }
)


@url_ns.route('/create')
class CreateUrl(Resource):
    @url_ns.expect(shorten_url_model)
    @url_ns.marshal_with(shortened_url_model)
    @jwt_required()
    def post(self):
        print('Enpoint called!!!!!')
        email = get_jwt_identity()

        data = request.get_json()
        long_url = data.get('long_url')
        # custom_domain = data.get('custom_domain')

        if not validate_url(long_url):
            abort(HTTPStatus.BAD_REQUEST, message='Invalid URL')

        if long_url:
            short_url = generate_short_url()

            while Url.query.filter_by(short_url=short_url).first() is not None:
                short_url = generate_short_url()

            url = Url(
                long_url=long_url,
                short_url=short_url,
                # custom_domain=custom_domain,
                user_id=email
            )
            url.save()
            return url, HTTPStatus.CREATED
        # return render_template('create_short_url.html'), HTTPStatus.OK


@url_ns.route('/<short_url>')
class RedirectUrl(Resource):
    # @url_ns.marshal_with(shorten_url_model)
    def get(self, short_url):
        url = Url.query.filter_by(short_url=short_url).first()
        if url:
            click = Click(
                url_id=url.id, 
                ip_address=request.remote_addr, 
                user_agent=request.user_agent.string, 
                referrer=request.referrer
            )
            click.save()
            
            return redirect(url.long_url)
        else:
            abort(HTTPStatus.NOT_FOUND, message='Invalid short URL')
            
        #     # response = {redirect(url.long_url)}
        #     return redirect(url.long_url), HTTPStatus.OK
        # else:
        #     # response = {
        #     #     'message': 'Invalid short url'
        #     # }
        #     return {
        #         'message': 'Invalid short url'
        #     }, HTTPStatus.NOT_FOUND



# @url_ns.route('/<short_url>/custom')
# class CustomUrl(Resource):
#     @url_ns.expect(custom_domain_model)
#     @url_ns.marshal_with(custom_domain_model)
#     @jwt_required()
#     def patch(self, url_id):
#         id = get_jwt_identity()

#         url_to_update = Url.query.get_by_id(url_id)
#         if url_to_update is None:
#             abort(HTTPStatus.NOT_FOUND, message='Url not found')

#         data = request.get_json()
#         url_to_update.custom_domain = data.get('custom_domain')
#         updated = url_to_update.custom_domain

#         db.session.commit()

#         return updated, HTTPStatus.CREATED    


@url_ns.route('/<int:url_id>/custom')  # Assuming `url_id` is an integer
class CustomUrl(Resource):
    @url_ns.expect(custom_domain_model)
    @url_ns.marshal_with(custom_domain_model)
    @jwt_required()
    def patch(self, url_id):
        current_user_id = get_jwt_identity()  # Renamed `id` to `current_user_id` to avoid shadowing

        url_to_update = Url.query.get(url_id)  # Fixed method name to `get` instead of `get_by_id`
        if url_to_update is None:
            abort(HTTPStatus.NOT_FOUND, message='Url not found')

        data = request.get_json()
        url_to_update.custom_domain = data.get('custom_domain')
        updated_custom_domain = url_to_update.custom_domain

        db.session.commit()

        return updated_custom_domain, HTTPStatus.CREATED


@url_ns.route('/urls')
class AllUrls(Resource):
    @url_ns.marshal_list_with(url_model)
    @jwt_required()
    def get(self):
        print("Endpoint initiated!!!!!")
        email = get_jwt_identity()
        user = User.query.filter_by(email=email).first()
        if user is None:
            abort(HTTPStatus.NOT_FOUND, message='User not found')
        # urls = Url.query.filter_by(user_id=id).all()
        urls = user.urls
        return urls, HTTPStatus.OK
        # else:
        #     response = {
        #         'message': 'Invalid user'
        #     }
        #     return response, HTTPStatus.NOT_FOUND


# @url_ns.route('/<short_url>/stats')
# class UrlStats(Resource):
#     def get(self, short_url):
#         url = Url.query.filter_by(short_url=short_url).first()
#         if url:
#             response = {
#                 'clicks': url.clicks
#             }
#             return response, HTTPStatus.OK
#         else:
#             response = {
#                 'message': 'Invalid short url'
#             }
#             return response, HTTPStatus.NOT_FOUND




@url_ns.route('/analytics/<short_url>')
class UrlAnalytics(Resource):
    # print("Endpoint started")
    def get(self, short_url):
        print("Endpoint initiated!!!!!")
        url = Url.query.filter_by(short_url=short_url).first()
        if url:
            clicks = Click.query.filter_by(url_id=url.id).all()
            click_data = []
            for click in clicks:
                click_data.append({
                    'id': click.id,
                    'timestamp': str(click.timestamp),
                    'ip_address': click.ip_address,
                    'referrer': click.referrer,
                    'user_agent': click.user_agent
                })
            response = {
                'short_url': short_url,
                'clicks': click_data
            }
            return response, HTTPStatus.OK
        else:
            response = {
                'message': 'Invalid short URL'
            }
            return response, HTTPStatus.NOT_FOUND



        

@url_ns.route('/<short_url>/qr-code')
class QrCode(Resource):
    def get(self, short_url):
        url = Url.query.filter_by(short_url=short_url).first()
        if url:
            qr_code_image = generate_qr_code(url.short_url)

            qr_code_file = io.BytesIO()
            qr_code_image.save(qr_code_file, format='PNG')
            qr_code_file.seek(0)

            # return send_file(
            #     qr_code_file,
            #     mimetype='image/png',
            #     as_attachment=True,
            #     attachment_filename='qrcode.png'
            # ), HTTPStatus.OK

            # return response, HTTPStatus.CREATED
            download = request.args.get('download', '').lower() == 'true'

            if download:
                response = make_response(qr_code_file.getvalue())
                response.headers.set('Content-Type', 'image/png')
                response.headers.set('Content-Disposition', 'attachment', filename='qrcode.png')
            else:
                response = make_response(send_file(qr_code_file, mimetype='image/png'))

            response.headers.set('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
            response.headers.set('Pragma', 'no-cache')
            response.headers.set('Expires', '0')

            return response
        
        else:
            response = {
                'message': 'Invalid short url'
            }
            return response, HTTPStatus.NOT_FOUND
        
        


        #     qr_code_image_url = generate_qr_code(url.short_url)

        #     return {
        #         "qr_code_image_url": qr_code_image_url
        #     }, HTTPStatus.OK
        # else:
        #     return {
        #         "message": "Invalid short URL"
        #     }, HTTPStatus.NOT_FOUND




def generate_qr_code(short_url):
    qr = qrcode.QRCode(
        version=4,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=3
    )
    qr.add_data(short_url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img = img.resize((400, 400), Image.ANTIALIAS)
    return img


    # qr_code_data = {
    #     "data": short_url,
    #     "size": 400,
    #     "color": "000000",
    #     "bgcolor": "FFFFFF",
    #     "format": "png",
    #     "qzone": 0,
    #     "eyes": "square",
    #     "dots": "square",
    #     "mask": 0,
    #     "logo": "",
    #     "logosize": 30
    # }

    # response = requests.post("https://www.qrcode-monkey.com/api/qr/custom", json=qr_code_data)
    # if response.status_code == 200:
    #     qr_code_image_url = response.json().get("imageUrl")
    #     return qr_code_image_url
    # else:
    #     # Handle the error case
    #     raise Exception("Failed to generate QR code")
