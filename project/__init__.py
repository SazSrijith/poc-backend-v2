from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate


app = Flask(__name__)
db = SQLAlchemy(app)

app.config['JWT_SECRET_KEY'] = 'secret'
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

Migrate(app,db)
CORS(app)

from project.authentication.routes import auth
from project.assignproject.routes import assign
from project.register.others.routes import othersreg
from project.landingpage.routes import home
from project.reports.winnercircle.routes import wcreport
from project.reports.trendnext.routes import tnreport
from project.reports.topgearchallenge.routes import tgcreport
from project.register.hackerrank.routes import hrregister
from project.register.winnercircle.routes import wcregister
from project.register.trendnext.routes import tnregister
from project.register.topgearchallenge.routes import tgcregister
from project.register.topgearlearning.routes import tglregister
from project.register.pragati.routes import prregister
from project.register.shristi.routes import shregister
from project.reports.others.routes import othersrep

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(assign, url_prefix='/assign')
app.register_blueprint(othersreg, url_prefix='/list')
app.register_blueprint(home, url_prefix='/home')
app.register_blueprint(wcreport, url_prefix='/report')
app.register_blueprint(tnreport, url_prefix='/report')
app.register_blueprint(tgcreport, url_prefix='/report')
app.register_blueprint(hrregister, url_prefix='/register')
app.register_blueprint(wcregister, url_prefix='/register')
app.register_blueprint(tnregister, url_prefix='/register')
app.register_blueprint(tgcregister, url_prefix='/register')
app.register_blueprint(tglregister, url_prefix='/register')
app.register_blueprint(prregister, url_prefix='/register')
app.register_blueprint(shregister, url_prefix='/register')
app.register_blueprint(othersrep, url_prefix='/report')