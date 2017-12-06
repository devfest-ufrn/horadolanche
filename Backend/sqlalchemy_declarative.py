import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()
 
class UnregisteredUser(Base):
    __tablename__ = 'unregistereduser'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    latitude = Column(Integer, nullable=True)
    longitude = Column(Integer, nullable=True)

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True) 
    username = Column(String(20), nullable=False , unique=True)
    email = Column(String(30), nullable=False)
    password = Column(String(40), nullable=False)
    name = Column(String(250), nullable=False)
    account_image = Column(String(140), nullable=True)
    latitude = Column(Integer, nullable=True)
    longitude = Column(Integer, nullable=True)

class Seller(Base):
    __tablename__ = 'seller'
    
    id = Column(Integer, primary_key=True)
    true_id = Column(Integer, ForeignKey('user.id'), unique=True, nullable=False)
    cpf = Column(String(11), nullable=False)
    cnpj = Column(String(14), nullable=True)
    data = relationship(User, uselist=False)
 
class Product(Base):
    __tablename__ = 'product'
    
    id = Column(Integer, primary_key=True)
    seller = Column(Integer, ForeignKey('seller.id'), unique=True, nullable=False)
    price = Column(Float, nullable=False)
    avaliable = Column(Boolean, nullable=False) 
    image = Column(String(140), nullable=False)
    start_sell_time = Column(String(4), nullable=True)
    end_sell_time = Column(String(4), nullable=True)
    seller_info = relationship(Seller, uselist=False)

class UserSeller(Base):
    __tablename__ = 'userseller'
    
    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey('user.id'))
    seller = Column(Integer, ForeignKey('seller.id'))

class ProductCategory(Base):
    __tablename__ = 'productcategory'
    
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    category = Column(String (20), nullable=False)


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///sqlalchemy_hdl.db')
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)