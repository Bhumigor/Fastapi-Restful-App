from models.user import User
from config.db import Base, engine

Base.metadata.create_all(bind=engine)

