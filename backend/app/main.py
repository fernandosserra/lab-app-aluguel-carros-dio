from datetime import date

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from . import models, schemas, crud

# -------------------------------------------------------------------
# Configuração do Banco de Dados (SQLite para dev)
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria as tabelas, se não existirem
models.Base.metadata.create_all(bind=engine)

# -------------------------------------------------------------------
# Instância do FastAPI
app = FastAPI(title="Car Rental Washu-sama")

# -------------------------------------------------------------------
# CORS: permita todas as origens (ajuste para produção)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# -------------------------------------------------------------------
# Dependency para obter sessão de DB
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------------------------------------------------------------------
# Endpoints de Carros

@app.post("/cars/", response_model=schemas.CarRead)
def create_car_endpoint(car: schemas.CarCreate, db: Session = Depends(get_db)):
    return crud.create_car(db, car)

@app.get("/cars/", response_model=list[schemas.CarRead])
def read_cars(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.list_cars(db, skip, limit)

@app.delete("/cars/{car_id}", status_code=204)
def remove_car(car_id: int, db: Session = Depends(get_db)):
    sucesso = crud.delete_car(db, car_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Carro não encontrado")
    return None  # 204 No Content

# -------------------------------------------------------------------
# (Aqui você adiciona endpoints de customers e rentals seguindo o mesmo padrão)
