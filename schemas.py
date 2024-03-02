from typing import Optional

from pydantic import BaseModel, constr


class SaveVehicle(BaseModel):
    agent_id: str
    customer_name: Optional[str]
    customer_number: Optional[str]
    insurance: Optional[str]
    fuel_type: str
    vehicle_number: constr(max_length=20)
    vehicle_make: str
    vehicle_model: str
    registration_month: int
    registration_year: int
    odometer_reading: int
    barath_stage: str
    picture_id: str
    certificate_type: str
