from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, Float, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

cookbook_user = Table(
    "cookbook_users",
    Base.metadata,
    Column('cookbook_id', ForeignKey("cookbooks.id"), primary_key=True),
    Column('user_id', ForeignKey("users.id"), primary_key=True),
    extend_existing=True,
)

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

    users = relationship('User', secondary=cookbook_user, back_populates='cookbooks')

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


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    username = Column(String())

    cookbooks = relationship('CookBook', secondary=cookbook_user, back_populates='users')

    def __repr__(self):
        return f'User(id={self.id}, ' + \
            f'username={self.name}' 
