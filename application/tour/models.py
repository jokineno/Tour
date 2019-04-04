from application import db
from sqlalchemy.sql import text

#tässä on harjoitustyön
class Tour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    start_date = db.Column(db.DateTime(), nullable=False)
    end_date = db.Column(db.DateTime(), nullable=False)
    #date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    #date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),

   # account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
    #                       nullable=False)
    # Vieraana avaimena keikat, jotka liittyvät tähän kiertueeseen. Samoin jäsenet, jotka liittyvät tähän kiertueeseen
    
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
