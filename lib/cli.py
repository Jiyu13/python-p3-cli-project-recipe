#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///db/recipes.db')
session = sessionmaker(bind=engine)()

if __name__ == '__main__':
    pass