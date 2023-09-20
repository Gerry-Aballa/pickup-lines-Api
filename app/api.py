from sqlalchemy import func
from sqlalchemy.orm import Session

from app import models, schemas


def get_random_pickupline(db: Session ):
    return db.query(models.Line).order_by(func.random()).first()

def create_pickupline(db: Session, line: schemas.LineCreate):
    db_line = models.Line(mood=line.mood, pickupline=line.pickupline)
    db.add(db_line)
    db.commit()
    db.refresh(db_line)
    return db_line