from application import db
from sqlalchemy.sql import text

#tässä on harjoitustyön
class Gig(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    place = db.Column(db.String(144), nullable=False)
    pvm = db.Column(db.DateTime(), nullable=False)
    showtime = db.Column(db.Time(), nullable=False)
    status = db.Column(db.String(144), nullable=False)
    #date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    #date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    tour_id = db.Column(db.Integer,db.ForeignKey('tour.id'),nullable=False)


    def __init__(self, name, place, pvm, showtime):
        self.name = name
        self.place = place
        self.pvm = pvm
        self.showtime = showtime
        self.status = False


    @staticmethod
    def upcoming_gigs(user_id):
        stmt = text("SELECT COUNT (account_id) FROM Gig WHERE account_id ="+str(user_id)+" AND status='Tulossa';")
        res = db.engine.execute(stmt)
        result = 0
        for row in res:
            result = row[0]
           
        return result
    
    @staticmethod
    def past_gigs(user_id):
        stmt = text("SELECT COUNT (account_id) FROM Gig WHERE account_id ="+str(user_id)+" AND status='Mennyt';")
        res = db.engine.execute(stmt)
        result = 0
        for row in res:
            result = row[0]
           
        return result
    
    @staticmethod
    def cancelled_gigs(user_id):
        stmt = text("SELECT COUNT (account_id) FROM Gig WHERE account_id ="+str(user_id)+" AND status='Peruttu';")
        res = db.engine.execute(stmt)
        result = 0
        for row in res:
            result = row[0]
           
        return result

    
    