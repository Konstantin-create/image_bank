from app import db
from datetime import datetime


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String, unique=True, nullable=False)
    from_ip = db.Column(db.String, nullable=False)
    time_stamp = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return f'<Image: {self.image_path} | {self.from_ip}>'
