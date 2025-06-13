from sqlalchemy.orm import Session
from . import models, schemas

def create_car(db: Session, car: schemas.CarCreate):
    db_car = models.Car(**car.dict())
    db.add(db_car); db.commit(); db.refresh(db_car)
    return db_car

def list_cars(db: Session, skip=0, limit=100):
    return db.query(models.Car).offset(skip).limit(limit).all()

# (idem para customer e rental)

def delete_car(db: Session, car_id: int):
    car = db.query(models.Car).filter(models.Car.id == car_id).first()
    if not car:
        return False
    db.delete(car)
    db.commit()
    return True
