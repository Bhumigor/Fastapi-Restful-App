from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from config.db import get_db
from models.index import User
from schemas.index import UserSchema
from utils.security import hash_password, verify_password, encode_password
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

user = APIRouter()


@user.get("/")
async def read_data(db: Session = Depends(get_db)):
    users = db.query(User).all()
    print([{"id": u.id, "name": u.name, "email": u.email, "password":u.password} for u in users] )
    return [{"id": u.id, "name": u.name, "email": u.email, "password":u.password} for u in users] 


@user.get("/{id}")
async def read_single_data(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user.id, "name": user.name, "email": user.email, "password":user.password}  # Hide password


@user.post("/")
async def write_data(user_data: UserSchema, db: Session = Depends(get_db)):
    hashed_password = hash_password(user_data.password)
    new_user = User(id=user_data.id, name=user_data.name, email=user_data.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    return {"message": "User created successfully"}


class UpdateUserRequest(BaseModel):
    name: Optional[str] = Field(None, example="John Doe")
    email: Optional[EmailStr] = Field(None, example="john@example.com")
    password: Optional[str] = Field(None, example="NewPassword@123")


@user.put("/users/{id}")
async def update_user(id: int, user_data: UpdateUserRequest, db: Session = Depends(get_db)):
    user_record = db.query(User).filter(User.id == id).first()
    if not user_record:
        raise HTTPException(status_code=404, detail="User not found")

    update_data = user_data.dict(exclude_unset=True)

    if "password" in update_data:
        update_data["password"] = hash_password(update_data["password"])

    for key, value in update_data.items():
        setattr(user_record, key, value)

    db.commit()
    db.refresh(user_record)
    return {"message": "User updated successfully", "updated_fields": list(update_data.keys())}


@user.delete("/{id}")
async def delete_data(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}

