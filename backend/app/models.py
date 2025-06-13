from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Car(Base):
    __tablename__ = "cars"
    id        = Column(Integer, primary_key=True, index=True)
    model     = Column(String, index=True)
    plate     = Column(String, unique=True, index=True)

class Customer(Base):
    __tablename__ = "customers"
    id        = Column(Integer, primary_key=True, index=True)
    name      = Column(String)
    email     = Column(String, unique=True, index=True)

class Rental(Base):
    __tablename__ = "rentals"
    id         = Column(Integer, primary_key=True, index=True)
    car_id     = Column(Integer, ForeignKey("cars.id"))
    customer_id= Column(Integer, ForeignKey("customers.id"))
    start_date = Column(Date)
    due_date   = Column(Date)

    car        = relationship("Car")
    customer   = relationship("Customer")
