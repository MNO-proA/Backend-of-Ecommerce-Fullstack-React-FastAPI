from fastapi import status, Depends, APIRouter
from sqlalchemy.orm import Session
from . import admin_oauth2
from app.database import get_db


router = APIRouter(
    tags=["Admin Profile"]
    )


@router.post("/api/admin/profile", status_code=status.HTTP_201_CREATED)
def profile( db: Session = Depends(get_db), current_user: int = Depends(admin_oauth2.get_current_user)):
    return {"admin":"profile"}