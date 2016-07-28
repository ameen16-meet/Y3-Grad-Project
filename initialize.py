from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import Base, Person

engine = create_engine('sqlite:///flasky.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSessionMaker = sessionmaker(bind=engine)
dbSession = DBSessionMaker()

### These are the commands you just saw live.

marvin = Person(
        name='Marvin Arnold',
        gender='male',
        nationality='American',
        hometown='New Orleans')

lorenzo = Person(
        name='Lorenzo Brown',
        gender='male',
        nationality='American',
        hometown='Dallas')

anna = Person(
        name='Anna Premo',
        gender='female',
        nationality='American',
        hometown='Pittsburg')

lisa = Person(
        name='Lisa Kavanaugh',
        gender='female',
        nationality='German',
        hometown='Fairbanks')

eric = Person(
        name='Eric Westberg',
        gender='male',
        nationality='American',
        hometown='Durango')

# This deletes everything in your database.
dbSession.query(Person).delete()
dbSession.commit()

# This adds some rows to the database. Make sure you `commit` after `add`ing!
dbSession.add(marvin)
dbSession.add(lorenzo)
dbSession.add(anna)
dbSession.add(lisa)
dbSession.add(eric)
dbSession.commit()

