from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.databases import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    # ORM Support
    transactions = relationship("Transaction", back_populates="operator")

class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True)
    product_barcode = Column(String)
    product_name = Column(String)
    product_price = Column(Float)
    product_quantity = Column(Integer)

    # ORM Support
    transaction_details = relationship("TransactionDetail", back_populates="product")

class Transaction(Base):
    __tablename__ = 'transaction'

    transaction_id = Column(Integer, primary_key=True, autoincrement=True)
    transaction_date = Column(DateTime, default=func.now(), nullable=False)
    transaction_operator = Column(Integer, ForeignKey('users.user_id'), nullable=False)

    # ORM Support
    operator = relationship("User", back_populates="transactions")
    transaction_details = relationship("TransactionDetail", back_populates="transaction")

class TransactionDetail(Base):
    __tablename__ = 'transaction_details'

    transaction_detail_id = Column(Integer, primary_key=True, autoincrement=True)
    transaction_detail_transaction = Column(Integer, ForeignKey('transaction.transaction_id'), nullable=False)
    transaction_detail_product = Column(Integer, ForeignKey('products.product_id'), nullable=False)
    transaction_detail_quantity = Column(Integer)
    transaction_detail_price = Column(Float)
    transaction_detail_subtotal = Column(Float)

    # ORM Support
    transaction = relationship("Transaction", back_populates="transaction_details")
    product = relationship("Product", back_populates="transaction_details")