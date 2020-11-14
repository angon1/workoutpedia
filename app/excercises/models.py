from app import db
from sqlalchemy_serializer import SerializerMixin

class Excercise(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(512), unique=True)
    movieLink = db.Column(db.String(512))

    def __repr__(self):
        return '<\nExcercise name: {}\n Description: {}\n Link: {}\n>'.format(self.name, self.description, self.movieLink)
