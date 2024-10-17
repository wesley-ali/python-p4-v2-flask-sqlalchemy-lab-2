from lib2to3.pytree import Base
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base



metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return f'<Customer {self.id}, {self.name}>'


class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)

    def __repr__(self):
        return f'<Item {self.id}, {self.name}, {self.price}>'

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    comment = Column(String, nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)

    customer = relationship('Customer', back_populates='reviews')
    item = relationship('Item', back_populates='reviews')

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    reviews = relationship('Review', back_populates='item')
    # Relationship with Review
    reviews = relationship('Review', back_populates='customer')