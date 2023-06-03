from flask import request, redirect
from flask_restx import Resource, Namespace, fields, abort
from ..models.click import Click
from ..utils import db
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity


click_ns = Namespace('click', description='Click related operations')

click_model = click_ns.model(
    'Click', {
        'id': fields.Integer(),
        'url_id': fields.Integer(description='Url ID'),
        'timestamp': fields.DateTime(description='Time Url is clicked'),
        'ip_address': fields.String(description='IP Address of where the url was clicked'),
        'user_agent': fields.String(description='User Agent'),
        'referer': fields.String(description='Referer')
    }
)

"""
Generate all related endpoints
"""
# @app.route('/qrcode/<shortened_url>')
# def generate_qrcode(shortened_url):
#     # Generate the QR code
#     qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
#     qr.add_data(shortened_url)
#     qr.make(fit=True)

#     # Create an in-memory buffer to store the QR code image
#     buffer = BytesIO()
#     img = qr.make_image(fill_color="black", back_color="white")
#     img.save(buffer, format="PNG")
#     buffer.seek(0)

#     # Create a Flask response with the QR code image
#     response = make_response(buffer.getvalue())
#     response.headers['Content-Type'] = 'image/png'

#     return response


