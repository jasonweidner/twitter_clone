import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate
from flask_login import LoginManager, login_required, login_user, logout_user
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_mail import Mail


naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}


app = Flask(__name__)

app.config['SECRET_KEY'] = 'blahblahblah'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        "DATABASE_URL", f"sqlite:///app.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'testforgritter@gmail.com'
app.config['MAIL_PASSWORD'] = 'gritteriscool'

#os.environ.get('GMAIL_USERNAME') or 'MAIL_USERNAME'
#os.environ.get('GMAIL_PASSWORD') or 'MAIL_PASSWORD'


mail = Mail(app)
#mail.init_app(app)
db = SQLAlchemy(app=app, metadata=MetaData(naming_convention=naming_convention))
db.init_app(app)
migrate = Migrate(app, db, render_as_batch=True)
bootstrap = Bootstrap(app)
login = LoginManager(app)
bcrypt = Bcrypt(app)


from project import routes
