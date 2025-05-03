from flask import Blueprint, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

from app.initializer import app
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
    user = User.query.filter_by(username=data['username']).first()

    if not user or not check_password_hash(user.password, data['password']):
        return {'msg':"Invalid credentials"}

    token = create_access_token(identity=user.id)
    return {'access_token':token}
