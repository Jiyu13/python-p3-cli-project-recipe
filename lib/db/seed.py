from random import random, randint, choice as rc

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///recipes.db')
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()