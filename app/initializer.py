from flask import Flask, request, Response
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_cors import CORS

from app.models import User, Company
from app.config import Configuration
from app.extensions import db

app = Flask(__name__)
app.config.from_object(Configuration)
db.init_app(app)
ma = Marshmallow(app)
jwt = JWTManager(app)
cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'user': User,
        'company': Company
    }

with app.app_context():
    db.create_all()
    
@app.before_request
def basic_authentication():
    if request.method.lower() == 'options':
        return Response()
