import pytest
from app.excercises.models import Excercise,Tag



@pytest.fixture(scope='module')
def new_excercise():
    excercise = Excercise(name='unittest1', description='description1', movieLink='link1')
    return excercise
