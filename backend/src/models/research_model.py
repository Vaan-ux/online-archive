from src.extensions import db
from datetime import datetime


class Research(db.Model):
    __tablename__ = 'research'

    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(150), nullable=False)
    authors     = db.Column(db.String(255), nullable=False)
    year        = db.Column(db.Integer,     nullable=False)
    category    = db.Column(db.String(100), nullable=True)
    pdf_path    = db.Column(db.String(255), nullable=False)
    status      = db.Column(db.String(50),  default='pending')
    is_featured = db.Column(db.Boolean,     default=False)
    user_id     = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at  = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at  = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id':          self.id,
            'title':       self.title,
            'authors':     self.authors,
            'year':        self.year,
            'category':    self.category,
            'pdf_path':    self.pdf_path,
            'status':      self.status,
            'is_featured': self.is_featured,
            'user_id':     self.user_id,
            'created_at':  self.created_at.isoformat(),
            'updated_at':  self.updated_at.isoformat()
        }
