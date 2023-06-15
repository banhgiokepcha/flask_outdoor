from .. import db


activity = db.Table('place_activity', 
    db.Column('places_id', db.Integer, db.ForeignKey('places.id')), 
    db.Column('activity_id', db.Integer, db.ForeignKey('activity.id'))) 
              
activity_marker = db.Table('marker_activity',
    db.Column('markers_id', db.Integer, db.ForeignKey('markers.id')),
    db.Column('activity_id', db.Integer, db.ForeignKey('activity.id')))

class Places(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))
    latitude = db.Column(db.String(350))
    longitude = db.Column(db.String(255))
    region = db.Column(db.String(255))
    text = db.Column(db.String(255))
    activity = db.relationship(
        'Activity',
        secondary=activity,
        backref=db.backref('places', lazy='dynamic')
    )
    
    def __init__(self, title="", text="",latitude="", longitude=""):
        self.title = title
        self.text = text
        self.latitude=latitude
        self.longitude=longitude

    def __repr__(self):
        return "<Post '{}'>".format(self.title)

class Markers(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.String())
    latitude = db.Column(db.String(255))
    longitude = db.Column(db.String(255)) 
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    activity_marker = db.relationship(
        'Activity', 
        secondary=activity_marker, 
        backref=db.backref('markers', lazy='dynamic'))

    def __init__(self, title="", text="", latitude="", longitude=""):
        self.title = title
        self.text = text 
        self.latitude = latitude
        self.longitude = longitude


    def __repr__(self):
        return "<Post '{}'>".format(self.title)

class Activity(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))

    def __init__(self, title=""):
        self.title = title

    def __repr__(self):
        return "<Activity '{}'>".format(self.title)