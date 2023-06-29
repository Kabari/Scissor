from ..utils import db
from datetime import datetime
import random, string
from uuid import uuid4
from .user import User

class Url(db.Model):
    # __tablename__ = 'urls'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(16), nullable=False, unique=True)
    long_url = db.Column(db.String(2048), nullable=False)
    short_code = db.Column(db.String(6), nullable=False, unique=True)
    short_url = db.Column(db.String(50), nullable=False, unique=True)
    custom_domain = db.Column(db.String(255), unique=True, nullable=True)
    custom_url = db.Column(db.String(50), unique=True, nullable=True)
    user_id = db.Column(db.String, db.ForeignKey('user.email'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    qr_code = db.Column(db.String, nullable=True)
    clicks = db.relationship('Click', backref='url', lazy=True)

    # users = db.Column(db.Integer())

    # url_id = db.relationship('User', backref='url', lazy=True)

    def __repr__(self):
        return f"<Url {self.id}>"

    def save(self):
        if not self.uuid:
            self.uuid = str(uuid4())
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_total_urls(cls, email):
        return Url.query.filter_by(user_id=email).count()

    @classmethod
    def get_total_clicks(cls, email):
        urls = Url.query.filter_by(user_id=email).all()
        total_clicks = sum(len(url.clicks) for url in urls)
        return total_clicks

    # @classmethod
    # def get_by_id(cls, id):
    #     return cls.query.get_or_404(id)
    
    # @classmethod
    # def get_url_total_clicks(cls, id):
    #     url = Url.query.filter_by(user_id=id).first()
    #     total_clicks = url.clicks
    #     return total_clicks
    
    # @classmethod
    # def get_total_clicks(cls, id):
    #     urls = Url.query.filter_by(user_id=id).all()
    #     total_clicks = sum([url.clicks for url in urls])
    #     return total_clicks
    
    # @classmethod
    # def get_total_urls(cls, id):
    #     counter = Url.query.filter_by(user_id=id).count()
    #     return counter
    
    @classmethod
    def check_url(cls, url):
        is_exist = Url.query.filter_by(short_url=url).first()
        if is_exist:
            return True
        else:
            return False
        

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(6))
    # existing_short_code = Shortenedcode.query.filter_by(short_code=short_code).first()
    # if existing_short_code:
    #     return generate_short_code()
    return short_code





# from ..utils import db
# from datetime import datetime
# import random, string
# from uuid import uuid4

# class ShortenedUrl(db.Model):
#     __tablename__ = 'shortened_urls'

#     id = db.Column(db.Integer, primary_key=True)
#     uuid = db.Column(db.String(16), nullable=False, unique=True)
#     original_url = db.Column(db.String(2048), nullable=False)
#     shortened_url = db.Column(db.String(10), nullable=False, unique=True)
#     custom_url = db.Column(db.String(255), unique=True)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)

#     clicks = db.relationship('Click', backref='shortened_urls', lazy=True)

#     def __repr__(self):
#         return f'<ShortenedUrl {self.shortened_url}'

#     # users_uuid = db.Column(db.String(), db.ForeignKey('users.uuid'), nullable=False)
#     # users_uuid = db.Column(db.String(36), db.ForeignKey('users.uuid'))

#     # def __init__(self, shortened_url, original_url, created_at):
#     #     self.shortened_url = shortened_url
#     #     self.original_url = original_url


# #     click_count = db.Column(db.Integer, nullable=False, default=0),
# #     long_url = db.Column(db.String(100), nullable=False, unique=True),
# #     short_url = db.Column(db.String(100), nullable=False, unique=True),
# #     created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
# #     updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# #     # def __init__(self, username, password):
# #     #     # self.id = str(uuid4())
# #     #     # self.uuid = str(uuid4())
# #     #     self.username = username
# #     #     self.password = password

# #     def __repr__(self):
# #         pass


#     def save(self):
#         self.uuid = str(uuid4())
#         # self.user_uuid = str(uuid4())
#         db.session.add(self)
#         db.session.commit()

# #     def delete(self):
# #         db.session.delete(self)
# #         db.session.commit()

# def generate_short_url(length=6):
#     characters = string.ascii_letters + string.digits
#     short_url = ''.join(random.choice(characters) for _ in range(6))
#     # existing_short_code = ShortenedURL.query.filter_by(short_code=short_code).first()
#     # if existing_short_code:
#     #     return generate_short_code()
#     return short_url
#     # return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

# # def redirect_to

# # def generate_uuid():
# #     return str(uuid4())

# # def get_shortened_url_by_shortened_url(shortened_url):
# #     return ShortenedUrl.query.filter_by(shortened_url=shortened_url).first()

# # def get_shortened_url_by_uuid(uuid):

# #     return ShortenedUrl.query.filter_by(uuid=uuid).first()

# # def get_shortened_url_by_custom_url(custom_url):
# #     return ShortenedUrl.query.filter_by(custom_url=custom_url).first()

# # def get_shortened_url_by_original_url(original_url):
# #     return ShortenedUrl.query.filter_by(original_url=original_url).first()

# # def get_shortened_url_by_user_id(user_id):
# #     return ShortenedUrl.query.filter_by(user_id=user_id).all()

# # def get_all_shortened_urls():
