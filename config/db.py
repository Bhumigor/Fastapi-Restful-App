from sqlalchemy import create_engine #MetaData
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("mysql+pymysql://root:admin@localhost:3306/fastapi")


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()