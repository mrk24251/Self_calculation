from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Date
import datetime

from .database import Base

class Punish(Base):
    __tablename__ = "punish"

    id = Column(Integer, primary_key=True, index=True)
    task = Column(String)
    # is_active = Column(Boolean, default=True)
    value = Column(Integer)

class Spirit(Base):
    __tablename__ = "spirit"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    # is_active = Column(Boolean, default=True)

class Restriction(Base):
    __tablename__ = "restriction"

    id = Column(Integer, primary_key=True, index=True)
    reason = Column(String)
    endingWith = Column(String)
    myRestriction = Column(String)
    created_date = Column(Date, default=datetime.date.utcnow)

