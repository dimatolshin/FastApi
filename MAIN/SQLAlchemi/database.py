from sqlalchemy import create_engine, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+psycopg2://lion:lion@localhost/lion")

Session = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()


class Person(Base):
    __tablename__ = "peoples"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    UniqueConstraint(name)

Base.metadata.create_all(bind=engine)

db = Session()
tom = Person(name="Tom", age=38)
bob = Person(name="Bob", age=42)
sam = Person(name="Sam", age=25)
db.add(tom)
db.add(bob)
db.add(sam)
db.commit()

# people = db.query(Person).all()
# for p in people:
#     print(f"{p.id}.{p.name} ({p.age})")
#
# user = db.get(Person, 1)
# print(f'{user.name},{user.age}')
#
# filter_people = db.query(Person).filter(Person.id == 2).first()
# print(filter_people.name)
