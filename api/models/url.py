# from ..utils import db
# from datetime import datetime

# class Url(db.Model):
#     __tablename__ = 'url'

#     id = db.Column(db.String(36), primary_key=True)
#     uuid = db.Column(db.String(36), nullable=False, unique=True),
#     click_count = db.Column(db.Integer, nullable=False, default=0),
#     long_url = db.Column(db.String(100), nullable=False, unique=True),
#     short_url = db.Column(db.String(100), nullable=False, unique=True),
#     created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

#     # def __init__(self, username, password):
#     #     # self.id = str(uuid4())
#     #     # self.uuid = str(uuid4())
#     #     self.username = username
#     #     self.password = password

#     def __repr__(self):
#         pass


#     def save(self):
#         self.uuid = str(uuid4())
#         db.session.add(self)
#         db.session.commit()

#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()