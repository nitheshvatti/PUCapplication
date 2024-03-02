from datetime import date

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
from database import engine, SessionLocal
from schemas import SaveVehicle
from utils import generate_uuid, calculate_expiry_date

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# TODO migrations
# TODO Auth
# TODO store images

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/saveVehicle")
async def root(vehicle_data: SaveVehicle, db: Session = Depends(get_db)):
    exp_date = calculate_expiry_date(vehicle_data.certificate_type)
    new_vehicle = models.Vehicle(
        id=generate_uuid(),
        agent_id=vehicle_data.agent_id,
        customer_name=vehicle_data.customer_name,
        customer_number=vehicle_data.customer_number,
        insurance=vehicle_data.insurance,
        fuel_type=vehicle_data.fuel_type,
        vehicle_number=vehicle_data.vehicle_number,
        vehicle_make=vehicle_data.vehicle_make,
        vehicle_model=vehicle_data.vehicle_model,
        registration_month=vehicle_data.registration_month,
        registration_year=vehicle_data.registration_year,
        odometer_reading=vehicle_data.odometer_reading,
        barath_stage=vehicle_data.barath_stage,
        picture_id=vehicle_data.picture_id,
        certificate_type=vehicle_data.certificate_type,
        expiry_date=exp_date
    )
    db.add(new_vehicle)
    db.commit()
    return {"message": "Vehicle added successfully", "vehicle_id": new_vehicle.id}


@app.get("/getVehicles")
# TODO accept userId, and based on userId, return the vehicles.
# TODO If owner, return all, if staff, return the ones related to him
# TODO pagination
# TODO get vehicle based on ID
# TODO filters on date
async def fetch_vehicles(db: Session = Depends(get_db)):
    vehicles = db.query(models.Vehicle).all()
    return {"vehicles": vehicles}
