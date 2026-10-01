from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base

def utcnow():
    return datetime.now(timezone.utc)

class WorkOrder(Base):
    __tablename__ = "work_orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    machine_id = Column(Integer, ForeignKey("machines.id"), nullable=False)
    technician_id = Column(Integer, ForeignKey("technicians.id"), nullable=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    status = Column(String(20), nullable=False, default='open')
    priority = Column(String(10), nullable=False, default='low')
    
    opened_at = Column(DateTime, nullable=False, default=utcnow)
    assigned_at = Column(DateTime, nullable=True)
    in_progress_at = Column(DateTime, nullable=True)
    closed_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=utcnow)
    updated_at = Column(DateTime, default=utcnow, onupdate=utcnow)

    machine = relationship("Machine", back_populates="work_orders")
    technician = relationship("Technician", back_populates="work_orders")
    comments = relationship("Comment", back_populates="work_order", cascade="all, delete-orphan")
