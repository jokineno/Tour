from application import db

    
class Task(db.Model):
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
    
            