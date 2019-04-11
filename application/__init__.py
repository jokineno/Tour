from flask import Flask
app = Flask(__name__)



from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///gigs.db"    
    app.config["SQLALCHEMY_ECHO"] = True

  
db = SQLAlchemy(app)



# login

from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.setup_app(app) #init_app to setup_app

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."


from functools import wraps


def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()
          
            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            
            unauthorized = False

            if role != "ANY":
                unauthorized = True
                
                user_role = current_user.role.name
                if user_role == role:
                    unauthorized = False

            if unauthorized:
                return login_manager.unauthorized()
            
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper



from application import views

from application.gigs import models
from application.gigs import views

from application.auth import models
from application.auth import views

from application.tour import models
from application.tour import views


from application.auth.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


try: 
    db.create_all()

    from application.auth.models import Role
    from application.tour.models import Tour
    from datetime import datetime
    role = Role.query.filter_by(name='USER').first()

    if not role:
        role = Role('USER')
        db.session().add(role)
        db.session().commit()

    role = Role.query.filter_by(name='ADMIN').first()

    if not role:
        role = Role('ADMIN')
        db.session().add(role)
        db.session().commit()
    
    admin = User.query.filter_by(role_id=2).first()

    #luodaan admin käynnistettäessä ohjelma ekan kerran
    if not admin:
        admin = User("ADMIN","admin","admin")
        admin.role_id = 2
        db.session().add(admin)
        db.session().commit()
    
    userX = User.query.filter_by(role_id=1).first()

    #luodaan admin käynnistettäessä ohjelma ekan kerran
    if not userX:
        userX = User("USER","user","user")
        userX.role_id = 1
        db.session().add(userX)
        db.session().commit()

    #luodaan "muut" -kiertue aluksi. 
    if Tour.query.first() == None:
        name = "Muut"
        start_date = datetime.strptime("2000-01-01","%Y-%m-%d")
        end_date = datetime.strptime("2099-01-01","%Y-%m-%d")
        tour = Tour(name,start_date,end_date)
        db.session().add(tour)
        db.session().commit()
except:
    pass