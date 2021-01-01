from factory import alchemy, Faker, Sequence
from podemos.models.client import ClientModel
from database import db_session

class ClientFactory(alchemy.SQLAlchemyModelFactory):
    id = Sequence(lambda n: 'abc-%03d' % n)
    nombre = Faker('name')

    class Meta:
        model = ClientModel
        sqlalchemy_session = db_session