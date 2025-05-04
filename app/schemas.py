from .extensions import ma
from .models import User, Company
from marshmallow import fields

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_fk = True

    password = ma.String(load_only=True)


class CompanySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Company
        include_fk = True

