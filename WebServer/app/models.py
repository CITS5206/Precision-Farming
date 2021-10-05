from app import db

class Map(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mapName = db.Column(db.String(100), index=True, unique=True)
    mapPath = db.Column(db.String(100))

    def __repr__(self):
        return '<Map {}, Path{}>'.format(self.mapName, self.mapPath)