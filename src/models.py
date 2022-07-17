from sqlalchemy import Column, Float, ForeignKey, Integer, String, DATE
import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

from src.cfg import CATEGORY_TABLE_NAME, PRODUCT_PRICE_TIMELAPSE_TABLE_NAME, PRODUCT_TABLE_NAME, SUPERMARKET_TABLE_NAME

Base = declarative_base()


class CategoryModel(Base):
    __tablename__ = CATEGORY_TABLE_NAME
    id = Column(String(8), primary_key=True)
    name = Column(String(100), nullable=False)


class SupermarketModel(Base):
    __tablename__ = SUPERMARKET_TABLE_NAME
    id = Column(String(8), primary_key=True)
    name = Column(String(100), nullable=False)


class ProductModel(Base):
    __tablename__ = PRODUCT_TABLE_NAME
    id = Column(String(8), primary_key=True)
    name = Column(String(255), nullable=False)
    id_category = Column(String(8), ForeignKey('category.id'))
    id_supermarket = Column(String(8), ForeignKey('supermarket.id'))
    url = Column(String(2083), nullable=False)


class ProductPricesTimelapseModel(Base):
    __tablename__ = PRODUCT_PRICE_TIMELAPSE_TABLE_NAME
    id = Column(Integer, primary_key=True)
    id_product = Column(String(8), ForeignKey('product.id'))
    price = Column(Float(precision=2), nullable = False)
    date = Column(DATE, server_default=sqlalchemy.func.now())
