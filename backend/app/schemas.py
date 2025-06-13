from pydantic import BaseModel
from datetime import date

class CarCreate(BaseModel):
    model: str
    plate: str

class CarRead(CarCreate):
    id: int
    class Config:
        orm_mode = True

class CustomerCreate(BaseModel):
    name: str
    email: str

class CustomerRead(CustomerCreate):
    id: int
    class Config:
        orm_mode = True

class RentalCreate(BaseModel):
    car_id: int
    customer_id: int
    start_date: date
    due_date: date

class RentalRead(RentalCreate):
    id: int
    car: CarRead
    customer: CustomerRead
    class Config:
        orm_mode = True
