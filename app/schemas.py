from datetime import datetime
from typing import Literal, Optional, List
from pydantic import BaseModel, EmailStr, constr


"""Request schema for USER SIGNUP"""
class BaseUsers(BaseModel):
    firstName:constr(to_lower=True, max_length=20, min_length=3, strip_whitespace=True)
    lastName:constr(to_lower=True, max_length=20, min_length=3, strip_whitespace=True)
    username:constr(to_lower=True, max_length=20, min_length=3, strip_whitespace=True) 
    email:EmailStr
    password:str
    role:Literal['user']
    contactNumber:constr(max_length=10, min_length=10, strip_whitespace=True)
    profilePicture:str


"""Request schema for ADMIN SIGNUP"""
class BaseAdmin(BaseModel):
    firstName:constr(to_lower=True, max_length=20, min_length=3, strip_whitespace=True)
    lastName:constr(to_lower=True, max_length=20, min_length=3, strip_whitespace=True)
    username:constr(to_lower=True, max_length=20, min_length=3, strip_whitespace=True) 
    email:EmailStr
    password:str
    role:Literal['admin']
    contactNumber:constr(max_length=10, min_length=10, strip_whitespace=True)
    profilePicture:str


# """Template response for users"""
# class User(BaseModel):
#     id:int
#     firstName:str
#     lastName:str
#     username:str
#     role:str
#     contactNumber:str
#     profilePicture:str

"""Response schema for USER TOKEN"""
class User_Token(BaseModel):
    user_access_token:str
    token_type:str



"""Response schema for ADMIN TOKEN"""
class Admin_Token(BaseModel):
    admin_access_token:str
    token_type:str



# """Response schema for Profile"""
# class Profile(BaseModel):   
#     username: User


class TokenData(BaseModel):
    id:Optional[int] = None # to validate the token data


"""Request Schema for create-category"""
class Category(BaseModel):
    name:constr(to_lower=True, max_length=80, min_length=2, strip_whitespace=True)
    slug:str
    parentId:Optional[int] = None 

"""Request Schema for create-product"""


class Product(BaseModel):
    name:constr(to_lower=True, max_length=80, min_length=2, strip_whitespace=True)
    slug:str
    description: constr(to_lower=True, max_length=20, min_length=3, strip_whitespace=True)  
    offer: Optional[int] = None
