from .db_setup import Base
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Index, Integer, String, text
from sqlalchemy.orm import relationship
# from sqlalchemy_imageattach.entity import Image, image_attachment


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False )
    last_name = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False )
    contact_number = Column(String)
    # profile_picture = image_attachment('UserPicture')
    # products = relationship(
    #     "Product", back_populates="user", cascade="all, delete-orphan"
    # )
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

Index("idx_username", User.username, postgresql_include=['id'])


# class UserPicture(Base, Image):
#     """User picture model."""
#     __tablename__ = 'user_picture'

#     user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
#     user = relationship('User')



class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    slug = Column(String, nullable=False, unique=True)
    parent_id = Column(Integer, ForeignKey("category.id", ondelete='CASCADE'), nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    slug = Column(String, nullable=False, unique=True)
    price = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    offer = Column(Integer, nullable=True)
    # product_picture =  image_attachment('ProductPicture')
    # reviews = Column(String, ForeignKey("users.id", ondelete='CASCADE'), nullable=True)
    # created_by = Column(Integer, ForeignKey("users"), nullable=False)
    # user = relationship("User", back_populates="products")
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


# class ProductPicture(Base, Image):
#     """Product picture model."""
#     __tablename__ = 'product_picture'

#     user_id = Column(Integer, ForeignKey('product.id'), primary_key=True)
#     product = relationship('Product')