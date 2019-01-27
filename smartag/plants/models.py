from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from smartag.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class Plant(Base):
    __tablename__ = 'plants'

    pid = Column(String(20), primary_key=True)
    uid = Column(Integer)
    name = Column(String(20), ForeignKey('plant_types.name'))
    ptype = relationship("PlantType", back_populates="plants")
    water_level = Column(Float)
    chemical_a = Column(Float)
    chemical_b = Column(Float)
    growth_level = Column(Float)
    timestamp = Column(Integer, nullable=True)
    state = Column(Integer)

    def __init__(self, pid=('-1--1'), uid=0, name='Unknown', water_level=0,
        chemical_a=0, chemical_b=0, growth_level=0, timestamp=0, state=1):
        self.pid = pid
        self.uid = uid
        self.name = name
        self.water_level = water_level
        self.chemical_a = chemical_a
        self.chemical_b = chemical_b
        self.growth_level = growth_level
        self.timestamp = timestamp
        self.state = state

    def __repr__(self):
        return f"Type: '{self.name}', ID: '{self.pid}'"

class PlantType(Base):
    __tablename__ = 'plant_types'

    name = Column(String(20), primary_key=True)
    plants = relationship("Plant", order_by=Plant.pid, back_populates='ptype')

    def __init__(self, name='basil'):
        self.name = name
    
    def __repr__(self):
        return f"Type: '{self.name}'"

'''
from sqlalchemy import Column, Integer, String
from yourapplication.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)
'''