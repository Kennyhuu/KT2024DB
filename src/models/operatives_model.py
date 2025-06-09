from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship, declarative_base
from models.base import Base

class Fraction(Base):
    __tablename__ = 'fraction'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    operatives = relationship("Operative", back_populates="fraction")
    gear_items = relationship("Equipment", back_populates="fraction")
    strategic_ploys = relationship("StrategicPloy", back_populates="fraction")
    firefight_ploys = relationship("FireFightPloy", back_populates="fraction")


class Operative(Base):
    __tablename__ = 'operatives'

    id = Column(Integer, primary_key=True)
    fraction_id = Column(Integer, ForeignKey('fraction.id'))
    name = Column(Text, nullable=False)
    type = Column(Text)
    apl = Column(Integer)
    move = Column(Text)
    save = Column(Text)
    wounds = Column(Integer)
    weapons = Column(JSONB)  # JSONB in PostgreSQL
    abilities = Column(JSONB)

    fraction = relationship("Fraction", back_populates="operatives")
