

from flask import Flask, render_template, url_for, redirect, request, abort
from api import create_app
from http import HTTPStatus
import requests
# app = Flask(__name__, static_folder='static', template_folder='templates')
app = create_app()

# Serve the webpages
@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    return render_template('login.html')


@app.route('/dashboard', methods=['GET'])
def dashboard_page():
    return render_template('dashboard.html')


@app.route('/create', methods=['GET', 'POST'])
def create_page():
    return render_template('shorten.html')


@app.route('/link-man')
def manage_page():
    return render_template('link-man.html')

@app.route('/analytics/<short_url>')
def analytics_page(short_url):
    return render_template('analytics.html', short_url=short_url)


@app.route('/qr-code/<short_url>')
def qr_code_page(short_url):
    return render_template('qr-code.html', short_url=short_url)


@app.route('/custom_url/<short_url>')
def custom_url_page(short_url):
    return render_template('custom_url.html', short_url=short_url)

if __name__ == '__main__':
    app.run(debug=True)