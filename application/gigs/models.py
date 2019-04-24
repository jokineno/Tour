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

    
    @staticmethod    
    def find_gigs(query):
        #Note.query.filter(Note.message.like("%somestr%")).all()
        #KOKEILE TÄTÄ
    
        stmt = text("SELECT * FROM Tour"
                    " LEFT JOIN gig ON Tour.id = tour_id"
                    " WHERE (Tour.name || Gig.place || Gig.name) LIKE '%{0}%';".format(query))
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append(row)

        return response

   
    @staticmethod
    def gigs_by_tour_id(tourid):
        stmt = text("SELECT * FROM Gig WHERE tour_id = " + str(tourid) + ";")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append(row)

        return response
