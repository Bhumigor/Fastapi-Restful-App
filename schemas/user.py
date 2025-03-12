from pydantic import BaseModel, EmailStr
from password_validator import PasswordValidator
import validators
#from passlib.context import CryptContext


password_schema = PasswordValidator()
password_schema.min(8).max(20).has().uppercase().lowercase().digits().symbols()

class UserSchema(BaseModel):
    id: int
    name: str 
    email: EmailStr 
    password: str 

    @staticmethod
    def validate_email(email):
        if not validators.email(email):
            raise ValueError("Invalid email address")
        return email
    

    @staticmethod
    def validate_password(password):
        if not password_schema.validate(password):
            raise ValueError("Password must be strong")
        return password
