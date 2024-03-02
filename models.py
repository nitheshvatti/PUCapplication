from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, func, Date, Enum
from sqlalchemy.orm import relationship

from database import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(String(10), primary_key=True)
    agent_id = Column(String(10), index=True)

    customer_name = Column(String)
    customer_number = Column(String)
    insurance = Column(String)
    fuel_type = Column(String, nullable=False)
    vehicle_number = Column(String, nullable=False)
    vehicle_make = Column(String, nullable=False)
    vehicle_model = Column(String, nullable=False)
    registration_month = Column(Integer, nullable=False)
    registration_year = Column(Integer, nullable=False)
    odometer_reading = Column(Integer, nullable=False)
    barath_stage = Column(String, nullable=False)
    picture_id = Column(String, nullable=False)
    certificate_type = Column(String, nullable=False)
    expiry_date = Column(Date, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())


class User(Base):
    __tablename__ = "users"

    id = Column(String(10), primary_key=True)
    name = Column(String, nullable=False)
    number = Column(String)
    email = Column(String)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())
    role = Column(Enum('owner', 'staff'), nullable=False)
