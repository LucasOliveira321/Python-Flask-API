from .base import Base, db

class User(Base):
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(162), nullable=True)
    email_confirmation_token = db.Column(db.String(80))
    email_confirmed_at = db.Column(db.DateTime())
    forgotten_password_token = db.Column(db.String(80))
    terms_and_conditions = db.Column(db.Boolean, default=False)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)
    active = db.Column(db.Boolean, default=True, nullable=False)