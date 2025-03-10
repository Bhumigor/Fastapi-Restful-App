from sqlalchemy import MetaData
from models.user import users
from config.db import meta, engine

meta = MetaData()

meta.create_all(engine)
