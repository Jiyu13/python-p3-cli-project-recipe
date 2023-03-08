from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, Float, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Author(Base):

    __tablename__ = "authors"
    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    books = relationship("CookBook", backref=backref("author"))

    def __repr__(self):
        return f'Author(id={self.id}, ' + \
            f'full name={self.first_name} {self.last_name}'


class CookBook(Base):
    __tablename__ = "cookbooks"
    id = Column(Integer(), primary_key=True)
    name = Column(String())

    author_id = Column(Integer(), ForeignKey("authors.id"))
    recipes = relationship("Recipe", backref=backref("cookbook"))

    def __repr__(self):
        return f'CookBook(id={self.id}, ' + \
            f'full name={self.name}'



class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer(), primary_key=True)
    category = Column(String())
    link = Column(String())

    book_id = Column(Integer(), ForeignKey("cookbooks.id"))


    def __repr__(self):
        return f'Recipe(id={self.id}, ' + \
            f'category={self.category}' + \
            f'link={self.link}'