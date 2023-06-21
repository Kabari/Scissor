from flask import Flask, render_template, redirect
from flask_restx import Api, Resource
from .config.config import config_dict
from .utils import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_mail import Mail
from .auth.views import auth_ns
from .shorten.views import url_ns
# from .controllers.controllers import api as ns
from .models.user import User
from .models.url import Url
from .models.click import Click
from flask_caching import Cache


def create_app(config=config_dict['dev']):
    app = Flask(__name__, static_folder='static', template_folder='templates')

    app.config.from_object(config)

    db.init_app(app)

    cache = Cache(app)
    # Cache.init_app(app)

    CORS(app)

    jwt = JWTManager(app)

    migrate = Migrate(app, db)

    mail = Mail(app)

    
    @app.route('/')
    def index():
        return render_template('index.html')
    



    authorizations = {
        'Bearer Auth': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization',
            'description': 'Add a JWT token to the header with ** Bearer &lt; JWT &gt; token to authorize **'
        }
    }

    api = Api(app, 
        version='1.0', 
        title='Scissor API', 
        description='A url shortener Service',
        authorizations=authorizations,
        security='Bearer Auth'
    )
    
    api.add_namespace(auth_ns, path='/auth')
    api.add_namespace(url_ns, path='/url')


    @app.shell_context_processor
    def make_shell_context():
        return {
            'db': db, 
            'User': User,
            'Url': Url,
            'Click': Click
        }

    return app
    















































# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_cors import CORS
# from flask_jwt_extended import JWTManager
# from flask_mail import Mail
# from flask_bcrypt import Bcrypt
# from flask_marshmallow import Marshmallow
# from flask_socketio import SocketIO
# from flask_redis import FlaskRedis

# from config import Config

# db = SQLAlchemy()
# migrate = Migrate()
# cors = CORS()
# jwt = JWTManager()

# mail = Mail()
# bcrypt = Bcrypt()
# ma = Marshmallow()
# socketio = SocketIO()
# redis = FlaskRedis()


# def create_app(config_class=Config):
#     app = Flask(__name__)
#     app.config.from_object(config_class)

#     db.init_app(app)
#     migrate.init_app(app, db, render_as_batch=True)
#     cors.init_app(app)
#     jwt.init_app(app)
#     mail.init_app(app)
#     bcrypt.init_app(app)
#     ma.init_app(app)
#     socketio.init_app(app)
#     redis.init_app(app)

#     from api.errors import bp as errors_bp
#     app.register_blueprint(errors_bp)

#     from api.auth import bp as auth_bp
#     app.register_blueprint(auth_bp, url_prefix='/auth')

#     from api.users import bp as users_bp
#     app.register_blueprint(users_bp, url_prefix='/users')

#     from api.posts import bp as posts_bp
#     app.register_blueprint(posts_bp, url_prefix='/posts')

#     from api.comments import bp as comments_bp
#     app.register_blueprint(comments_bp, url_prefix='/comments')

#     from api.chat import bp as chat_bp
#     app.register_blueprint(chat_bp, url_prefix='/chat')

#     from api.notifications import bp as notifications_bp
#     app.register_blueprint(notifications_bp, url_prefix='/notifications')

#     from api.messages import bp as messages_bp
#     app.register_blueprint(messages_bp, url_prefix='/messages')

#     from api.search import bp as search_bp
#     app.register_blueprint(search_bp, url_prefix='/search')

#     from api.admin import bp as admin_bp
#     app.register_blueprint(admin_bp, url_prefix='/admin')

#     return app