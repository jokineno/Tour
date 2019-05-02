from application import db
from application.tour import models
from application.models import Base


tours = db.Table('tours_users', 
        db.Column('account_id', db.Integer,db.ForeignKey('account.id')),
        db.Column('tour_id',db.Integer,db.ForeignKey('tour.id'))
)


#allgigs = db.Table('gigs_users',
#        db.Columns('account_id',db.Integer,db.ForeignKey('account.id')),
#        db.Column('gig_id',db.Integer,db.ForeignKey('gig.id'))
#)
class User(Base):

    __tablename__ = "account"
    
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)    
    gigs = db.relationship("Gig",backref='account',lazy=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=True)
    role = db.relationship("Role")
    tours = db.relationship('Tour',secondary=tours, backref=db.backref('tours',lazy=True))
    #gigs = db.relationship("Gig",secondary=gigs backref=db.backref('gigs'),lazy=True)
    

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
       
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
    
   


class Role(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(5), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name