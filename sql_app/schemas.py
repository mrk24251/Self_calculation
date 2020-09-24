from typing import List, Optional
from pydantic import BaseModel
import datetime
from fastapi import Body

class PunishValue(BaseModel):
    value: int

class PunishCreate(PunishValue):
    task: str

class Punish(PunishCreate):
    id: int

    class Config:
        orm_mode = True


class SpiritCreate(BaseModel):
    text: str

class Spirit(SpiritCreate):
    id: int

    class Config:
        orm_mode = True

class RestrictionCreate(BaseModel):
    reason: str
    endingWith: str
    myRestriction: str

class RestrictionList(RestrictionCreate):
    created_date: Optional[datetime.date] = Body(None)

class Restriction(RestrictionList):
    id: int

    class Config:
        orm_mode = True