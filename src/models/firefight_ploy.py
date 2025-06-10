from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from models.base import Base


class FireFightPloy(Base):
    __tablename__ = 'firefight_ploy'

    id = Column(Integer, primary_key=True)
    fraction_id = Column(Integer, ForeignKey('fraction.id'))
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)

    fraction = relationship("Fraction", back_populates="firefight_ploys")