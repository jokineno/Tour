from application import db
from sqlalchemy.sql import text
from application.auth import models



class Tour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    start_date = db.Column(db.DateTime(), nullable=False)
    end_date = db.Column(db.DateTime(), nullable=False)
    gigs = db.relationship("Gig", backref='tour', lazy=True)
    

    

    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date

    @staticmethod
    def get_tourName_by_id(id=0):
        stmt = text("SELECT name FROM tour WHERE id = :id;").params(id=id)
        res = db.engine.execute(stmt)
        result = ""
        for item in res:
            result = item[0]
        return result

    @staticmethod
    def get_gig_amount_by_id(id=0):
        stmt = text("SELECT COUNT (tour_id) FROM gig WHERE tour_id = :id;").params(id=id)
        res = db.engine.execute(stmt)
        result = 0
        for item in res:
            result = item[0]
        return result

    
    @staticmethod
    def get_index(id=0):
        stmt = text("SELECT tour_id FROM tours_users"
                    " WHERE account_id= :id;").params(id=id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append(row[0])

        return response
    
    @staticmethod
    def get_gig_amounts_by_tour():
        stmt = text("SELECT tour.name, count(*) FROM Gig INNER JOIN tour ON Tour.id=gig.tour_id  GROUP BY tour.name;")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append(row)
        
        return response