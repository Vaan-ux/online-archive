from src.extensions import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'

    id         = db.Column(db.Integer, primary_key=True)
    username   = db.Column(db.String(50),  unique=True, nullable=False)
    email      = db.Column(db.String(120), unique=True, nullable=False)
    phone      = db.Column(db.String(20),  unique=True, nullable=False)
    password   = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    research = db.relationship('Research', backref='uploader', lazy=True)

    def to_dict(self):
        return {
            'id':         self.id,
            'username':   self.username,
            'email':      self.email,
            'phone':      self.phone,
            'created_at': self.created_at.isoformat()
        }
