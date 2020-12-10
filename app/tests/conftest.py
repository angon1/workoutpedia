import pytest
from app.excercises.models import Excercise,Tag


@pytest.fixture(scope='module')
def test_excercise():
    return {
        'name':'unittest1',
        'description':'description1',
        'movieLink':'link1'
    }

@pytest.fixture(scope='module')
def test_tags():
    return [
        {
            'name':'tag1',
            'category':'category1'
        },
        {
            'name':'tag2',
            'category':'category2'
        }
    ]

@pytest.fixture(scope='function')
def new_excercise(test_excercise):
    excercise = Excercise(name=test_excercise['name'], description=test_excercise['description'], movieLink=test_excercise['movieLink'])
    yield excercise
    excercise.tags = []


@pytest.fixture(scope='function')
def new_tags(test_tags):
    tags = [
        Tag(name=test_tags[0]['name'],category=test_tags[0]['category']),
        Tag(name=test_tags[1]['name'],category=test_tags[1]['category'])
        ]
    return tags





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
