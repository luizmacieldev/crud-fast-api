from sqlalchemy.orm import Session
from . import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user_update: schemas.UserUpdate):
    user_db = db.query(models.User).filter(models.User.id == user_id).first()
    if not user_db:
        return None

    if user_update.name is not None:
        user_db.name = user_update.name
    if user_update.email is not None:
        user_db.email = user_update.email

    db.commit()
    db.refresh(user_db)
    return user_db


def delete_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        return None
    db.delete(user)
    db.commit()
    return user
