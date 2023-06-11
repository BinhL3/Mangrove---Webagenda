from vision_app import db
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime 
import sqlalchemy

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique = True, nullable=False)
    name = db.Column(db.String(120),  nullable=False)
    password_hash = db.Column(db.String(128))
    items = db.relationship('Item', backref='user',lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    task = db.Column(db.String(128), nullable=False) # task list name
    course_category = db.Column(db.String(128), nullable = False) # task course name
    course_weight = db.Column(db.String(128), nullable = False) # task course weight % (convert via python code?)
    date = db.Column(db.DateTime(timezone=True), default=datetime.now) # the date (specific formatting)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # access the user's unique id
