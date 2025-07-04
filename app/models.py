from . import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    site_name = db.Column(db.String(128), nullable=False)
    contact_details = db.Column(db.String(128), nullable=False)
    site_address = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    lanes = db.relationship('Lane', backref='location', lazy=True)

class Lane(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lane_name = db.Column(db.String(128), nullable=False)
    lane_type = db.Column(db.String(16), nullable=False)  # 'entry' or 'exit'
    controller_ip = db.Column(db.String(64), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    readers = db.relationship('Reader', backref='lane', lazy=True)

class Reader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reader_ip = db.Column(db.String(64), nullable=False)
    reader_type = db.Column(db.String(16), nullable=False)  # 'entry' or 'exit'
    lane_id = db.Column(db.Integer, db.ForeignKey('lane.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 