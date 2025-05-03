from flask import Blueprint, request, abort
from flask_jwt_extended import jwt_required

from app.initializer import app
from app.extensions import db
from app.models import Company
from app.schemas import CompanySchema

companies = Blueprint(
    'companies', 
    __name__, 
    url_prefix=app.config['API_URL_PREFIX'] + "/companies"
)


@companies.route('/', methods=['GET', 'POST'])
# @jwt_required()
def root():
    if request.method == 'GET':
        return CompanySchema(many=True).dump(Company.query.all())
    if request.method == 'POST':
        try:
            new_company = Company()
            data = request.json
            for field in data:
                setattr(new_company, field, data[field])
            db.session.add(new_company)
            db.session.commit()
            return CompanySchema().dump(new_company)
        except Exception as e:
            db.session.rollback()
            abort(500, description=f'Error: {e}')


