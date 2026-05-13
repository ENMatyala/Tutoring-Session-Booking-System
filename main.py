from fastapi import FastAPI

from api.student_api import router as student_router
from api.tutor_api import router as tutor_router
from api.booking_api import router as booking_router
from api.session_api import router as session_router
from api.payment_api import router as payment_router
from api.review_api import router as review_router
from api.availability_slot_api import (
    router as slot_router
)

app = FastAPI(
    title="Tutor Booking System API",
    description="REST API for Tutor Booking System",
    version="1.0.0"
)

app.include_router(student_router)
app.include_router(tutor_router)
app.include_router(booking_router)
app.include_router(session_router)
app.include_router(payment_router)
app.include_router(review_router)
app.include_router(slot_router)