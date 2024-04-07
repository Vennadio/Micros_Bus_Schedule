from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

SQLALCHEMY_DATABASE_URL = "postgresql://user:password@db/dbname"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Stop(Base):
    __tablename__ = "stops"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)


Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class StopCreate(BaseModel):
    name: str
    location: str

@app.post("/stops/")
def create_stop(stop: StopCreate, db: Session = Depends(get_db)):
    db_stop = Stop(name=stop.name, location=stop.location)
    db.add(db_stop)
    db.commit()
    db.refresh(db_stop)
    return db_stop

@app.get("/stops/")
def read_stops(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    stops = db.query(Stop).offset(skip).limit(limit).all()
    return stops
