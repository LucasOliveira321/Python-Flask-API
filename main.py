from app.controllers import auth, company
from app.initializer import app

app.register_blueprint(auth.auth)
app.register_blueprint(company.companies)
