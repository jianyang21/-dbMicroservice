from sqlalchemy import Column, String, Float, JSON, TIMESTAMP, ARRAY, ForeignKey
from sqlalchemy.sql import func
from .database import Base

class Merchant(Base):
    __tablename__ = "Merchant"
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    shop_domain = Column(String, unique=True, nullable=False)

class Product(Base):
    __tablename__ = "Product"
    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    vendor = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    discount = Column(Float, nullable=False)
    size = Column(ARRAY(String))
    tags = Column(ARRAY(String))
    merchant_id = Column(String, ForeignKey("Merchant.id"), nullable=False)
    createdAt = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updatedAt = Column(TIMESTAMP, nullable=False)
    shopify_id = Column(String, unique=True, nullable=False)
    images = Column(ARRAY(String))
    inventory_quantity = Column(String, nullable=False)
    type = Column(String, nullable=False)
