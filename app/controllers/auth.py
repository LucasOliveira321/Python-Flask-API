from flask import Blueprint, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

from app.initializer import app
from app.helpers.create_user_token import create_user_token
from app.extensions import db
from app.models import User
from app.schemas import UserSchema

auth = Blueprint(
    'auth', 
    __name__, 
    url_prefix=app.config['API_URL_PREFIX'] + "/auth"
)

@auth.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if User.query.filter_by(username=data['username']).first():
        return {'msg':"User already exists"}

    hashed = generate_password_hash(data['password'])
    user = User(username=data['username'], password=hashed)
    db.session.add(user)
    db.session.commit()
    return UserSchema().dump(user)

@auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()

    if not user or not check_password_hash(user.password, data['password']):
        return {'msg':"Invalid credentials"}
    
    access_token = create_user_token(user)
    return {
        'access_token':access_token,
        'first_name': user.first_name,
        'last_name': user.last_name
    }

# @auth.route("/teste", methods=["GET"])
# @jwt_required()
# def test():
#     claims = get_jwt()
#     print(claims['email'])
#     print(claims['perms_1_allowed'])
#     print(claims['perms_2_allowed'])
#     print(claims['perms_3_allowed'])
#     return {
#         'email': 'EMAIL'
#     }

