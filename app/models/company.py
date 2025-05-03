from .base import Base, db

class Company(Base):
    __tablename__ = 'companies'
    business_name = db.Column(db.String(80))
    legal_name = db.Column(db.String(80), nullable=False)
    tax_id = db.Column(db.String(80), unique=True, nullable=False)
    website_url = db.Column(db.String(80), unique=True)
    address_line_1 = db.Column(db.String(160), nullable=False)
    phone = db.Column(db.String(80), nullable=False)
    users = db.relationship('User', backref='company', lazy=True)