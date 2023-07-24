from .database import Base
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Index, Integer, String, text


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    firstName = Column(String, nullable=False )
    lastName = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False )
    contactNumber = Column(String)
    profilePicture = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

Index("idx_username", User.username, postgresql_include=['id'])


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    slug = Column(String, nullable=False, unique=True)
    parentId = Column(Integer, ForeignKey("category.id", ondelete='CASCADE'), nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))