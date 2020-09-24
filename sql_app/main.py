from typing import List,Optional
from fastapi import Depends, FastAPI, HTTPException,Query,Path
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

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
def read_punish_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    punishes = crud.get_punishes(db, skip=skip, limit=limit)
    return punishes


@app.get("/punishes/{punish_id}", response_model=schemas.Punish)
def read_punish(punish_id: int, db: Session = Depends(get_db)):
    db_punish = crud.get_punish(db, punish_id=punish_id)
    if db_punish is None:
        raise HTTPException(status_code=404, detail="Punish not found")
    return db_punish

@app.post("/punish_by_value/", response_model=List[schemas.Punish])
def read_punish_by_value(punish: schemas.PunishValue, db: Session = Depends(get_db)):
    db_punish = crud.get_punish_by_value(db, value=punish.value)
    return db_punish

@app.post("/spirits/", response_model=schemas.Spirit)
def create_spirit(spirit: schemas.SpiritCreate, db: Session = Depends(get_db)):
    return crud.create_spirit(db=db, spirit= spirit)

@app.get("/random_spirit/", response_model=schemas.Spirit)
def read_random_spirit(db: Session = Depends(get_db)):
    db_spirit = crud.get_random_spirit(db)
    return db_spirit

@app.get("/restrictions/", response_model=List[schemas.Restriction])
def read_restriction_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    punishes = crud.get_restriction(db, skip=skip, limit=limit)
    return punishes

@app.post("/restrictions/", response_model=schemas.Restriction)
def create_restriction(restriction: schemas.RestrictionCreate, db: Session = Depends(get_db)):
    return crud.create_restriction(db=db, restriction= restriction)

# @app.post("/punishes/{punish_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)


# @app.get("/items/", response_model=List[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items


## authentication and authorization

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user


@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@app.post("/punishes/VIP", response_model=schemas.Punish)
def create_punish(punish: schemas.PunishCreate, db: Session = Depends(get_db),token: str = Depends(oauth2_scheme)):
    return {crud.create_punish(db=db, punish= punish),token}
