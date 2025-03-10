from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.index import User
from sqlalchemy import select

user = APIRouter()

# Helper function to serialize database rows into dictionaries
def serialize(rows):
    return [dict(row._mapping) for row in rows]

@user.get("/")
async def read_data():
    result = conn.execute(select(users)).fetchall()
    return serialize(result)

@user.get("/{id}")
async def read_single_data(id: int):
    result = conn.execute(select(users).where(users.c.id == id)).fetchall()
    return serialize(result)

@user.post("/")
async def write_data(user: User):
    conn.execute(users.insert().values(
        id=user.id,
        name=user.name,
        email=user.email,
        password=user.password
    ))
    conn.commit()
    return {"message": "User created successfully"}

@user.put("/{id}")
async def update_data(id: int, user: User):
    conn.execute(users.update().where(users.c.id == id).values(
        name=user.name,
        email=user.email,
        password=user.password
    ))
    conn.commit()
    return {"message": "User updated successfully"}

@user.delete("/{id}")
async def delete_data(id: int):
    conn.execute(users.delete().where(users.c.id == id))
    conn.commit()
    return {"message": "User deleted successfully"}
