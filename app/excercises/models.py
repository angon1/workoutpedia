from flask import current_app
from app import db
from sqlalchemy_serializer import SerializerMixin
from .validators import ExcerciseValidator

excerciseToTag = db.Table(
    "excercisetotag",
    db.Column(
        "excercise_id", db.Integer, db.ForeignKey("excercise.id"), primary_key=True
    ),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"), primary_key=True),
)


class Excercise(db.Model, SerializerMixin):
    # fields
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(512), unique=True)
    movieLink = db.Column(db.String(512))
    # relations
    tags = db.relationship(
        "Tag", secondary=excerciseToTag, lazy=True, back_populates="excercise"
    )
    # methods
    def __repr__(self):
        return "<\nExcercise name: {}\n Description: {}\n Link: {}\n Tags: {}>".format(
            self.name, self.description, self.movieLink, self.tagsDict()
        )

    def addTag(self, tag):
        self.tags.append(tag)
        db.session.commit()
        return True

    def addTagsList(self, tagsList):
        for tag in tagsList:
            self.tags.append(tag)
        db.session.commit()
        return True

    def removeTag(self, tag):
        if tag in self.tags:
            self.tags.remove(tag)
            db.session.commit()
            return True
        else:
            return False

    def tagsDict(self):
        tagDict = []
        for t in self.tags:
            tagDict.append(t.asDict())
        return tagDict

    def asDict(self):
        excerciseDict = self.to_dict(rules=("-tags.excercise",))
        return excerciseDict

    def asDictNoTags(self):
        excerciseDict = self.to_dict(rules=("-tags",))
        return excerciseDict

    @classmethod
    def from_json_request(cls, params):
        if params is

class Tag(db.Model, SerializerMixin):
    # fields
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, unique=True)
    category = db.Column(db.String(512))
    # relations
    excercise = db.relationship(
        "Excercise", secondary=excerciseToTag, lazy=True, back_populates="tags"
    )
    # methods
    def __repr__(self):
        return "{}".format(self.asDict())

    def asDict(self):
        return {"id": self.id, "name": self.name, "category": self.category}

    def addExcercise(self, excercise):
        self.excercise.append(excercise)
        db.session.commit()
        return True

    def getExcercises(self):
        excercises = []
        for e in self.excercise:
            excercises.append(e.asDictNoTags())
        return excercises

    def getCategory(self):
        return self.category
