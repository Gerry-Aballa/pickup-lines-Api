from sqlalchemy import Column, Integer, String
from .dependencies.database import Base

# Define database model using SQLAlchemy
class Line(Base):
    __tablename__ = "lines"

    id = Column(Integer, primary_key=True, index=True)
    mood = Column(String)
    pickupLine = Column(String)