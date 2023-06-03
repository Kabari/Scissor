from ..utils import db
from datetime import datetime

class Click(db.Model):
    # __tablename__ = 'clicks'

    id = db.Column(db.Integer, primary_key=True)
    url_id = db.Column(db.Integer, db.ForeignKey('url.id'), nullable=False)
    # short_url_id = db.Column(db.Integer, db.ForeignKey('shortened_urls.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    ip_address = db.Column(db.String(50))
    user_agent = db.Column(db.String(255))
    referrer = db.Column(db.String(2048))

    # urls = db.relationship('ShortenedUrl', backref='clicks')
    # user = db.relationship('User', backref='clicks')

    # def __repr__(self):
    #     return f"<Click {self.referrer} {self.ip_address}>"

    # def __init__(self, urls, user, timestamp):
    #     self.urls = urls
    #     self.user = user
    #     self.timestamp = timestamp
    
    def save(self):
        db.session.add(self)
        db.session.commit()