

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


@app.route('/link-man', methods=['GET', 'POST'])
def manage_page():
    return render_template('link-man.html')

@app.route('/analytics/', methods=['GET', 'POST'])
def analytics_page():
    return render_template('analytics.html')

if __name__ == '__main__':
    app.run(debug=True)