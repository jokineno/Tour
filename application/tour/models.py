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
    def get_all_tours():
        stmt = text("SELECT name FROM tour")
        res = db.engine.execute(stmt)
        results = []
        for item in res:
            results.append(item[0])
        return results

    @staticmethod
    def get_tourName_by_id(id):
        stmt = text("SELECT name FROM tour WHERE id = " + str(id) + ";")
        res = db.engine.execute(stmt)
        result = ""
        for item in res:
            result = item[0]
        return result

    @staticmethod
    def get_gig_amount_by_id(id):
        stmt = text("SELECT COUNT (tour_id) FROM gig WHERE tour_id = " + str(id) + ";")
        res = db.engine.execute(stmt)
        result = 0
        for item in res:
            result = item[0]
        return result
       