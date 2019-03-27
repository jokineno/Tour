from application import db

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
    

    


    def __init__(self, name, place, pvm, showtime):
        self.name = name
        self.place = place
        self.pvm = pvm
        self.showtime = showtime
        self.status = False
            