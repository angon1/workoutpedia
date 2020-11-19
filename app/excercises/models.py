from app import db
from sqlalchemy_serializer import SerializerMixin


excerciseToTag = db.Table('excercisetotag',
    db.Column('excercise_id', db.Integer, db.ForeignKey('excercise.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)


class Excercise(db.Model, SerializerMixin):
#fields
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(512), unique=True)
    movieLink = db.Column(db.String(512))
#relations
    tags = db.relationship('Tag', secondary=excerciseToTag, lazy=True, back_populates="excercise")
#methods
    def __repr__(self):
        return '<\nExcercise name: {}\n Description: {}\n Link: {}\n>'.format(self.name, self.description, self.movieLink)


class Tag(db.Model, SerializerMixin):
#fields
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, unique=True)
    category = db.Column(db.String(512))
#relations
    excercise = db.relationship('Excercise', secondary=excerciseToTag, lazy=True, back_populates="tags")
#methods
    def __repr__(self):
        return '<\nTag name: {}\n Category: {}\n>'.format(self.name, self.category)
