from typing import List

from fastapi import Depends, FastAPI, HTTPException,Query,Path
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/punishes/", response_model=schemas.Punish)
def create_punish(punish: schemas.PunishCreate, db: Session = Depends(get_db)):
    return crud.create_punish(db=db, punish= punish)


@app.get("/punishes/", response_model=List[schemas.Punish])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    punishes = crud.get_punishes(db, skip=skip, limit=limit)
    return punishes


@app.get("/punishes/{punish_id}", response_model=schemas.Punish)
def read_punish(punish_id: int, db: Session = Depends(get_db)):
    db_punish = crud.get_punish(db, punish_id=punish_id)
    if db_punish is None:
        raise HTTPException(status_code=404, detail="Punish not found")
    return db_punish

@app.post("/punish_by_value/", response_model=List[schemas.Punish])
def read_user_by_value(punish: schemas.PunishValue, db: Session = Depends(get_db)):
    db_punish = crud.get_punish_by_value(db, value=punish.value)
    return db_punish

# @app.post("/punishes/{punish_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)


# @app.get("/items/", response_model=List[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items