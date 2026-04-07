from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class Booking(BaseModel):
    user_id: int
    daycare_id: int
    pet_name: str
    booking_time: datetime
    
bookings_db = []

@app.post("/bookings")
async def create_booking(booking: Booking):
    bookings_db.append(booking)
    
    return {"message": "Success!", "pet": booking.pet_name, "status": "Confirmed"}

@app.get("/available-slots/{daycare_id}")
async def get_slots(daycare_id: int):
    return ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00"]