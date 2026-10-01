from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class Technician(Base):
    __tablename__ = "technicians"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100))
    specialization = Column(String(50))
    is_available = Column(Boolean, default=True)

    work_orders = relationship("WorkOrder", back_populates="technician")
