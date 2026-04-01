from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Salon(Base):
    __tablename__ = 'salons'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    owner = Column(String(100))
    financial_records = relationship("FinancialRecord", back_populates="salon")

class FinancialRecord(Base):
    __tablename__ = 'financial_records'
    id = Column(Integer, primary_key=True)
    salon_id = Column(Integer, ForeignKey('salons.id'))
    period_start = Column(DateTime)
    period_end = Column(DateTime)
    salon = relationship("Salon", back_populates="financial_records")

class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True)
    record_id = Column(Integer, ForeignKey('financial_records.id'))
    category = Column(String(50))
    amount = Column(Float)
    description = Column(Text)

class Earning(Base):
    __tablename__ = 'earnings'
    id = Column(Integer, primary_key=True)
    record_id = Column(Integer, ForeignKey('financial_records.id'))
    amount = Column(Float)
    source = Column(String(100))

class ChatMessage(Base):
    __tablename__ = 'chat_messages'
    id = Column(Integer, primary_key=True)
    salon_id = Column(Integer, ForeignKey('salons.id'))
    role = Column(String(10))  # user / ai
    content = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
