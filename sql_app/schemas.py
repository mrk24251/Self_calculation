from typing import List, Optional

from pydantic import BaseModel

class PunishValue(BaseModel):
    value: int

class PunishCreate(PunishValue):
    task: str

class Punish(PunishCreate):
    id: int

    class Config:
        orm_mode = True