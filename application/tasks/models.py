from application import db

'''   
class Task(db.Model):
    tämä on minun työni
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(144), nullable=False)
    name = db.Column(db.String(144), nullable=False)
    place = db.Column(db.String(144), nullable=False)
    showtime = db.Column(db.String(144), nullable=False)
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    
    done = db.Column(db.Boolean, nullable=False)

    def __init__(self, date,name,place,showtime):
        self.date = date
        self.name = name
        self.place = place
        self.showtime = showtime
        self.done = False
'''

#tässä on harjoitustyön
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    place = db.Column(db.String(144), nullable=False)
    pvm = db.Column(db.DateTime(), nullable=False)
    showtime = db.Column(db.Time(), nullable=False)
    status = db.Column(db.String(144), nullable=False)
    #date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    #date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    

    
    #done = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, place, pvm, showtime):
        self.name = name
        self.place = place
        self.pvm = pvm
        self.showtime = showtime
        self.status = False
            