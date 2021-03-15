import pytest, tempfile, os
from app import create_app, db
from app.exercises.models import Exercise, Tag
from flask_sqlalchemy import SQLAlchemy

from config import Config

# db = SQLAlchemy()


class TestConfig(Config):
    basedir = os.path.abspath(os.path.dirname(__file__))
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "test.db")


class ExerciseDatabaseChecker:
    @staticmethod
    def check_if_name_exist(name, client):
        if (Exercise.query.filter_by(name=name).first()) is not None:
            return True
        else:
            return False


class TagDatabaseChecker:
    @staticmethod
    def check_if_name_exist(name, client):
        if (Tag.query.filter_by(name=name).first()) is not None:
            return True
        else:
            return False

    @staticmethod
    def check_if_category_exist(category, client):
        if (Tag.query.filter_by(category=category).first()) is not None:
            return True
        else:
            return False


@pytest.fixture(scope="function")
def app():

    """Create and configure a new app instance for each test."""
    # create a temporary file to isolate the database for each test

    app = create_app(TestConfig)
    app_context = app.app_context()
    app_context.push()
    db.create_all()

    yield app
    db.session.remove()
    db.drop_all()
    app_context.pop()


@pytest.fixture(scope="function")
def client(app):
    """A test client for the app."""
    return app.test_client()


# from config import Config
# from app import create_app
# class TestConfig(Config):
#     TESTING = True
# SQLALCHEMY_DATABASE_URI = 'sqlite://'

# class UserModelCase(unittest.TestCase):
#     def setUp(self):
#         self.app = create_app(TestConfig)
#         self.app_context = self.app.app_context()
#         self.app_context.push()
#         db.create_all()

#     def tearDown(self):
#         db.session.remove()
#         db.drop_all()
#         self.app_context.pop()


@pytest.fixture(scope="module")
def test_exercise():
    return {"name": "unittest1", "description": "description1", "movieLink": "link1"}


@pytest.fixture(scope="module")
def test_exercise_incorrect():
    return {
        "name": "unittest1",
        "description": "description1",
    }


@pytest.fixture(scope="module")
def test_tags():
    return [
        {"name": "tag1", "category": "category1"},
        {"name": "tag2", "category": "category2"},
    ]


@pytest.fixture(scope="module")
def test_tag():
    return {"name": "tag1", "category": "category1"}


@pytest.fixture(scope="module")
def test_tags_incorrect():
    return [
        {
            "name": "tag1",
        }
    ]


@pytest.fixture(scope="function")
def new_exercise(app, test_exercise):
    exercise = Exercise(
        name=test_exercise["name"],
        description=test_exercise["description"],
        movieLink=test_exercise["movieLink"],
    )
    db.session.add(exercise)
    db.session.commit()
    yield exercise
    exercise.tags = []


@pytest.fixture(scope="function")
def new_tags(app, test_tags):
    tags = [
        Tag(name=test_tags[0]["name"], category=test_tags[0]["category"]),
        Tag(name=test_tags[1]["name"], category=test_tags[1]["category"]),
    ]
    # for tag in tags:
    db.session.add(tags[0])
    db.session.add(tags[1])
    db.session.commit()
    yield tags


@pytest.fixture(scope="function")
def new_exercise_with_tags(app, test_exercise, new_tags):
    exercise = Exercise(
        name=test_exercise["name"],
        description=test_exercise["description"],
        movieLink=test_exercise["movieLink"],
    )
    exercise.addTagsList([new_tags[0], new_tags[1]])
    db.session.add(exercise)
    db.session.commit()
    yield exercise
    exercise.tags = []


# @pytest.fixture
# def client():
#     db_fd, app.config['DATABASE'] = tempfile.mkstemp()
#     app.config['TESTING'] = True

#     with app.test_client() as client:
#         with app.app_context():
#             app.init_db()
#         yield client

#     os.close(db_fd)
#     os.unlink(app.config['DATABASE'])
