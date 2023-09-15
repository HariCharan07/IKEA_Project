from fastapi import FastAPI
from pydantic import BaseModel
from bson import ObjectId
from typing import Optional
from datetime import datetime
class usersignup(BaseModel):
    email:str
    name:str
    # lastname:str
    # dob:str
    # country: str
    # address: Optional[str]   
    # preferredstore:Optional[str]
    # mobilenumber:Optional[str]
    # email:str
    password:str
    confirmPassword:str
    # city: Optional[str]
    # postal_code:Optional[str]
class userLoginSchema(BaseModel):
    email: str
    password: str 
class ForgotPasswordSchema(BaseModel):
    email:str
class emailVerifyOtpSchema(BaseModel):
    otp: str