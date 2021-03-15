from flask import current_app
from app import db
from sqlalchemy_serializer import SerializerMixin
from .validators import ExerciseValidator


exerciseToTag = db.Table(
    "exercisetotag",
    db.Column(
        "exercise_id", db.Integer, db.ForeignKey("exercise.id"), primary_key=True
    ),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"), primary_key=True),
)


class ExerciseCommand:
    @staticmethod
    def create_or_none_if_already_in_db(params):
        exercise = Exercise.query.filter_by(name=params["name"]).first()
        if exercise is not None:
            return False
        else:
            exercise = Exercise(
                params["name"], params["description"], params["movieLink"]
            )
            db.session.add(exercise)
            db.session.commit()
            return True

    @staticmethod
    def update(id, params):
        exercise = Exercise.query.filter_by(id=id).first()
        if exercise is None:
            return False
        else:
            exercise.name = params["name"]
            exercise.description = params["description"]
            exercise.movieLink = params["movieLink"]
            db.session.commit()
            return True

    @staticmethod
    def remove_from_db(id):
        exercise = Exercise.query.filter_by(id=id).first()
        if exercise is None:
            return False
        else:
            db.session.delete(exercise)
            db.session.commit()
            return True


class ExerciseQuery:
    @staticmethod
    def get_from_db_or_none(id):
        return Exercise.query.filter_by(id=id).first()

    @staticmethod
    def get_name_from_db_or_none(name):
        return Exercise.query.filter_by(name=name).first()

    @staticmethod
    def __tags_dict(exercise):
        return exercise.only_tags_dict()

    @classmethod
    def get_tags_dict_from_db_or_none(cls, id):
        exercise = Exercise.query.filter_by(id=id).first()
        if exercise is None:
            return None
        else:
            return cls().__tags_dict(exercise)


class Exercise(db.Model, SerializerMixin):
    # class fields
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(512), unique=True)
    movieLink = db.Column(db.String(512))
    # constructor
    def __init__(self, name, description, movieLink):
        self.name = name
        self.description = description
        self.movieLink = movieLink

    # relations
    tags = db.relationship(
        "Tag", secondary=exerciseToTag, lazy=True, back_populates="exercise"
    )
    # methods
    def __repr__(self):
        return "<\nExercise name: {}\n Description: {}\n Link: {}\n Tags: {}>".format(
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
        exerciseDict = self.to_dict(rules=("-tags.exercise",))
        return exerciseDict

    def asDictNoTags(self):
        exerciseDict = self.to_dict(rules=("-tags",))
        return exerciseDict

    def only_tags_dict(self):
        return self.to_dict(only=("tags",), rules=("-tags.exercise",))


class TagCommand:
    @staticmethod
    def create_if_not_in_db(params):
        tag = Tag.query.filter_by(name=params["name"]).first()
        if tag is not None:
            return False
        else:
            tag = Tag(params["name"], params["category"])
            db.session.add(tag)
            db.session.commit()
            return True

    @classmethod
    def __validate_if_name_is_not_a_duplicate(cls, id, name):
        if Tag.query.filter_by(name=name).first().id == id:
            return True
        return False

    @staticmethod
    def update(id, params):
        tag = Tag.query.filter_by(id=id).first()
        if tag is None:
            return False
        elif False == TagCommand.__validate_if_name_is_not_a_duplicate(
            id, params["name"]
        ):
            return False
        else:
            tag.name = params["name"]
            tag.category = params["category"]
            db.session.commit()
            return True

    @staticmethod
    def delete(id):
        tag = Tag.query.filter_by(id=id).first()
        if tag is None:
            return False
        else:
            db.session.delete(tag)
            db.session.commit()
            return True


class Tag(db.Model, SerializerMixin):
    # fields
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, unique=True)
    category = db.Column(db.String(512))
    # relations
    exercise = db.relationship(
        "Exercise", secondary=exerciseToTag, lazy=True, back_populates="tags"
    )
    # methods
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def __repr__(self):
        return "{}".format(self.asDict())

    def asDict(self):
        return {"id": self.id, "name": self.name, "category": self.category}

    def addExercise(self, exercise):
        self.exercise.append(exercise)
        db.session.commit()
        return True

    def getExercises(self):
        exercises = []
        for e in self.exercise:
            exercises.append(e.asDictNoTags())
        return exercises

    def getCategory(self):
        return self.category
