from sqlalchemy.orm import Session
from random import randrange

from . import models, schemas


def get_punish(db: Session, punish_id: int):
    return db.query(models.Punish).filter(models.Punish.id == punish_id).first()

def get_punish_by_value(db: Session, value: int):
    punish_size = value
    punish_set =[]
    while punish_size >0:
        length = len(db.query(models.Punish).filter(models.Punish.value <= punish_size).all())
        i = randrange(length)
        rand_punish=db.query(models.Punish).filter(models.Punish.value <= punish_size)[i]
        punish_set.append(rand_punish)
        punish_size -= rand_punish.value

    return punish_set

def get_random_spirit(db: Session):
    length = len(db.query(models.Spirit).all())
    i = randrange(length)
    rand_spirit=db.query(models.Spirit)[i]

    return rand_spirit


def get_punishes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Punish).offset(skip).limit(limit).all()


def create_punish(db: Session, punish: schemas.PunishCreate):
    db_punish = models.Punish(task=punish.task, value=punish.value)
    db.add(db_punish)
    db.commit()
    db.refresh(db_punish)
    return db_punish

def create_spirit(db: Session, spirit: schemas.SpiritCreate):
    db_spirit = models.Spirit(text=spirit.text)
    db.add(db_spirit)
    db.commit()
    db.refresh(db_spirit)
    return db_spirit


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item