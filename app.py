from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import declarative_base, sessionmaker, Session
import os

# Database setup
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/mydb")
try:
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()

    # Database model
    class Item(Base):
        __tablename__ = "items"
        id = Column(Integer, primary_key=True, index=True)
        name = Column(String, index=True)
        description = Column(String)

    # Create tables
    Base.metadata.create_all(bind=engine)
except Exception:
    # For testing without database
    Base = declarative_base()
    SessionLocal = None
    
    class Item(Base):
        __tablename__ = "items"
        id = Column(Integer, primary_key=True, index=True)
        name = Column(String, index=True)
        description = Column(String)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World with Database"}

@app.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item:
        return {"id": item.id, "name": item.name, "description": item.description}
    return {"error": "Item not found"}

@app.post("/items/")
def create_item(name: str, description: str, db: Session = Depends(get_db)):
    item = Item(name=name, description=description)
    db.add(item)
    db.commit()
    db.refresh(item)
    return {"id": item.id, "name": item.name, "description": item.description}