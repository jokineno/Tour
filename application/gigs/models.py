from application import db
from sqlalchemy.sql import text


class Gig(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    place = db.Column(db.String(144), nullable=False)
    pvm = db.Column(db.DateTime(), nullable=False)
    showtime = db.Column(db.Time(), nullable=False)
    status = db.Column(db.String(144), nullable=False)
 
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
    def gigs_by_tour_id(tourid=0):
        stmt = text("SELECT * FROM Gig WHERE tour_id = :tourid ;").params(tourid=tourid)
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append(row)

        return response

    @staticmethod
    def upcoming(account_id=0):
        stmt = text("SELECT COUNT (gig.id) FROM Gig WHERE tour_id IN (SELECT tour_id FROM tours_users WHERE account_id = :account_id) and gig.status='Upcoming';").params(account_id=account_id)
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append(row[0])

        return response[0]

    @staticmethod
    def past(account_id=0):
        stmt = text("SELECT COUNT (gig.id) FROM Gig WHERE tour_id IN (SELECT tour_id FROM tours_users WHERE account_id = :account_id) and gig.status='Past';").params(account_id=account_id)
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append(row[0])

        return response[0]

    @staticmethod
    def cancelled(account_id=0):
        stmt = text("SELECT COUNT (gig.id) FROM Gig WHERE tour_id IN (SELECT tour_id FROM tours_users WHERE account_id = :account_id) and gig.status='Cancelled';").params(account_id=account_id)
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append(row[0])

        return response[0]    


#SELECT gig.pvm, gig.name, gig.place, gig.showtime, gig.status, tour.name FROM Gig INNER JOIN Tour on Gig.tour_id = Tour.id GROUP BY gig.name;
#ADMININLLE KAIKKI KEIKAT

    @staticmethod
    def allgigsforuser(account_id=0):
        stmt = text("SELECT gig.pvm, gig.name, gig.place, gig.showtime, gig.status, tour.name FROM GIG INNER JOIN TOUR on Gig.tour_id = Tour.id WHERE tour_id IN (SELECT tour_id FROM tours_users WHERE account_id = :account_id)").params(account_id=account_id)
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append(row[0])

        return response[0]    