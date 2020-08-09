from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from .database import Base


class Punish(Base):
    __tablename__ = "punish"

    id = Column(Integer, primary_key=True, index=True)
    task = Column(String)
    # is_active = Column(Boolean, default=True)
    value = Column(Integer)