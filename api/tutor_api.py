from fastapi import APIRouter, HTTPException
from models.tutor_model import TutorModel
from services.tutor_service import TutorService
from src.tutor import Tutor

router = APIRouter()

service = TutorService()


@router.post("/tutors")
def create_tutor(tutor: TutorModel):

    try:

        new_tutor = Tutor(
            tutor.user_id,
            tutor.email,
            tutor.password,
            tutor.tutor_id,
            tutor.name,
            tutor.subject,
            tutor.hourly_rate
        )

        created_tutor = service.create_tutor(
            new_tutor
        )

        return {
            "message": "Tutor created",
            "tutor": created_tutor.__dict__
        }

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


@router.get("/tutors")
def get_all_tutors():

    return [
        tutor.__dict__
        for tutor in service.get_all_tutors()
    ]


@router.get("/tutors/{tutor_id}")
def get_tutor(tutor_id: str):

    try:

        tutor = service.get_tutor(tutor_id)

        return tutor.__dict__

    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )


@router.delete("/tutors/{tutor_id}")
def delete_tutor(tutor_id: str):

    service.delete_tutor(tutor_id)

    return {"message": "Tutor deleted"}